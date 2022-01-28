
#fuck i haven't touched python in months
#all thaaaaaaaaaat jazz....BORING but required
import numpy as np 
#import tweepy
import json

#TODO: credential stuff from separate file ONCE THEY GIVE THEM TO ME
#lord please let me always use the right python interpreter

#here's the plan:
#take lyrics 
f = open('Lyrics_fredodisco.json')
#returns JSON object as a dictionary
g = json.load(f)
h = g.keys()
j = g['songs'] # list of dictionaries/song
print(type(j))
k = j[6]['lyrics']

songs = json.load(f)['songs'] #list of dictionaries/song
#select spot to start


#choose length

#tweet out length

#yeehaw that's the program