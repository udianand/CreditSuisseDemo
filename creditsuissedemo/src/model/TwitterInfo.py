import Label

class Sentiment():
	def __init__(self):
		self._tweet = ""
		self._sentiment = ""
		self.label = ""

	@property
	def tweet(self):
		return self._tweet

	@property
	def sentiment(self):
		return self._sentiment

	@property
	def label(self):
		return self._label
		
	@tweet.setter
	def tweet(self, tweet):
		self._tweet =  tweet

	@sentiment.setter
	def sentiment(self, sentiment):
		self._sentiment =  sentiment

	@label.setter
	def label(self, label):
		self._label = label	

class HashTags():

	def __init__(self):
		self._hashtag = ""
		self._count = 0

	@property
	def hashtag(self):
		return self._hashtag

	@property
	def count(self):
		return self._count
		
	@hashtag.setter
	def hashtag(self, hashtag):
		self._hashtag =  hashtag	

	@count.setter
	def count(self, count):
		self._count = count	

class Mentions():

	def __init__(self):
		self._entity = ""
		self._num_mentions = 0

	@property
	def entity(self):
		return self._entity

	@property
	def num_mentions(self):
		return self._num_mentions
		
	@entity.setter
	def entity(self,entity):
		self._entity =  entity

	@num_mentions.setter
	def num_mentions(self, num_mentions):
		self._num_mentions = num_mentions



class TwitterInfo():
	""" Stores the twitter info of an individual """

	def __init__(self):
		self._mentionsList = []
		self._hashtagsList = []
		self._sentimentList = []

	def append_to_mention_list(self, entity, num_mentions):
		m1 =  Mentions()
		m1.entity = entity
		m1.num_mentions =  num_mentions
		self._mentionsList.append(m1)	

	def get_mention_list(self):
		return self._mentionsList

	def append_to_hashtag_list(self, hashtag, count):
		h1 = HashTags()
		h1.hashtag = hashtag
		h1.count =  count
		self._hashtagsList.append(h1)

	def get_hashtag_list(self):
		return self._hashtagsList

	def append_to_sentiment_list(self, tweet, sentiment):
		s1 =  Sentiment()
		s1.tweet = tweet
		s1.sentiment =  sentiment
		s1.label = Label.generateLabel(tweet)
		self._sentimentList.append(s1)

	def get_sentiment_list(self):
		return self._sentimentList				


#class SocialInfo(TwitterInfo):

#	def __init__(self):
#		TwitterInfo.__init__(self)
		

