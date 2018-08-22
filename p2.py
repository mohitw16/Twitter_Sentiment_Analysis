
#PROBLEM 2: DERIVE THE SENTIMENTS OF EACH TWEET

import sys																							#SYS TO GET COMMAND LINE ARGUMENTS
import json																							#JSON TO GET JSON STRING
sentimentData = sys.argv[1] 
twitterData = sys.argv[2] 
    
def tweet_dict(twitterData):  
    
    twitter_list_dict = []
    twitterfile = open(twitterData)																	#OPENING THE FILE
    for line in twitterfile:
        twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))								#DECODING BYTE STRING TO UNICODE AND ADDING IT TO THE LIST
        twitter_list_dict.append(json.loads(line))

    twitterfile.close()																				#CLOSING THE FILE
    return twitter_list_dict
    
def sentiment_dict(sentimentData):
    
    afinnfile = open(sentimentData)																	#OPENING THE FILE
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t") 															#SPLITTING THROUGH TAB SPACES
        scores[term] = int(score)  

    afinnfile.close()																				#CLOSING THE FILE
    return scores 
    
def main():
    
    
    tweets = tweet_dict(twitterData)																#LIST OF TWEETS
    sentiment = sentiment_dict(sentimentData)														#DICTIONARY OF SENTIMENT
    
    for index in range(len(tweets)):
        tweet_word = tweets[index]['text'].split()													#SPLITTING THROUGH TEXT PART IN A TWEET
        sent_score = 0
        for word in tweet_word:
            word = word.rstrip('?:!.,;"!@')															#REMOVING SPECIAL SYMBOLS
            word = word.replace("\n", "")															#REPLACING NEW LINE WITH SPACE
            
            if not (word.encode('utf-8', 'ignore') == ""):											#CHECKING IF ENCODED STRING HAS ANY VALUE
                if word.encode('utf-8') in sentiment.keys():										#CHECKING IF WORD IS PRESENT IN SENTIMENT DICTIONARY
                    sent_score = sent_score + int(sentiment[word])
                    
                else:
                    sent_score = sent_score
                    
        print 'Tweet number',index,' having sentiment_score',int(sent_score)						#PRINTING THE RESULT
    
if __name__ == '__main__':
    main()																							#MAIN FUNCTION CALL
