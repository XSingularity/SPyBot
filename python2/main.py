#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from SPylib import *

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

funcs = [delTweetsFromFile, delAllTweets, tweetFromList, unfollowNonFollowers, unfollowAll, sendDMToAll, delAllDm]

while True:
	try:
		print "Press Ctrl+c to exit"
		print "Select what you want to do:\n(1) Delete every tweet with twitter file\n(2) Delete every tweet from twitter\n(3) Start Tweeting from 'tweetList.txt'\n(4) Unfollow Non-followers\n(5) Unfollow everybody\n(6) Send a DM to every friend\n(7) Delete every Dm"

		sel = int(raw_input('Option: '))

		funcs[sel-1](api)
	except KeyboardInterrupt:
		print "\n\nHave a good one!\n"
		break
