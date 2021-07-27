from datetime import datetime, timedelta
import logging
import os
import tweepy

CK = os.environ["TWITTER_CONSUMER_KEY"]
CS = os.environ["TWITTER_CONSUMER_SECRET"]
AT = os.environ["TWITTER_ACCESS_TOKEN"]
AS = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
twitter = tweepy.API(auth)

logging.basicConfig(level=logging.INFO)


tweets = twitter.home_timeline(count=200)
# 自分自身のツイートは対象外にする
tweets = [tweet for tweet in tweets if tweet.user.screen_name != "UTokyoLib_bot"]

# 5時間以内のツイートに絞る
tweets = [tweet for tweet in tweets if tweet.created_at >= datetime.today() - timedelta(hours=5)]

# 開館・閉館に関するツイートに絞る
tweets = [tweet for tweet in tweets if "開館" in tweet.text or "開室" in tweet.text or "閉館" in tweet.text or "閉室" in tweet.text or "休館" in tweet.text or "休室" in tweet.text]

# 最近の RT が上に来るようにする
tweets.reverse()

for tweet in tweets:
    try:
        twitter.retweet(tweet.id)
        logging.info(f"{tweet.user.screen_name} さんによる以下のツイートをRTしました: ")
        logging.info(tweet.text)
    except tweepy.error.TweepError as e:
        logging.info(e)
