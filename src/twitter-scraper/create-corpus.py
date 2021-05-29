from tweet_repository import TweetRepository


class CreateCorpus:
    def generate_corpus(self):
        tr = TweetRepository()
        tr.connect()
        tweets = tr.get_all_tweets()
        tweet_content = []
        for i in tweets:
            # other preproc?
            tweet_content.append(i['content'])

    def write_to_txt(self, path="./corpus.txt", tweets=None):
        if tweets is None:
            return
        with open(path, 'w') as f:
            for t in tweets:
                f.write(t)
