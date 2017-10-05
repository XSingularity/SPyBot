#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy#, time, random

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_secret_token = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_secret_token)

api = tweepy.API(auth)

messageText = "Hola esto es una prueba"

def DirectMessage(userId, messageText):
	api.send_direct_message(screen_name=userId, text=messageText)

followers = list()
def GetFollowers():
	for follower in tweepy.Cursor(api.followers).items():  # For each follower i have
		followers.append(follower.screen_name)
	return followers # Return list of new followers

try:
	GetFollowers()
	for x in followers:
		DirectMessage(x, messageText) # Send them a dm
	#time.sleep(int(random.random()*20+15) * 60)
except tweepy.RateLimitError:
	time.sleep(17 * 60)
	print "Too many requests wait 17 minutes..."
