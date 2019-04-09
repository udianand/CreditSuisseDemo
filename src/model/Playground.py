import Label
import json
import jsonpickle

from elasticsearch import Elasticsearch
from KTFInfo import KTFInfoClass


def init_elastic_search():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return es


if __name__ == "__main__":
    es = init_elastic_search()
    KTFInfoObj =  KTFInfoClass()
    res = es.get(index='user_profile', doc_type='individual', id=1)
    
    email_list = res['_source']['EmailInfo']['_emailInfoList']
    for email in email_list:
    	email_text_body = email['_textBody']
    	email_ktf_list = Label.generateKTFList(email_text_body)
    	for KtfObj in email_ktf_list: 
    		if KtfObj.category != "uncategorized":
    			KTFInfoObj.append_ktf_list(KtfObj)

    tweet_info_list = res['_source']['TwitterInfo']['_sentimentList']
    for tweet_info in tweet_info_list:
    	tweet_text = tweet_info['_tweet']	
    	tweet_ktf_list = Label.generateKTFList(tweet_text)
    	for KTFObj in tweet_ktf_list:
    		if KTFObj.category != "uncategorized":
    			KTFInfoObj.append_ktf_list(KTFObj)



    jsonObj = jsonpickle.encode(KTFInfoObj)
    print(jsonObj)
  