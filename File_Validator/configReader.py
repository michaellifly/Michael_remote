import ConfigParser

class ConfigReader:
	config = None
	
	def readConfig (self) :
		global config
		config = ConfigParser.RawConfigParser()
		config.read('config.ini')
		return config
		
