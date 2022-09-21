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

queries = [
    "東大 図書館",
    "総合図書館",
    "柏図書館",
    "本郷 図書館",
    "駒場 図書館",
    "\"駒図\""
]

for query in queries:

    tweets = twitter.search(query, result_type="recent")

    for tweet in tweets:

        # 既にファボしていたら skip する
        if tweet.favorited:
            continue

        # URL を含むツイートは対象外にする
        if tweet.entities["urls"]:
            continue

        # リプライは対象外にする
        if tweet.in_reply_to_status_id or tweet.in_reply_to_user_id:
            continue
        if hasattr(tweet, "retweeted_status") and \
                (tweet.retweeted_status.in_reply_to_status_id or tweet.retweeted_status.in_reply_to_user_id):
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
