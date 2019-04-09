class ContactInfo():
	""" Stores the contact information for an individual"""
	def __init__(self):
		keys_emailInfo = ['electronicAddress', 'electronicAddressType', 'isPreferred']
		keys_phoneInfo = ['phoneNumber','phoneType']
		keys_addressInfo = ['city','state', 'country']
		self._emailInfo = dict.fromkeys(keys_emailInfo, None)
		self._addressInfo =  dict.fromkeys(keys_addressInfo, None)
		self._phoneInfo =  dict.fromkeys(keys_phoneInfo, None)

	""" Email Info """	
	@property
	def electronicAddress(self):
		return self._emailInfo['electronicAddress']

	@property
	def electronicAddressType(self):
		return self._emailInfo['electronicAddressType']

	@property
	def isPreferred(self):
		return self._emailInfo['isPreferred']
	
	@electronicAddress.setter
	def electronicAddress(self, electronicAddress):
		self._emailInfo['electronicAddress'] = electronicAddress

	@electronicAddressType.setter
	def electronicAddressType(self, electronicAddressType):
		self._emailInfo['electronicAddressType'] =  electronicAddressType

	@isPreferred.setter
	def isPreferred(self, isPreferred):
		self._emailInfo['isPreferred'] =  isPreferred

	""" Phone Info """
	@property
	def phoneNumber(self):
		return self._phoneInfo['phoneNumber']

	@property
	def phoneType(self):
		return self._phoneInfo['phoneType']

	@phoneNumber.setter
	def phoneNumber(self, phoneNumber):
		self._phoneInfo['phoneNumber'] =  phoneNumber

	@phoneType.setter
	def phoneType(self, phoneType):
		self._phoneInfo['phoneType'] =  phoneType

	
	""" AddressInfo """			
	@property
	def city(self):
		return self._addressInfo['city']

	@property
	def state(self):
		return self._addressInfo['state']

	@property
	def country(self):
		return self._addressInfo['country']

	@city.setter
	def city(self, city):
		self._addressInfo['city'] =  city

	@state.setter
	def state(self, state):
		self._addressInfo['state'] =  state

	@country.setter
	def country(self, country):
		self._addressInfo['country'] = country			
			
	