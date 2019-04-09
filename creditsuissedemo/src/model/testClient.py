import json
from elasticsearch import Elasticsearch
import sys


#es.index(index='user_profile', doc_type = 'individual', id = i, body = user_profile_json)
#res = es.search(index="user_profile", doc_type="individual", body={"query": {"match": {"message": keyword}}}, size=1000, from_=0)

es = Elasticsearch()
keyword_t = "Education"
keyword_e = "Sustainable"
res = es.search(index="user_profile", doc_type="individual", body={"query": {"match": {"EmailInfo._emailInfoList._textBody": keyword_e}}}, size=10, from_=0)
#res = es.search(index="tweetstream", doc_type="tweet", body={"query": {"match": {"message": keyword}}}, size=1000, from_=0)
print(res)