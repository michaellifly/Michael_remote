import io
import sys
import csv
from configReader import ConfigReader

class FileReader:

	def __init__(self,fileName):
		configReader = ConfigReader()
		config = configReader.readConfig()
		
		#reading the parameters from the config file
		#file = config.get('Csv', 'csv.file')
		file = fileName
		self.topOffset = config.get('Csv','csv.topOffset')
		self.leftOffset = config.get('Csv','csv.leftOffset')
		
		#opening and reading from the file
		with open(file, "rb") as csvfile:
			
			try:
				# for removing the byte order mark (BOM ), read the file, decoded the file , and encodeg again without the BOM
				file = csv.reader(f.read().decode('utf-8-sig').encode('utf-8').splitlines(), delimiter='\t', quotechar='"')
			except:
				file = csv.reader(csvfile, delimiter=',', quotechar='"')
			
			self.data = []
			for lines in file:
				self.data.append(lines) #storing each lines of file in array
				
	def readHeader(self):
		
		# selecting the first line as header from the data array
		columns = self.data[int(self.topOffset)]	 		
		
		# for removing the leftOffset(blank cells) from the header
		for i in range (int(self.leftOffset)):
			columns.pop(i)
		
		#return the header as array	
		return columns
	
	def readRows(self) :
		
		#for selecting only the data excluding the topOffset and header from data array 
		startRow = int(self.topOffset)+ 1
		endRow = len(self.data)		
		rows = self.data[startRow:endRow]
	
	# for removing the leftOffset(blank cells) from each line
		for eachRow in rows:
			for i in range (int(self.leftOffset)):
				eachRow.pop(i)

		#return the rows of data as array
		return rows
	
		