#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time#, time, cPickle, random

#hashtag = str(raw_input("Enter a hastag if you want: "))
#print "Hastag to use "+hashtag

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="Alguien").pages():
    ids.extend(page)
    time.sleep(60)

for nf in ids:
    print "Unfollowing %s" % nf.screen_name
    try:
        nf.unfollow()
    except:
        print "Failed, sleeping for 5 seconds and then trying again."
        time.sleep(5)
        nf.unfollow()
    print "Completed, sleeping for 1 second."
time.sleep(1)

'''
with open('myFollowers.pickle', 'rb') as fLoad:
	myFollowers = cPickle.load(fLoad)

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			print "\nYou have to wait 15 minutes..."
			time.sleep(15 * 60)


for follower in limit_handled(tweepy.Cursor(api.followers).items()):
	try:
		if follower.following and follower.screen_name not in myFollowers:
			print follower.screen_name
			apifollower.unfollow()
	except tweepy.TweepError:
		print "Already Requested"

num_line = 0

with open('numero.pickle', 'rb') as fLoad:
	line_number = int(cPickle.load(fLoad))

with open('osoText.txt', 'r') as osoText:
	f=osoText.readlines()

for line in f:

	line = line+" "+hashtag

	line = line.strip()
	line = line.strip('\n')
	line = line.replace('oso', 'OSO') # Hace que todo sea mas OSO
	line = line.replace('hombre', 'OSO') # Hace que todo sea mas OSO
	line = line.replace('mujer', 'OSA') # Hace que todo sea mas OSO

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
'''