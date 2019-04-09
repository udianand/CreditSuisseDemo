import random
import json
import jsonpickle

from Data_Sources import Data_Sources
from IndividualInfo import IndividualInfo
from ContactInfo import ContactInfo
from AssetsInfo import AssetsInfo
from TwitterInfo import TwitterInfo
from EmailInfo import EmailInfo

name_to_email_id = {
"Pierre": "pierreebayomidyar@gmail.com",
"Bill": "billygatessoft@gmail.com"
}


def init_data_sources():
    data_src = Data_Sources()
    return data_src
# Individual's Aggregated json profile
#/home/UditAdmin/creditsuissedemo/src/model/Documents

def convert_csv_to_json(data_src, firstName):
    csv_file = "/home/UditAdmin/creditsuissedemo/src/model/Documents/clientlist.csv"
    csv_to_json = data_src.create_json(csv_file, firstName)
    csv_to_json_dict = json.loads(csv_to_json)
    # removing the leading and trailing '{}' and converting to a dictionary
    csv_to_json_dict = csv_to_json_dict[0]
    return csv_to_json_dict

# Map firstname to email id
def map_email_id(first_name):
    return name_to_email_id.get(first_name) 

# Map Individual PII Info
def map_individual_pii_info(csv_to_json_dict):
    individual_pii_info = IndividualInfo()
    individual_pii_info.firstName = csv_to_json_dict['firstName']
    individual_pii_info.lastName = csv_to_json_dict['lastName']
    individual_pii_info.gender = "Male"  # TODO: Add gender field to csv file
    individual_pii_info.dateOfBirth = csv_to_json_dict['dateOfBirth']
    individual_pii_info.isDeceased = csv_to_json_dict['isDeceased']
    individual_pii_info.citizenship = csv_to_json_dict['citizenship']
    individual_pii_info.employerName = csv_to_json_dict['employerName']
    # TODO: Add position title field to csv file
    individual_pii_info.positionTitle = "Chairman"
    # TODO: Add nature of business field to csv file
    individual_pii_info.natureOfBusiness = "Internet"
    # TODO: Add employment status to csv file
    individual_pii_info.employmentStatus = "Passive"

    return individual_pii_info

# Map Individual Assets Info


def map_individual_assets_info(csv_to_json_dict):
    individual_assets_info = AssetsInfo()
    individual_assets_info.aum = csv_to_json_dict['aum']
    individual_assets_info.cash = csv_to_json_dict['cash']
    individual_assets_info.networth = csv_to_json_dict['networth']
    individual_assets_info.securites = csv_to_json_dict['securities']
    individual_assets_info.other = csv_to_json_dict['other']
    individual_assets_info.level = csv_to_json_dict['level']

    return individual_assets_info

# Map Individual Contact Info


def map_individual_contact_info(csv_to_json_dict):
    individual_contact_info = ContactInfo()
    individual_contact_info.electronicAddress = csv_to_json_dict['electronicAddress']
    # TODO: Add electronic Address Type to csv
    individual_contact_info.electronicAddressType = "Home"
    # TODO: Add is Preferred field to csv
    individual_contact_info.isPreferred = "True"
    individual_contact_info.phoneNumber = csv_to_json_dict['phone']
    individual_contact_info.phoneType = "Work"  # TODO: Add phone type field to csv
    individual_contact_info.city = csv_to_json_dict['city']
    individual_contact_info.state = csv_to_json_dict['state']
    individual_contact_info.country = csv_to_json_dict['country']

    return individual_contact_info

# Map Individual Twitter Info


def map_individual_twitter_info(data_src, twitter_user_name):
    individual_twitter_info = TwitterInfo()
    user_twitter_obj = data_src.get_twitter_info([twitter_user_name])

    sentiment_dict = user_twitter_obj['sentiment']
    map_twitter_sentiment(individual_twitter_info, sentiment_dict)

    mentions_dict = user_twitter_obj['mentions']
    map_twitter_mentions(individual_twitter_info, mentions_dict)

    hashtags_dict = user_twitter_obj['hashtags']
    map_twitter_hashtags(individual_twitter_info, hashtags_dict)

    return individual_twitter_info


def map_twitter_sentiment(individual_twitter_info, sentiment_dict):
    for tweet, sentiment in sentiment_dict.items():
        individual_twitter_info.append_to_sentiment_list(tweet, sentiment)


def map_twitter_mentions(individual_twitter_info, mentions_dict):
    for mentions, count in mentions_dict.items():
        individual_twitter_info.append_to_mention_list(mentions, count)


def map_twitter_hashtags(individual_twitter_info, hashtags_dict):
    for hashtag, count in hashtags_dict.items():
        individual_twitter_info.append_to_hashtag_list(hashtag, count)


def map_individual_email_info(data_src, first_name):
    individual_email_info = EmailInfo()
    usr_email_obj = data_src.get_email_info_from_sf(map_email_id(first_name))

    for sf_email_id in usr_email_obj.keys():
        map_email_contents(individual_email_info, sf_email_id, usr_email_obj, first_name)

    return individual_email_info


def map_email_contents(individual_email_info, sf_email_id, usr_email_obj, first_name):
    CREATED_DATE = 'CreatedDate'
    SUBJECT = 'Subject'
    TEXTBODY = 'TextBody'
    TOADDRESS = 'ToAddress'
    FROMADDRESS = 'FromAddress'

    email_contents = usr_email_obj[sf_email_id]
    email_salesforce_id = sf_email_id
    email_created_date = email_contents[CREATED_DATE]
    email_subject = email_contents[SUBJECT]
    email_text_body = email_contents[TEXTBODY]
    email_to_address = email_contents[TOADDRESS]
    email_from_address = email_contents[FROMADDRESS]

    individual_email_info.append_to_email_list(email_salesforce_id, email_created_date, email_subject, email_text_body,
                                               email_to_address, email_from_address, first_name)


def add_to_party_profile(partyObj, tag, value):
    partyObj[tag] = value
    # return partyObj


def convert_party_profile_to_json(partyObj):
    jsonObj = jsonpickle.encode(partyObj)
    return jsonObj


def map_all_individual_information(first_name, twitter_user_name):
    INDIVIDUAL_INFO = "IndividualInfo"
    CONTACT_INFO = "ContactInfo"
    TWITTER_INFO = "TwitterInfo"
    EMAIL_INFO = "EmailInfo"
    ASSETS_INFO = "AssetsInfo"

    data_src = init_data_sources()
    csv_to_json_dict = convert_csv_to_json(data_src, first_name)
    party = {}

    individual_pii_info = map_individual_pii_info(csv_to_json_dict)
    add_to_party_profile(party, INDIVIDUAL_INFO, individual_pii_info)

    individual_contact_info = map_individual_contact_info(csv_to_json_dict)
    add_to_party_profile(party, CONTACT_INFO, individual_contact_info)

    individual_assets_info = map_individual_assets_info(csv_to_json_dict)
    add_to_party_profile(party, ASSETS_INFO, individual_assets_info)

    individual_twitter_info = map_individual_twitter_info(data_src, twitter_user_name)
    add_to_party_profile(party, TWITTER_INFO, individual_twitter_info)

    individual_email_info = map_individual_email_info(data_src, first_name)
    add_to_party_profile(party, EMAIL_INFO, individual_email_info)

    party_profile = convert_party_profile_to_json(party)
    return party_profile

