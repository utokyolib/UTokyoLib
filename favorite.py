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

# 「駒場 図書館」で検索
komaba_tweets = twitter.search("駒場 図書館", result_type="recent")

for tweet in komaba_tweets:

    # 既にファボしていたら skip する
    if tweet.favorited:
        continue

    # URL を含むツイートは対象外にする
    if tweet.entities["urls"]:
        continue

    # リプライは対象外にする
    if tweet.in_reply_to_status_id or tweet.in_reply_to_user_id:
        continue

    # 自分自身のツイートは対象外にする
    if tweet.user.screen_name == "UTokyoLib_bot":
        continue

    try:
        twitter.create_favorite(tweet.id)
        logging.info(f"{tweet.user.screen_name} さんによる以下のツイートをファボしました: ")
        logging.info(tweet.text)
    except tweepy.error.TweepError as e:
        logging.info(e)


# 「本郷 図書館」で検索
hongo_tweets = twitter.search("本郷 図書館", result_type="recent")

for tweet in hongo_tweets:

    # 既にファボしていたら skip する
    if tweet.favorited:
        continue

    # URL を含むツイートは対象外にする
    if tweet.entities["urls"]:
        continue

    # リプライは対象外にする
    if tweet.in_reply_to_status_id or tweet.in_reply_to_user_id:
        continue

    # 自分自身のツイートは対象外にする
    if tweet.user.screen_name == "UTokyoLib_bot":
        continue

    try:
        twitter.create_favorite(tweet.id)
        logging.info(f"{tweet.user.screen_name} さんによる以下のツイートをファボしました: ")
        logging.info(tweet.text)
    except tweepy.error.TweepError as e:
        logging.info(e)


# 「総合図書館」で検索
sogo_tweets = twitter.search("総合図書館", result_type="recent")

for tweet in sogo_tweets:

    # 既にファボしていたら skip する
    if tweet.favorited:
        continue

    # URL を含むツイートは対象外にする
    if tweet.entities["urls"]:
        continue

    # リプライは対象外にする
    if tweet.in_reply_to_status_id or tweet.in_reply_to_user_id:
        continue

    # 自分自身のツイートは対象外にする
    if tweet.user.screen_name == "UTokyoLib_bot":
        continue

    try:
        twitter.create_favorite(tweet.id)
        logging.info(f"{tweet.user.screen_name} さんによる以下のツイートをファボしました: ")
        logging.info(tweet.text)
    except tweepy.error.TweepError as e:
        logging.info(e)
