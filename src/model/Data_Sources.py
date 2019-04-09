import csv
import json
import sys
import csv
import re
import os
import string
from textblob import TextBlob

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
from simple_salesforce import Salesforce

class Data_Sources:
	def __init__(self):
		self.consumer_key= 'sljGvj4bKLY9LPKlHpySGuMW5'
		self.consumer_secret= 'MGDfahGilqS0pJBxLOVk5FPAfqluLs51XCzZUWdd8TF2QuQ7WQ' 
		self.access_token = '2894483640-G5e7wjEW8FoKCmCrq8lWG0OR2E1e07gqympzid9'
		self.access_secret= 'D8EMLNXFT3SiaXpKjeWBX5f0cxbOjBdFjqvbek5YR2QxA'
		
		self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_secret)
		self.auth_api = API(self.auth)
		self.sf = None

	#def open_sf_connection(self):
	#self.sf = Salesforce(username='anmolsgandhi@gmail.com', password='Password575757', security_token='R0bSAm9uQT0A3pol6Cl0Q0L9D')

	def get_twitter_info(self,usernames):
		self.account_list = usernames
		self.twitter_obj = {}

		if len(self.account_list) > 0:

			for self.target in self.account_list:
				self.hashtags = []
				self.mentions = []
				self.tweet_count = 0
				self.end_date = datetime.utcnow() - timedelta(days=300)

				for self.status in Cursor(self.auth_api.user_timeline, id=self.target).items():
					self.tweet_count += 1
					
					if hasattr(self.status, "entities"):
						self.entities = self.status.entities
						
						if "hashtags" in self.entities:
							for self.ent in self.entities["hashtags"]:
								if self.ent is not None:
									if "text" in self.ent:
										self.hashtag = self.ent["text"]
										if self.hashtag is not None:
											self.hashtags.append(self.hashtag)

						if "user_mentions" in self.entities:
							for self.ent in self.entities["user_mentions"]:
								if self.ent is not None:
									if "screen_name" in self.ent:
										self.name = self.ent["screen_name"]
										if self.name is not None:
											self.mentions.append(self.name)
					if self.status.created_at < self.end_date:
						break
			self.mentions_d = {}
			self.hashtags_d = {}

			for self.item, self.count in Counter(self.mentions).most_common(10):
				self.mentions_d[self.item] = self.count
			for self.item, self.count in Counter(self.hashtags).most_common(10):
				self.hashtags_d[self.item] = self.count

			self.number_of_tweets=10
			self.tweets = self.auth_api.user_timeline(screen_name=self.target) 
			self.sentiment_d ={}
			self.tweets_for_csv = [tweet.text for tweet in self.tweets] # CSV file created  

			for self.j in self.tweets_for_csv:
				self.sentence = self.j
				self.exclude = set(string.punctuation)
				self.sentence = ''.join(ch for ch in self.sentence if ch not in self.exclude or ch == ":" or ch == "#")
				self.sentence = re.sub(r"https\S+", "", self.sentence)
				self.sentence = re.sub(' +', ' ', self.sentence)
				self.blob = TextBlob(self.sentence)

				if(self.blob.sentiment.polarity > 0):
					self.sentiment = "Positive"
				elif(self.blob.sentiment.polarity == 0):
					self.sentiment = "Neutral"
				else:
					self.sentiment = "Negative"

				self.sentiment_d[self.sentence] = self.sentiment 

			for i,j in zip(["sentiment","mentions","hashtags"],[self.sentiment_d,self.mentions_d,self.hashtags_d]):
				self.twitter_obj[i] = j

			return(self.twitter_obj)

	def get_email_info_from_sf(self, to_address):
		user_name = "foobar@dummy.com"
		pass_word = "thisdemoislit!!!123"
		security_token = "kMWcBvuvgYsPCCTi5idSDfSy"
		
		if to_address == None: 
			to_address = "pierreebayomidyar@gmail.com"
		
		self.sf = Salesforce(username=user_name, password=pass_word, security_token= security_token)
		salesforce_query_result = self.sf.query_all("SELECT CreatedDate, Subject, TextBody, ToAddress, FromAddress FROM EmailMessage Where ToAddress = '%s'" %to_address)
		salesforce_email_obj = {}
		num_of_emails = len(salesforce_query_result["records"])

		for i in range(0,num_of_emails):
			email_record = salesforce_query_result["records"][i]
			email_record_url = email_record["attributes"]["url"]
			email_url_list  = email_record_url.split('/')
			email_record_identification = email_url_list[len(email_url_list)-1]
			salesforce_email_obj[email_record_identification] = {}
			for names in ["CreatedDate","Subject","TextBody", "ToAddress", "FromAddress"]:
				salesforce_email_obj[email_record_identification][names] =  email_record[names]
		return(salesforce_email_obj)

	def create_json(self, csv_file, firstName):
		csv_rows = []
		with open(csv_file) as csvfile:
			reader = csv.DictReader(csvfile)
			title = reader.fieldnames
			for row in reader:
				fName =  row['firstName']
				fName =  fName.replace(" ","")
				if fName == firstName:
					csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
		return json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',',':'), ensure_ascii = False)		

