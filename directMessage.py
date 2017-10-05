#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy#, time, cPickle, random

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_secret_token = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_secret_token)

api = tweepy.API(auth)

'''
with open('myFollowers.pickle', 'rb') as fLoad:
	myFollowers = cPickle.load(fLoad)
'''
messageText = "Hola camarada ¡Un saludo revolucionario! La comuna Santa Ines de Catia te invita a participar en un sorteo donde estaremos ofreciendo: Dos tablets, y una Cava ¡Participa, y Gana!"

'''
def addNewToDb(newAccounts):
	with open('myFollowers.pickle', 'wb') as fWrite:
		myFollowers.extend(newAccounts)
		cPickle.dump(myFollowers, fWrite)
'''
def DirectMessage(userId, messageText):
	api.send_direct_message(screen_name=userId, text=messageText)

newFollowers = list()
def GetNewFollowers():
	for follower in tweepy.Cursor(api.followers).items():  # For each follower i have
		'''if follower.following and follower.screen_name not in myFollowers: # If im not following them
			print 'New Follower: {0}'.format(follower.screen_name)'''
		newFollowers.append(follower.screen_name)
	#addNewToDb(newFollowers)
	return newFollowers # Return list of new followers

#while True:
try:
	GetNewFollowers()
	for x in newFollowers:
		DirectMessage(x, messageText) # Send them a dm
	#time.sleep(int(random.random()*20+15) * 60)
except tweepy.RateLimitError:
	time.sleep(17 * 60)
	print "Too many requests wait 17 minutes..."
