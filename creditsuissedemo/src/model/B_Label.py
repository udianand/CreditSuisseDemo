import CleanText

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
		self._category =  category
	
	@category_freq.setter
	def category_freq(frequency):
		self._category_freq = frequency

def labelAll(text):
	text = text.lower()
	full_word_list = CleanText.stripNonAlphaNum(text)
	wordlist = CleanText.removeStopwords(full_word_list, CleanText.stopwords)
	print(wordlist)
	dictionary = CleanText.wordListToFreqDict(wordlist)
	sorted_dict = CleanText.sortFreqDict(dictionary)
	#sorteddict_label = CleanText.labelDict(sorteddict)
	return sorted_dict

def countLabel(sorted_dict):
	label_freq_list = []
	count_uncatg = 0
	count_security = 0
	count_alternate = 0
	count_cash = 0
	for s in sorted_dict:
		category = s[0][0]
		if category == "uncategorized":
			count_uncatg += 1
		elif category == "security":
			count_security += 1
		elif category == "alternate":
			count_alternate += 1
		else:
			count_cash += 1
	label_freq_list.append(count_uncatg)
	label_freq_list.append(count_security)
	label_freq_list.append(count_alternate)
	label_freq_list.append(count_cash)
	return label_freq_list		


def groupLabel(sorted_dict, label_freq_list):
	g1 = CategoryGroup("uncategorized", label_freq_list[0])
	g2 = CategoryGroup("security", label_freq_list[1])
	g3 = CategoryGroup("alternate", label_freq_list[2])
	g4 = CategoryGroup("cash",label_freq_list[3])

	#g1.category_freq = label_freq_list[0]
	#g2.category_freq = label_freq_list[1]
	#g3.category_freq = label_freq_list[2]
	#g4.category_freq = label_freq_list[3]

	group_list = []
	group_list.append(g1)
	group_list.append(g2)
	group_list.append(g3)
	group_list.append(g4)

	group_list_sorted = sorted(group_list,key=lambda x:x.category_freq, reverse = True)
	
	if group_list_sorted[0].category == "uncategorized" and group_list_sorted[1].category_freq > 0:
		return group_list_sorted[1].category
	else:
		return group_list_sorted[0].category	

def labelTop(text):
	sorted_dict =  labelAll(text)
	group_label(sorted_dict)
	#label = topLabel(sorted_dict)
	#label =  topLabel(sorted_dict)
	#return sorted_dict[0][0][0]

def textLabel(text):
	sdict = labelAll(text)
	label_freq_list =  countLabel(sdict)
	text_label = groupLabel(sdict, label_freq_list)
	return text_label

#if __name__ == "__main__":
#	text = "Hello Pierre,\n\nThis is test email being sent from Salesforce test org.\nHope you are doing well. I wanted to take this opportunity to introduce our new product on impact investing.\n\n\nBest,\nFoo Bar\nCredit Suisse\n"
#	print(textLabel(text))

	


	
