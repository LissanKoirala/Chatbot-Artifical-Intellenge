from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from textblob import TextBlob
from unidecode import unidecode
import time

client_key = "PiYkEo37L8ZpIqADjcV33vvjb"
client_secret = "AYRtpZQiPw2EQsPV2G7JOexgrjvF16xATNz2pykPqDhRxzHpWl"

access_token = "1244290622665691137-qS5vnYQQi8y0sVe7USFi92h4O5bFWf"
access_secret = "vpIhUTaShcFKUxZDILqkcNgI6050oOomLGuSpPbwyFExM"

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()



class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']

            analysis = TextBlob(tweet)
            sentiment = analysis.sentiment.polarity

            #print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return True

    def on_error(self, status):
        print(status)


while True:

    try:
        auth = OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_secret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["a","e","i","o","u"]) # To track all the tweets coming through
        #twitterStream.filter(track=["$hood", "robinhood", "stock", "$VIX"]) # To track specific terms.
    except Exception as e:
        print(str(e))
        time.sleep(5)
