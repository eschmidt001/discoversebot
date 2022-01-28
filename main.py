#i haven't touched python in months
#all thaaaaaaaaaat jazz....BORING but required
import numpy as np 
#import tweepy
import json
import random

#TODO: credential stuff from separate file ONCE THEY GIVE THEM TO ME
#lord please let me always use the right python interpreter

#here's the plan:
#take lyrics 
f = open('Lyrics_fredodisco.json')
g = json.load(f) #dictionary

songs = g['songs'] #list of dictionaries/song

#select song and spot to start
n1 = random.randint(0, len(songs))
lyr = songs[n1]['lyrics']
lyr = lyr[:lyr.find('1')]
#remove '1embed'.  can also search for it in last line and remove more elegantly, since sometimes last letter cut off

#this likely be done more elegantly using filter and regular expressions
lines = lyr.splitlines()[1:] #cut out title
while "" in lines:
    lines.remove('') # trim empty strings
for l in lines: 
    if l[0] == '[': #remove words in brackets
        lines.remove(l)

#also need to find and replace instances of \u2005 with '' within strings
#I wonder if that's something genius uses to rat out who's using their lyrics
print(lines)
n2 = random.randint(0,len(lines)-1)
#choose length (tweet limit is 280 chars)

#tweet out length

#yeehaw that's the program