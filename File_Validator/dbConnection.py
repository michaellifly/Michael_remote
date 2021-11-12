import MySQLdb
from configReader import ConfigReader

class DbConnection:
	

	def dbConnect(self):
		configReader = ConfigReader()
		config = configReader.readConfig()
		
		host = config.get('Database', "database.host")
		username = config.get('Database', "database.user")
		password = config.get('Database', "database.password")
		dbname = config.get('Database', "database.dbname")
		
		conn = MySQLdb.connect(host,username,password,dbname)
		return conn
