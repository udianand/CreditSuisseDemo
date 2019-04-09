import time
import requests
from elasticsearch import Elasticsearch



def check_elastic_search_connection():
    res = requests.get("http://localhost:9200")
    print('Elastic Search Server Status')
    print('--------Start---------')
    print('\n')
    print(res.content)
    print('\n')
    print('--------End-------')


def init_elastic_search():
    es = Elasticsearch([{'host': '192.168.231.142', 'port': 9200}])
    return es

if __name__ == "__main__":

    check_elastic_search_connection()
    es = init_elastic_search()
    # query will return email text body and client present information
    # the first result will be the one you are looking for :)... in prelim testing
    res = es.search(index="user_profile", doc_type="individual", body={"_source":{
    "includes" : ["EmailInfo._emailInfoList._textBody",
    "EmailInfo._emailInfoList._clientPresent"
    ]
  },
    "query": {
        "bool" : {
            "must" : {
                "query_string" : {
                    "query" : "Pierre" # what you want to search
                }
            },
            "filter" : {
                "bool" : {
              "should" : [
                 { "term" : {"_id" : 0}},  # repalce with id you want to search
                 { "term" : {"EmailInfo._emailInfoList._clientPresent" : "Yes"}} 
              ]
              
           }
               
            }
        }
    }})    
    print(res)





