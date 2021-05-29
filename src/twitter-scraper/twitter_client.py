#!/usr/bin/env python
# encoding: utf-8
import os
import re
from pathlib import Path

import tweepy  # https://github.com/tweepy/tweepy
import langdetect
from key_manager import KeyManager
from tweet_repository import TweetRepository


class MyStreamListener(tweepy.StreamListener):
    tr = None

    def on_connect(self):
        self.tr = TweetRepository()

    def on_status(self, status):
        if status.truncated is True:
            try:
                content = status.extended_tweet["full_text"]
            except AttributeError:
                content = status.full_text
        else:
            content = status.text
        if not hasattr(status, "retweeted_status"):
            # ignore
            try:
                if langdetect.detect(content) == 'en':
                    self.tr.connect()
                    self.tr.save_new_tweet(status.id_str, status.created_at, content)
                    self.tr.close()
                    print(self.remove_link(content.replace("\n", "")))
            except Exception as e:
                print(e)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    @staticmethod
    def remove_link(string):
        links = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', string)
        return links


class TwitterClient:
    TWITTER_KEYS = str(Path(os.getcwd()).joinpath("resources").joinpath("keys.yaml"))

    def auth_user_to_app(self):
        keys = KeyManager(self.TWITTER_KEYS)
        auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        print(auth.get_authorization_url())
        verifier = input('Verifier:').strip()
        token = auth.get_access_token(verifier)
        print(token)

    def create_auth(self):
        keys = KeyManager(self.TWITTER_KEYS)
        auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
        return auth
        # return tweepy.API(auth)

    def read_stream(self):
        auth = self.create_auth()
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
        myStream.filter(track=['#BREAKINGNEWS', '#breakingnews', '#news', '#NEWS'])

    def tweet(self, the_tweet, the_image_path):
        api = tweepy.API(self.create_auth())
        media = api.media_upload(the_image_path)
        api.update_status(status=the_tweet, media_ids=[media.media_id])


if __name__ == "__main__":
    tr = TweetRepository()
    tr.connect()
    tr.create_tables()
    tr.close()
    tc = TwitterClient()
    tc.read_stream()
