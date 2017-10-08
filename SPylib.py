import time, random, cPickle, sys, tweepy

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.TweepError:
			print "Rate limit reached wait 15 minutes"
			time.sleep(15*60)

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
			try:
				for t in timeline: # Delete tweets one by one
					api.destroy_status(t.id)
					time.sleep(random.randint(8, 29))
			except tweepy.RateLimitError:
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
		for follower in followers:
			DirectMessage(follower, messageText) # Send them a dm
			time.sleep(random.randint(1, 3))
	except tweepy.RateLimitError:
		time.sleep(17 * 60)
		print "Too many requests wait 17 minutes..."

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

def unfollowNonFollowers(api):
	num = 0
	followers = []
	friends = []
	print "Loading followers.."
	
	for follower in limit_handled(tweepy.Cursor(api.followers).items()):
		followers.append(follower)
		print "%s" % follower.screen_name
		time.sleep(1)

	print "Found %s followers, finding friends.." % len(followers)
	for friend in limit_handled(tweepy.Cursor(api.friends).items()):
		friends.append(friend)
		time.sleep(1)

	# creating dictionaries based on id's is handy too

	friend_dict = {}
	for friend in friends:
		friend_dict[friend.id] = friend

	follower_dict = {}
	for follower in followers:
		follower_dict[follower.id] = follower

	# now we find all your "non_friends" - people who don't follow you
	# even though you follow them.

	non_friends = [friend for friend in friends if friend.id not in follower_dict]

	# Double Check cuz... you know... users...

	print "Unfollowing %s people who don't follow you back" % len(non_friends)
	print "This will take approximately %s minutes." % (len(non_friends) / 60.0)
	answer = raw_input("Are you sure? [Y/n]").lower()
	if answer and answer[0] != "y":
		sys.exit(1)

	for nf in non_friends:
		print "Unfollowing %s" % nf.screen_name
		try:
			nf.unfollow()
		except:
			print "Failed... Wait 5 seconds...."
			time.sleep(5)
			nf.unfollow()
		print "Succesful... Wait 1 second..."
	time.sleep(1)

def unfollowAll(api):
	''' This will unfollow every friend '''
	print "Setting up..."
	# Double Check cuz... you know... users...
	answer = raw_input("Are you sure? [Y/n]: ").lower()
	if answer and answer[0] != "y":
		sys.exit(1)

	for friend in limit_handled(tweepy.Cursor(api.friends).items()):
		print "Unfollowing %s" % friend.screen_name
		friend.unfollow()
		time.sleep(1)

def delAllDm(api):
	for page in tweepy.Cursor(api.sent_direct_messages, count=100).pages():
		for dm in page:
			print dm.text
			api.destroy_direct_message(dm.id)
