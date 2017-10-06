import time, random, cPickle

def deleteAllTweets(api):
	''' This function deletes every tweet in the time line, deleting tweet by tweet '''
	print "Getting all tweets in current timeline..."
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
					time.sleep(random.randint(8, 29))
				except:
					print "Failed... Retrying..."
					time.sleep(5)
			print "Twitter timeline removed!"

def sendDMToAll(api, messageText):
	''' This function takes as an argument the message to send to every contact possible as a DM '''
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


def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			print "\nYou have to wait 15 minutes..."
			time.sleep(15 * 60)

def tweetFromList(api):
	''' This tweets a list of tweets in the tweetList every different tweet is on a different line '''
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