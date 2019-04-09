import CleanText
import collections
import re

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from itertools import tee

def remove_punctuation(text):
    punctuation2 = '-&'+'®©™€â´‚³©¥ã¼•ž®è±äüöž!@#Â“§$%^*()î_+€$=¿{”}[]:«;"»\â¢|<>,.?/~`0123456789'
    for sign in punctuation2:
        text = text.replace(sign, " ")
    return text

def count_phrases(words, cnt):
	#phrases = ['impact investing']
	phrases = CleanText.categories
	print(type(phrases))
	fw1, fw2 = tee(findWords(words))  
	next(fw2)
	for w1,w2 in zip(fw1, fw2):
		phrase = ' '.join([w1, w2])
		if phrase in phrases:
			cnt[phrase] += 1
			#print(phrase)		
	return dict(cnt)	

def findWords(text):
	words = re.findall('\w+', text)
	yield from words

if __name__ == "__main__":
	text = "Hello Pierre,\n\nThis is email being sent from Salesforce test org.\nHope you are doing well. I wanted to take this opportunity to introduce our new product on impact investing.\n\n\nBest,\nFoo Bar\nCredit Suisse\n"
	first_name = "Pierre"
	isPresent = text.lower().find(first_name.lower())
	if isPresent != -1: print("true")
	else: 
		print("false")   


	'''text = text.lower()
	text = remove_punctuation(text)
	#print(text)
	s = ""
	#full_word_list = CleanText.stripNonAlphaNum(text)
	#stop_words = set(stopwords.words('english'))
	
	list_stopwords = stopwords.words('english')
	list_stopwords.extend(CleanText.stopwords)
	stop_words = set(list_stopwords)
	words_token =  word_tokenize(text)

	for w in words_token:
		if w not in stop_words:
			s += " " + w
	cnt = collections.Counter(findWords(s))
	phrase_count = count_phrases(s, cnt)
	for phrase in phrase_count:
		print(phrase + " => "+ str(phrase_count[phrase]))		

	#print(s)'''		


	


	
