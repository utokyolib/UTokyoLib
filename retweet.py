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

# 1週間前以降のツイートに絞る
tweets = [tweet for tweet in tweets if tweet.created_at >= datetime.today() - timedelta(days=7)]

# 開館に関するツイートに絞る
tweets = [tweet for tweet in tweets if "開館" in tweet.text or "開室" in tweet.text]


for tweet in tweets:
    try:
        if tweet.retweeted:
            twitter.unretweet(tweet.id)
        twitter.retweet(tweet.id)
        logging.info(f"{tweet.user.screen_name} さんによる以下のツイートをRTしました: ")
        logging.info(tweet.text)
    except tweepy.error.TweepError as e:
        logging.info(e)
