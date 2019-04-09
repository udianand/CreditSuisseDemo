import time
import requests
from elasticsearch import Elasticsearch
import KTFInfo
import Mapper


def check_elastic_search_connection():
    res = requests.get("http://localhost:9200")
    print('Elastic Search Server Status')
    print('--------Start---------')
    print('\n')
    print(res.content)
    print('\n')
    print('--------End-------')


def init_elastic_search():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    return es


class Main():
    def __init__(self):
        pass

    def get_individual_profile_in_json(self, individual_first_name, individual_twitter_name):
        user_profile_json = Mapper.map_all_individual_information(
            individual_first_name, individual_twitter_name)
        return user_profile_json

    def get_ktf_info(self, user_id):
    	res = es.get(index='user_profile', doc_type='individual', id=user_id)
    	user_ktf_json = KTFInfo.generate_user_ktf(res['_source'])
    	return user_ktf_json    


if __name__ == "__main__":

    check_elastic_search_connection()
    es = init_elastic_search()

    fName = ['Pierre', 'Bill']
    twitter_names = ['pierre', 'BillGates']

    for i in range(len(fName)):
        individual_first_name = fName[i]
        individual_twitter_name = twitter_names[i]
        m1 = Main()
        
        user_profile_json = m1.get_individual_profile_in_json(
            individual_first_name, individual_twitter_name)
        es.index(index='user_profile', doc_type='individual',
                 id=i, body=user_profile_json)

        user_ktf_json = m1.get_ktf_info(i)
        es.index(index = 'user_ktf_info', doc_type= 'individual',
        	id = i, body = user_ktf_json)

        print("Profile Inserted: " + individual_first_name )
        print('\n')
        #print("User Profile: ")
        #print(user_profile_json)
        time.sleep(60)  # sleep for 60 seconds
        
