import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
#import codecs

consumer_key ='HzZpvfMusPz9rOujU6XAjruBW'
consumer_secret = 'oJ9IdjidamiZC1HZTO7gyRvrVcyHXKyaDkM7TdCOhAy3bgE7JS'
access_token = '960464454252187653-hq9PoZZ81wisLPjt2xA6ogEgq5Ic6cG'
access_token_secret = 'NcvGN0Lln0F4MD730krA94TFl2jlCfxbQ1v1ZcK6XAyOk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class listener(StreamListener):
    
    def __init__(self):
        self.compteur=0
        #self.mon_fichier = codecs.open("fichier.txt", "a","utf-8")
        self.liste=[]
        
    def on_data(self, data):
        all_data = json.loads(data.decode('utf-8','ignore').encode('utf-8'))
        
		# collect all desired data fields 
        if 'text' in all_data:
          tweet         = all_data["text"]
          created_at    = all_data["created_at"]
          retweeted     = all_data["retweeted"]
          username      = all_data["user"]["screen_name"]
          user_tz       = all_data["user"]["time_zone"]
          user_location = all_data["user"]["location"]
          user_coordinates   = all_data["coordinates"]
		  
          
          #self.mon_fichier.write(tweet+"\n")
          
          self.compteur=self.compteur+1
          self.liste.append(tweet)
          print((self.compteur,username,tweet))
          #print(self.liste[self.compteur-1])
          if self.compteur >= 2:
              #self.mon_fichier.close()  
              return False
          return True   
        else:
            return True
            
    def retrieveList(self):
        return self.liste
    
    def on_error(self, status):
        print(status)

    def getTrends(self):
        trends1 = api.trends_place(23424819) # france
        # trends1 is a list with only one element in it, which is a 
        # dict which we'll put in data.
        data = trends1[0] 
        # grab the trends
        trends = data['trends']
        # grab the name from each trend
        names = [trend['name'] for trend in trends]
        return names
        
#twitterStream = Stream(auth, listener())
#le contenu de la recherche se met ici dans track
#twitterStream.filter(track=["france"],languages = ["fr"], stall_warnings = True)
        
        