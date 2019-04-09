import Label
import json
import jsonpickle

class KTFInfoClass():

	def __init__(self):
		self._KTFInfoList = []  

	def extend_ktf_list(self, KTFList):
		self._KTFInfoList.extend(KTFList)

	def append_ktf_list(self, KTFObj):
		self._KTFInfoList.append(KTFObj)

	@property
	def KTFInfoList(self):
		return self._KTFInfoList

def generate_user_ktf_live_tweet(live_tweet):
	KTFInfoObj =  KTFInfoClass()
	live_tweet_ktf_list = Label.generateKTFList(live_tweet)
	
	for KtfObj in live_tweet_ktf_list:
		if KtfObj.category != "uncategorized":
			KTFInfoObj.append_ktf_list(KtfObj)
	
	user_live_tweet_ktf_json = jsonpickle.encode(KTFInfoObj)
	return user_live_tweet_ktf_json		

def generate_user_ktf(es_user_profile):
	KTFInfoObj =  KTFInfoClass()

	email_list = es_user_profile['EmailInfo']['_emailInfoList']
	for email in email_list:
		email_text_body = email['_textBody']
		email_ktf_list = Label.generateKTFList(email_text_body)

		for KtfObj in email_ktf_list: 
			if KtfObj.category != "uncategorized":
				KTFInfoObj.append_ktf_list(KtfObj)

	tweet_info_list = es_user_profile['TwitterInfo']['_sentimentList']
	for tweet_info in tweet_info_list:
		tweet_text = tweet_info['_tweet']	
		tweet_ktf_list = Label.generateKTFList(tweet_text)
		for KTFObj in tweet_ktf_list:
			if KTFObj.category != "uncategorized":
				KTFInfoObj.append_ktf_list(KTFObj)
    
	user_ktf_json = jsonpickle.encode(KTFInfoObj)
	return user_ktf_json						