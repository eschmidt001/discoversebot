
from lyricsgenius import Genius

#TODO: credential stuff from separate file ONCE THEY GIVE THEM TO ME
#lord please let me always use the right python interpreter

#here's the plan:
#take lyrics from genius (definitely not allowed but oh well it's just for personal purposes)
gtoken = 'X781DaTOSyVR_DR2EgevfwPEsWqoSyw5cLwmUmKN4ced4KbpVst6GoRIQLV2jiaa'

genius = Genius(gtoken)
artist = genius.search_artist("fredo disco", max_songs=4, sort="title")
artist = genius.search_artist("fredo disco", sort="title")
#print(artist.songs)
artist.save_lyrics()