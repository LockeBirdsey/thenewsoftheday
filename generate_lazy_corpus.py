from create_corpus import CreateCorpus


def create_corpus_all(path=None):
    cc = CreateCorpus()
    corpus_as_list = cc.generate_corpus()
    print("Number of tweets {}".format(len(corpus_as_list)))
    cc.write_to_txt(tweets=corpus_as_list)


if __name__ == "__main__":
    create_corpus_all()
