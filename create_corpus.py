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

    def write_to_txt(self, path="./corpus.txt", tweets=None):
        if tweets is None:
            return
        with open(path, 'w', encoding="utf-8") as f:
            for t in tweets:
                f.write(t + "\n")
