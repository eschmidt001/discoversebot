#i haven't touched python in months
import numpy as np 
import tweepy
import json
import random
import re
from private.creds import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from private.creds import lyric_file

#here's the plan: take lyrics 
f = open(lyric_file)
g = json.load(f) #dictionary
songs = g['songs'] #list of dictionaries/song

#select song and spot to start
n1 = random.randint(0, len(songs)-1)
lyr = songs[n1]['lyrics']

#preprocessing - might want to do this for all lyrics, move this to private file, then select from there
x = re.search(r'[0-9]+[E,e]', lyr) #remove 'embed' and surrounding numbers. 
if x is None:
    x = re.search(r'[E,e]mbed', lyr)
lyr = lyr[:x.start()]
lyr = lyr.replace('\u2005', ' ') #remove fake spaces
lyr = lyr.replace('\\', "") #remove backslashes
#this likely be done more elegantly using filter and regular expressions
lines = lyr.splitlines()[1:] #cut out title
while "" in lines:
    lines.remove('') # trim empty strings
for l in lines: 
    if l[0] == '[': #remove words in brackets
        lines.remove(l)

"""picks a section of a song from song n1"""
def get_line():
    n2 = random.randint(0,len(lines)-3) #extract length (tweet limit is 280 chars)
    t = lines[n2]
    i = 1
    while len(t) < 280 and (i<5):
        if (n2+i) < (len(lines)-1) :
            t = t + lines[n2+i]
            i = i+1
        else: break
    if len(t) > 279:
        tw = lines[n2:n2+i-2]
    else: tw = lines[n2:n2+i]
    return '\n'.join(tw)

#tweet out length
"""when called, reach the twitter API using tweepy and post the given tweet in line"""
def t_out():
    line = get_line()

    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    status = api.update_status(status= line)
    
t_out() #theoretically the .bat automatically triggered every day should do the job
#yeehaw that's the program