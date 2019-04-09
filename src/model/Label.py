import CleanText
import collections
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import tee


class CategoryGroup():

    def __init__(self, category, frequency):
        self._category = category
        self._category_freq = frequency

    @property
    def category(self):
        return self._category

    @property
    def category_freq(self):
        return self._category_freq

    @category.setter
    def category(category):
        self._category = category

    @category_freq.setter
    def category_freq(frequency):
        self._category_freq = frequency


class KTFClass():

    def __init__(self, keyword, keyword_frequency, category):
        self._keyword = keyword
        self._keyword_frequency = keyword_frequency
        self._category = category

    @property
    def category(self):
        return self._category

    @property
    def keyword_frequency(self):
        return self._keyword_frequency

    @property
    def keyword(self):
        return self._keyword

    @category.setter
    def category(category):
        self._category = category

    @keyword_frequency.setter
    def category_freq(frequency):
        self._keyword_frequency = frequency

    @keyword.setter
    def keyword(key):
        self._keyword = key


'''def countKeywordFrequency(words, cnt):
	fw1, fw2 = tee(findWords(words))  
	next(fw2)
	phrases = CleanText.categories
	for w1,w2 in zip(fw1, fw2):
		phrase = ' '.join([w1, w2])
		if phrase in phrases:
			cnt[phrase] += 1
	print(dict(cnt))				
	return dict(cnt)'''


def assignCategories(dict_keyword_frequency):
    KTFList = []
    for keyword in dict_keyword_frequency:
        frequency = dict_keyword_frequency[keyword]
        category = CleanText.keyCategory(keyword)
        KTFObj = KTFClass(keyword, frequency, category)
        KTFList.append(KTFObj)

    # for KTFObj in KTFList:
    #	print(KTFObj.category)

    return KTFList


def mostFreqCategory(KTFList):
    num_alt = 0
    num_cash = 0
    num_security = 0
    num_uncatg = 0

    group_catg_list = []

    for KTFObj in KTFList:
        if(KTFObj.category == "alternate"):
            num_alt += 1
        if(KTFObj.category == "security"):
            num_security += 1
        if(KTFObj.category == "cash"):
            num_cash += 1
        else:
            num_uncatg += 1

    # = CategoryGroup("uncategorized", num_uncatg)
    g_security = CategoryGroup("security", num_security)
    g_alternate = CategoryGroup("alternate", num_alt)
    g_cash = CategoryGroup("cash", num_cash)

    group_catg_list.append(g_security)
    group_catg_list.append(g_alternate)
    group_catg_list.append(g_cash)

    groupList_sorted = sorted(
        group_catg_list, key=lambda x: x.category_freq, reverse=True)
    frequent_group = groupList_sorted[0]
    # print(frequent_group.category_freq)
    if (frequent_group.category_freq == 0):
        return "uncategorized"
    else:
        return groupList_sorted[0].category


def count_phrases_live_tweet(words, cnt):
    phrases = CleanText.categories
    fw1, fw2 = tee(CleanText.findWords(words))
    try:
        next(fw2)
        for w1, w2 in zip(fw1, fw2):
            phrase = ' '.join([w1, w2])
            if phrase in phrases:
                cnt[phrase] += 1
                # print(phrase)
        return dict(cnt)
    except StopIteration:
        print("Stop Iteration Exception")    

def count_phrases(words, cnt):
    phrases = CleanText.categories
    fw1, fw2 = tee(CleanText.findWords(words))
    next(fw2)
    for w1, w2 in zip(fw1, fw2):
        phrase = ' '.join([w1, w2])
        if phrase in phrases:
            cnt[phrase] += 1
            # print(phrase)
    return dict(cnt)


def generateKTFList(text):
    text = text.lower()
    text = CleanText.remove_punctuation(text)
    s = ""
    list_stopwords = stopwords.words('english')
    list_stopwords.extend(CleanText.stopwords)
    stop_words = set(list_stopwords)
    words_token = word_tokenize(text)
    for w in words_token:
        if w not in stop_words:
            s += " " + w
    cnt = collections.Counter(CleanText.findWords(s))

    keyword_cnt = count_phrases(s, cnt)
    KTFList = assignCategories(keyword_cnt)

    return KTFList


def generateLabel(text):
    text = text.lower()
    text = CleanText.remove_punctuation(text)
    s = ""
    list_stopwords = stopwords.words('english')
    list_stopwords.extend(CleanText.stopwords)
    stop_words = set(list_stopwords)
    words_token = word_tokenize(text)
    for w in words_token:
        if w not in stop_words:
            s += " " + w
    cnt = collections.Counter(CleanText.findWords(s))

    keyword_cnt = count_phrases(s, cnt)
    KTFList = assignCategories(keyword_cnt)
    label = mostFreqCategory(KTFList)
    return label


def generateLabel_live_tweet(text):
    text = text.lower()
    text = CleanText.remove_punctuation(text)
    s = ""
    list_stopwords = stopwords.words('english')
    list_stopwords.extend(CleanText.stopwords)
    stop_words = set(list_stopwords)
    words_token = word_tokenize(text)
    for w in words_token:
        if w not in stop_words:
            s += " " + w
    cnt = collections.Counter(CleanText.findWords(s))

    keyword_cnt = count_phrases_live_tweet(s, cnt)
    
    if keyword_cnt is None:
        return "uncategorized"
    else:    
        KTFList = assignCategories(keyword_cnt)
        label = mostFreqCategory(KTFList)
        return label

'''if __name__ == "__main__":
	text = "Hello Pierre,\n\nThis is email is sent from Salesforce test org.\nHope you are doing well. I wanted to take this opportunity to introduce our new product on impact investing.\n\n\nBest,\nFoo Bar\nCredit Suisse\n"
	#text = "this this this"
	print(generateLabel(text))'''
