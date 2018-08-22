
#PROBLEM 3: DERIVE THE SENTIMENTS OF NEW TERM


from __future__ import division																#IMPORTING FEATURES FROM FUTURE VERSIONS OF PYTHON
from textblob import TextBlob																#FOR NATURAL LANGUAGE PROCESSING

import re																					#REGULAR EXPRESSION TO FOR PATTERN MATCHING
import sys																					#SYS TO GET COMMAND LINE ARGUMENTS
import json																					#JSON TO GET JSON STRING
from nltk.corpus import stopwords															#TO IMPORT A SET OF STOPWORDS

operators = set(('https', 'meant', ' ','rt','does nt','doesn t','http','i'))				#USER CREATED SET
stop_words = set(stopwords.words('english')) 												#SET OF STOPWORDS
	
def main():
	words = open(sys.argv[1])
	tweets = open(sys.argv[2])
	word_scores = {}																		#DICTIONARY
	tweet_scores = {}																		#DICTIONARY
	tweet_text = []																			#LIST
	new_words = []																			#LIST

	# CREATE DICTIONARY OF TERMS AND THEIR SCORES
	for line in words:
		term, score = line.split("\t")														#SPLITTING THROUGH TAB SPACES
		word_scores[term] = int(score)

	# LOAD TEXT OF TWEETS INTO LIST
	for line in tweets:
		tweet = json.loads(line)															#TO LOAD JSON DATA
		if 'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))											#ENDECODING FROM UNICODE STRING TO BYTE STRING AND ADDING IT TO THE LIST
			
			

	# FOR ALL TWEETS
	for t in tweet_text:
		sentiment = 0 																		#INITIALIZE THE TWEET'S SENTIMENT TO 0
		breakdown = t.split() 																#SPLIT THE TWEET INTO INDIVIDUAL STRINGS
		
		# FOR EVERY WORD IN THE TWEET
		for word in breakdown:

			# IF THE WORD EXISTS IN ARGV[1], INCREASE SENTIMENT APPROPRIATELY
			# ELSE, ADD IT TO THE LIST OF NEW WORDS
			if word_scores.has_key(word):													#CHECKING IF WORD IS PRESENT IN SENTIMENT DICTIONARY
				sentiment = sentiment + word_scores[word]
			else:
				new_words.append(word)														#APPENDING NEW WORD TO LIST

		tweet_scores[t] = int(sentiment)

	# FOR ALL NEW WORDS
	for new in new_words:
		pos = neg = total = 0																#INITIALIZE THE NEW WORD SENTIMENT TO 0
		for t in tweet_scores:
			if new in t:
				if tweet_scores[t] > 0:														#CHECKING IF A WORD IS POSITIVE
					pos+=1
				elif tweet_scores[t] < 0:													#CHECKING IF A WORD IS NEGATIVE
					neg+=1
				total+=1
		
		
		tweet=" ".join(re.findall("[a-zA-Z]+", new))										#TO EXTRACT CHARACTERS ONLY
		blob=TextBlob(tweet.strip())														#TO REMOVE EXTRA SPACES AND DUPLICATE VALUES
		if (pos - neg)/total!= 0.0 and blob.lower() not in stop_words and blob.lower() not in operators and len(blob) > 1 and len(blob) < 16:
			print 'Word :',blob, ' 	  Score  :	 ', '%.3f'%((pos - neg)/total)				#PRINTING THE RESULT

if __name__ == '__main__':
    main()																					#MAIN FUNCTION CALL