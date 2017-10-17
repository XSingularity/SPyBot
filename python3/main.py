import tweepy
import webbrowser
from SPylib import *

consumer_key = '4bjxMFFpjPgsn6gH6ImbtzhZf'
consumer_secret = 'Ung82wKl7Cl6Hk3oQMjkvfZmPUll3boRzzGEUyR6ZcRFcAzFue'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Redirect user to Twitter to authorize
webbrowser.open(auth.get_authorization_url())

# Get access token
verifier_value = input('Verifier value: ')
auth.get_access_token(verifier_value)

api = tweepy.API(auth)

funcs = [delTweetsFromFile, delAllTweets, tweetFromList, unfollowNonFollowers, unfollowAll, sendDMToAll, delAllDm]

while True:
	try:
		print("Press Ctrl+c to exit")
		print("Select what you want to do:\n(1) Delete every tweet with twitter file\n(2) Delete every tweet from twitter\n(3) Start Tweeting from 'tweetList.txt'\n(4) Unfollow Non-followers\n(5) Unfollow everybody\n(6) Send a DM to every friend\n(7) Delete every Dm")

		sel = int(input('Option: '))

		funcs[sel-1](api)
	except KeyboardInterrupt:
		print("\n\nHave a good one!\n")
		break
	except Exception as e:
		print(e)
	