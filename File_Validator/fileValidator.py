import sys
from fileReader import FileReader
from tableMetadata import TableMetadata
from validation import Validation
from sortFiletype import SortFileType
from fileInfo import FileInfo

class FileValidator:
	rowNum = 0

	def __init__(self):
		#importing the client name and raw table name passed as parameters
		clientName = sys.argv[1]
		fileName = sys.argv[2]
		
		#if needed to give filepath and validate a file not in the same folder
		#fileNamewithPath = sys.argv[2]
		#tempfileName = re.findall('[A-Za-z0-9_-\s]+.csv',fileNamewithPath)
		#fileName = tempfileName[0]
		
		fileInfo = FileInfo()
		fileInfo.setFileInfo(fileName)
		sortFileType = SortFileType()
		fileType,rawTableName = sortFileType.getFileType(clientName,fileName)
		#print fileType
		#print rawTableName
		
		fileReader = FileReader(fileName)
		tableMetadata = TableMetadata()
		validation = Validation()
		error = None
		
		fileColumns = fileReader.readHeader()
		dbColumns = tableMetadata.readTableHeader(clientName,rawTableName)
		
		if validation.validateHeaders(dbColumns,fileColumns):
			dataType = tableMetadata.readMetadata(clientName,rawTableName)
			fileRows = fileReader.readRows()
			
			for eachRow in fileRows :	
				self.rowNum = self.rowNum + 1
				if validation.validateRow(dataType,eachRow,self.rowNum) is False:
					error = "Error in dataType"
					break	
		else:
			error =  "Error in header"
		
		if error:
			print error
		else:	
			print"File sucessfully validated"
		
		
		
if  __name__ =='__main__':
	fileValidator = FileValidator()