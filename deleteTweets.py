import tweepy, time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

if __name__ == '__main__':
	# Create authentication token
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	print "Getting all tweets in current timeline..."

	# Get all tweets for the account
	# API is limited to 350 requests/hour per token
	api = tweepy.API(auth)
	while True:
		timeline = api.user_timeline(count = 350)

		print "Found: %d" % (len(timeline))
		if len(timeline) < 1:
			print "There is no timeline"
			break
		else:
			print "Removing..."
			# Delete tweets one by one
			for t in timeline:
				try:
					api.destroy_status(t.id)
					time.sleep(30)
				except:
					print "Failed... Retrying..."
					time.sleep(5)
			print "Twitter timeline removed!"
