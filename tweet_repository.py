import psycopg2
from psycopg2.extras import RealDictCursor
import os


class TweetRepository:
    conn = None
    DATABASE_URL = os.environ['DATABASE_URL']

    # DATABASE_URL = ""
    # Attempt to connect to the database
    def connect(self):
        try:
            self.conn = psycopg2.connect(self.DATABASE_URL)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # Executes a query and returns all results
    def query(self, query):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            all_results = cur.fetchall()
            cur.close()
            return all_results
        except Exception as e:
            print(e)

    # TODO
    def get_all_tweets_in_range(self):
        print('s')

    def get_all_tweets(self):
        return self.query("SELECT * FROM Tweets;")

    def save_new_tweet(self, tweet_id, created_at, text):
        insert_string = "INSERT INTO Tweets(id, created_at, text) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING"
        cur = self.conn.cursor()
        cur.execute(insert_string, (int(tweet_id), created_at, text))
        self.conn.commit()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Tweets(id bigint PRIMARY KEY, created_at varchar(255), text varchar(5000));")
        self.conn.commit()

    def drop_tables(self):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE Tweets;")
        self.conn.commit()

    # Close DB connection
    def close(self):
        if self.conn is not None:
            self.conn.close()
