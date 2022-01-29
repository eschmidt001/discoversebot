#i haven't touched python in months
import numpy as np 
#import tweepy
import json
import random
import re

#TODO: credential stuff from separate file ONCE THEY GIVE THEM TO ME

#here's the plan: take lyrics 
f = open('Lyrics_fredodisco.json')
g = json.load(f) #dictionary
songs = g['songs'] #list of dictionaries/song

#select song and spot to start
n1 = random.randint(0, len(songs)-1)
lyr = songs[n1]['lyrics']

#preprocessing
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

print(songs[n1]['title'])
n2 = random.randint(0,len(lines)-3) #extract length (tweet limit is 280 chars)
t = lines[n2]
i = 1
while len(t) < 280:
    if (n2+i) < (len(lines)-1):
        t = t + lines[n2+i]
        i = i+1
    else: break
if len(t) > 279:
    tw = lines[n2:n2+i-2]
else: tw = lines[n2:n2+i]
print(len(''.join(tw)))
print(tw)
#tweet out length

#yeehaw that's the program