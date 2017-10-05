import tweepy, time

consumer_key = 'dE28fOWH3JNqiih3VMTLfq4hx'
consumer_secret = '8AIEdGvu6LhYdcJZfE3lIWaGdj2GgQBDpOMf0UBeSMgyHryJvX'
access_token = '108980977-oyfwVzqpnHtbR2WsETuFNYVJZnjJh1UTHstCEOoW'
access_token_secret = 'Et7rVI8jvm4dkxels2QVQ5CRJt8gDC3vw4OHzz7zDaSrL'

if __name__ == '__main__':
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Getting all tweets..."

    # Get all tweets for the account
    # API is limited to 350 requests/hour per token
    api = tweepy.API(auth)
    while True:
	    timeline = api.user_timeline(count = 350)

	    print "Found: %d" % (len(timeline))
	    if len(timeline) < 1:
	    	print "There is no timeline"
	    	break
	    print "Removing..."

	    # Delete tweets one by one
	    for t in timeline:
	    	try:
	    		api.destroy_status(t.id)
	    	except:
	    		print "Failed... Retrying..."
	    		time.sleep(5)
	    print "Twitter timeline removed!"
