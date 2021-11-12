from datetime import datetime
from configReader import ConfigReader

class Validation :

	def validateHeaders(self,dbColumns,fileColumns):
		self.dbColumns = dbColumns
		self.fileColumns = fileColumns
		
		for i in range (len(self.dbColumns)):
			if self.fileColumns[i] <> self.dbColumns[i]:
				#point the location of the header error in the excel sheet
				self.pointError(fileColumns[i],i,0) 
				return False
			#else:
			#	print self.fileColumns[i] +"=" + self.dbColumns[i];
		return True

	
	def validateRow(self,dataType,eachRow,rowNum):
		self.dataType = dataType
		self.eachRow = eachRow	
		self.rowNum = rowNum
		
		for i in range (len(self.dataType)):
			
			value = self.eachRow[i]
			
			if self.dataType[i] == "int": # if data type for this data is defined as int
				if self.isValueInt(value) is False:
					#for identifying error
					self.pointError(value,i,self.rowNum)  
					return False
			
			elif self.dataType[i] == "datetime": # if data type for this data is defined as datetime
				if self.isValueDatetime(value) is False:
					#for identifying error
					self.pointError(value,i,self.rowNum)
					return False
								
			else : # assumed data type for this data is defined as varchar
				if self.isValueVarchar(value) is False:
					#for identifying error
					self.pointError(value,i,self.rowNum)
					return False
	
	
	def isValueInt(self,value):
		try: # return true if value is sucessfully parsed as integer		
			int(value)
			return True
		except :
			return False	

			
	def isValueDatetime(self,value):
		if value <> "" : #check data type only if value is not null
			try: 	# return true if value is sucessfully parsed as datetime		
				datetime.strptime(value, "%Y/%m/%d %H:%M:%S")
				#TODO add multiple timedate formats
				return True
			except :
				return False	
		else:
			return True #returns true since value is null

			
	def isValueVarchar(self,value):
		try:	# return true if value is sucessfully parsed as string (varchar)	
			str(value)
			return True
		except :
			return False
	
	
	def pointError(self,value,i,rowNum):
		
		configReader = ConfigReader()
		config = configReader.readConfig()
		
		#Reading parameters from the config file
		topOffset = config.get('Csv','csv.topOffset')
		leftOffset = config.get('Csv','csv.leftOffset')
		
		print "Column number : %d" %(i+1+int(leftOffset))
		print "Row number : %d" %(rowNum+1+int(topOffset))
		print "value: %s" % (value)
		
		
