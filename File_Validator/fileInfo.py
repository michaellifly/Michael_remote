import csv
import ConfigParser
import re

class FileInfo:

	def setFileInfo(self,fileName):
		
		#tempfileName = fileName
		#tempfileName = re.findall('[A-Za-z0-9_-\s]+.csv',tempfileName)
		#fileName = tempfileName[0]
		print fileName		
		
		# - specifically csv files------------------
		with open (fileName,"rb") as csvfile:
			file = csv.reader(csvfile, delimiter=',', quotechar='"')
			data = []
			for lines in file:
				data.append(lines)
		
		# For looping through the file to find the start of lines
		rowCount = 0
		breakValue = False
		for line in data:
			#print line
			rowCount = rowCount + 1
			columnCount= 0
			for each in line:	
				columnCount = columnCount + 1
				#print each
				if re.match('[0-9]+',each): 
					#print each
					leftOffset = columnCount -1
					topOffset = rowCount - 2
					breakValue = True
					break
			if breakValue:
				break
		datacount =  len(data) - topOffset
		self.writeToConfig(topOffset,leftOffset)
	
	def writeToConfig(self,topOffset,leftOffset):

		config = ConfigParser.RawConfigParser()
		
		config.add_section('Database')
		config.set('Database', 'database.host','localhost')
		config.set('Database', 'database.user','root')
		config.set('Database', 'database.password','root')
		config.set('Database', 'database.dbname','file_validator')
		
		config.add_section('Csv')
		config.set('Csv', 'csv.topOffset', topOffset)
		config.set('Csv', 'csv.leftOffset', leftOffset)

		with open('config.ini', 'wb') as configfile:
			config.write(configfile)
