
#PROBLEM 1: GET THE TWITTER DATA


import tweepy																					#TWEEPY TO PROVIDE ACCESS TO TWITTER DATA
from tweepy import OAuthHandler																	#OAUTH TO PROVIDE AUTHENTICATION TO TWITTER DATA
from tweepy import Stream																		#STREAM TO PROVIDE STREAM TO TWITTER DATA
from tweepy.streaming import StreamListener														#TO INHERIT THE CLASS STREAMLISTENER

#AUTHENTICATION KEYS
consumer_key = "x6M3VQJyb5eH9YSC8ocVBneCK"
consumer_secret= "22jUUM7D2VezY05EWrapfmAv0mpoIKgxgellZBHFAPvbH1pi9o"
access_token = "915185600344465408-j0Wg6rX7kgLNRElavMxMFsTaCKIHzgS" 
access_token_secret = "iykoWGzghtI1csKXUZoVucDCVI1b1ga0RNWMUgmkCuhmr"


class StdOutListener(StreamListener):
   
  def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:  												#OPENING JSON FILE IN APPEND MODE
			  
				f.write(data)																	#WRITING DATA INTO JSON FILE
				
				ff=open('output.txt','a')														#OPENING TEXT FILE IN APPEND MODE													
				ff.write(data)																	#WRITING DATA INTO TEXT FILE															
				return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))													#ERROR IN CASE OF CONNECTION LOST
        return True
 
  def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True																				 #TO CONTINUE LISTENING
 
  def on_timeout(self):
        print('Timeout...')																		#ERROR IN CASE OF TIMEOUT
        return True 																			#TO CONTINUE LISTENING
 
if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)									#GETTING AUTHENTICATION
    auth.set_access_token(access_token, access_token_secret)
 
    stream = Stream(auth, listener)																#GETTING STREAM OF DATA
    stream.filter(track=['economy'])															#FILTERING THE STREAM AND TRACKING THE INFORMATION