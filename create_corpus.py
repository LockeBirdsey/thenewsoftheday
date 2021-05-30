import codecs
import csv
import re

from tweet_repository import TweetRepository


class CreateCorpus:
    def generate_corpus(self):
        tr = TweetRepository()
        tr.connect()
        tweets = tr.get_all_tweets()
        tweet_content = []
        for i in tweets:
            # other preproc?
            tweet_content.append(i['text'].replace("\n", " "))
        tr.close()
        return tweet_content

    def write_to_csv(self, path="./corpus.csv", tweets=None):
        if tweets is None:
            return
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["TEXT"])
            for t in tweets:
                ut = self.deEmojify(t).encode('ascii', 'ignore')
                writer.writerow([ut])

    @staticmethod
    def deEmojify(text):
        regex_pattern = re.compile(pattern="["
                                           u"\U0001F600-\U0001F64F"  # emoticons
                                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                           "]+", flags=re.UNICODE)
        return regex_pattern.sub(r'', text)
