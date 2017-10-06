#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, random

#hashtag = str(raw_input("Enter a hastag if you want: "))
#print "Hastag to use "+hashtag

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			print "\nYou have to wait 15 minutes..."
			time.sleep(15 * 60)

num_line = 0

with open('numero.pickle', 'rb') as fLoad:
	line_number = int(cPickle.load(fLoad))

with open('tweetList.txt', 'r') as tweetsFile:
	f=tweetsFile.readlines()

for line in f:

	line = line+" "+hashtag
	line = line.strip()
	line = line.strip('\n')

	if num_line == line_number and line != f[-1] and len(line) <= 140:
		num_line+=1
		line_number+=1

		with open('numero.pickle', 'wb') as fWrite:
			cPickle.dump(num_line, fWrite)

		api.update_status(status=line)
		print line
		wating_dig = int(random.random()*5+15) * 60
		print wating_dig/60
		time.sleep(wating_dig) # n minutes

	elif line == f[-1] and len(line) <= 140:
		num_line = 0
		with open('numero.pickle', 'wb') as fWrite:
			cPickle.dump(num_line, fWrite)

		api.update_status(status=line)
		print line

	else:
		if len(line) >140:
			line_number+=1
		num_line+=1
		print "Next Line %d" % (num_line)
		continue
