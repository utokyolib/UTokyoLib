import datetime
import logging
import os

import tweepy

import library

CK = os.environ["TWITTER_CONSUMER_KEY"]
CS = os.environ["TWITTER_CONSUMER_SECRET"]
AT = os.environ["TWITTER_ACCESS_TOKEN"]
AS = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
twitter = tweepy.API(auth)

dt_now = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)

YEAR = dt_now.year
MONTH = dt_now.month
DAY = dt_now.day
w_list = ['月', '火', '水', '木', '金', '土', '日']
WEEKDAY = w_list[dt_now.weekday()]

libdic = [
    ("柏図書館", 500840),
    ("駒場図書館", 300300),
    ("総合図書館", 100001)
]


logging.basicConfig(level=logging.INFO)

for (library_name, library_num) in libdic:
    opening_type, opening_info \
        = library.fetch_opening_info(library_num, year=YEAR, month=MONTH, day=DAY)

    tweet_content = \
        f"{MONTH}/{DAY}({WEEKDAY}) {library_name}\n\n【{opening_type}】\n{opening_info}\n\n" + \
        "※実際の日付と異なる場合があります。必ず https://www.lib.u-tokyo.ac.jp/ja もご確認ください。"
    twitter.update_status(tweet_content)

    logging.info(f"{library_name} done!")
