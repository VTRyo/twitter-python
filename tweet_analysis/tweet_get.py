#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from env import CONFIG
import tweepy
import csv

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#ツイート取得
tweet_data = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name = "3s_hv",exclude_replies = True).items():
    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open('tweets_20191109.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
pass