class AssetsInfo():
	""" Stores the assets information for an individual"""
	def __init__(self):
		self._aum = ""
		self._level = ""
		self._networth = ""
		keys_aumInfo = ['cash','securites','other']
		self._aumInfo = dict.fromkeys(keys_aumInfo, None)

	@property
	def aum(self):
		return self._aum

	@property
	def level(self):
		return self._level
	
	@property
	def networth(self):
		return self._networth
	
	@property
	def cash(self):
		return self._aumInfo['cash']

	@property
	def securites(self):
		return self._aumInfo['securites']
	
	@property
	def other(self):
		return self._aumInfo['other']

	@aum.setter
	def aum(self, aum):
		self._aum = aum

	@level.setter
	def level(self, level):
		self_level =  level

	@networth.setter
	def networth(self, networth):
		self_networth =  networth

	@cash.setter
	def cash(self, cash):
		self._aumInfo['cash'] =  cash

	@securites.setter
	def securites(self, securites):
		self._aumInfo['securites'] = securites

	@other.setter
	def other(self, other):
		self._aumInfo['other'] = other
						
		
		