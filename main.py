#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, random
from SPylib import *

consumer_key = 'hg4362Sz3sgkXIenj5WMvOO04'
consumer_secret = 'V8lEbVid61uBJy3W0UX2nNp7z7lAXPLYOPcQIlYZQJCNPrcajp'
access_token = '900453085876768770-74jZd2G14bTRVEeF8U8Khk5UGyTUsXz'
access_token_secret = '3b3wnz1OU7f95Io5T4EXyYv3g4PuHQst0J9M2GE5JkTOd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

deleteAllTweets(api)