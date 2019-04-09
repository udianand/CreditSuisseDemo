import jsonpickle

class IndividualInfo():
	""" IndividualInfo class to represent an individual's information """

	def __init__(self):
		keys_nameInfo = ['firstName', 'lastName']
		keys_employmentInfo = ['employerName','positionTitle','natureOfBusiness','employmentStatus']

		self._nameInfo = dict.fromkeys(keys_nameInfo, None)
		self._employmentInfo =  dict.fromkeys(keys_employmentInfo, None)
		self._gender = ""
		self._dateOfBirth = ""
		self._isDeceased = ""
		self._citizenship = ""

	
	@property
	def firstName(self):
		return self._nameInfo['firstName']

	@firstName.setter
	def firstName(self, firstName):
		self._nameInfo['firstName'] =  firstName	
	
	@property
	def lastName(self):
		return self._nameInfo['lastName']

	@lastName.setter
	def lastName(self, lastName):
		self._nameInfo['lastName'] =  lastName	
		
	@property
	def gender(self):
		return self._gender

	@gender.setter
	def gender(self, gender):
		self._gender =  gender

	@property
	def dateOfBirth(self):
		return self._dateOfBirth

	@dateOfBirth.setter
	def dateOfBirth(self, dateOfBirth):
		self._dateOfBirth = dateOfBirth	
	
	@property
	def isDeceased(self):
		return self._isDeceased
	
	@isDeceased.setter
	def isDeceased(self, isDeceased):
		self._isDeceased = isDeceased

	@property
	def citizenship(self):
		return self._citizenship

	@citizenship.setter
	def citizenship(self, citizenship):
		self._citizenship =  citizenship
		
	@property
	def employerName(self):
		return self._employmentInfo['employerName']

	@employerName.setter
	def employerName(self, employerName):
		self._employmentInfo['employerName'] =  employerName

	@property
	def positionTitle(self):
		return self._employmentInfo['positionTitle']

	@positionTitle.setter
	def positionTitle(self, positionTitle):
		self._employmentInfo['positionTitle'] =  positionTitle		

	@property
	def natureOfBusiness(self):
		return self._employmentInfo['natureOfBusiness']

	@natureOfBusiness.setter
	def natureOfBusiness(self, natureOfBusiness):
		self._employmentInfo['natureOfBusiness'] =  natureOfBusiness	

	@property
	def employmentStatus(self):
		return self._employmentInfo['employmentStatus']

	@employmentStatus.setter
	def employmentStatus(self, employmentStatus):
		self._employmentInfo['employmentStatus'] = employmentStatus		







			