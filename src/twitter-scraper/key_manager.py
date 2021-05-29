import yaml


class KeyManager:
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""

    def __init__(self, location):
        with open(location) as f:
            keys = yaml.load(f, Loader=yaml.FullLoader)

        self.CONSUMER_KEY = keys["consumer_key"]
        self.CONSUMER_SECRET = keys["consumer_secret"]
        self.ACCESS_KEY = keys["token"]
        self.ACCESS_SECRET = keys["secret"]
