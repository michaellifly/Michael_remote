import MySQLdb
from dbConnection import DbConnection

class TableMetadata:
	
	
	def __init__(self):
		self.dbConnection = DbConnection()
		self.conn = self.dbConnection.dbConnect()
	

	def readTableHeader (self,clientName,rawTableName):

		cursor = self.conn.cursor()
		sqlQuery = "select raw_file_columns from file_validator.metadata where client_name ='%s' and raw_table_name='%s' and raw_file_columns <> 'null';" %(clientName,rawTableName)
		cursor.execute(sqlQuery)
		dbColumns = cursor.fetchall()

		rawColumns =[]
		for eachColumn in dbColumns:
			eachColumn  = [x.strip(',') for x in eachColumn]
			rawColumns.append(eachColumn)	
		#self.conn.close()
		
		columns = []
		for i in range (len(rawColumns)):
			 columns.append(rawColumns[i][0])
	
		return columns
	
	def readMetadata (self,clientName,rawTableName) :
		
		cursor = self.conn.cursor()
		sqlQuery = "select data_type from file_validator.metadata where client_name='%s'and raw_table_name ='%s' and raw_file_columns <> 'null';" %(clientName,rawTableName)
		cursor.execute(sqlQuery)
		columns = cursor.fetchall()
		
		rawColumns =[]
		for eachColumn in columns:
			eachColumn  = [x.strip(',') for x in eachColumn]
			rawColumns.append(eachColumn)	
		self.conn.close()
		
		dataType = []
		for i in range (len(rawColumns)):
			 dataType.append(rawColumns[i][0])
	
		return dataType
	


	