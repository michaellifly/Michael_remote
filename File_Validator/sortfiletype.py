import sys
import re

class SortFileType:

	def getFileType(self,clientName,fileName):
		
		if clientName == 'Correctcare':
			if re.search('^jobs\.[0-9.]+',fileName):
				fileType = 'req'
				rawTableName = 'zzz_cc_req_raw'
				return fileType,rawTableName
			elif (re.search('^candidates\.[0-9.]+',fileName)):
				fileType = 'candidate'
				rawTableName = 'zzz_cc_candidate_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")
				
		elif clientName == 'Pepsico':
			if re.search('^NEW\sBB\sCandidate\s',fileName):
				fileType = 'candidate'
				rawTableName = 'zzz_pepsico_candidate_raw'
				return fileType,rawTableName
			elif (re.search('^NEW\sBB\sReq\s',fileName)):
				fileType = 'req'
				rawTableName = 'zzz_pepsico_req_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")
			
		elif clientName == 'ADP':
			if re.search('^ADP~adpbroadbean_RM_Can_[0-9_]+',fileName):
				fileType = 'candidate'
				rawTableName = 'zzz_adp_candidate_raw'
				return fileType,rawTableName
			elif (re.search('^ADP~adpbroadbean_RM_Req_[0-9_]+',fileName)):
				fileType = 'req'
				rawTableName = 'zzz_adp_req_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")
		
		elif clientName == 'Stryker':
			if re.search('^BDAS\sCandidate\s[0-9_A-Za-z]',fileName):
				fileType = 'candidate'
				rawTableName = 'zzz_adp_candidate_raw'
				return fileType,rawTableName
			elif (re.search('^BDAS\sReqToDate\s[0-9_A-Za-z]',fileName)):
				fileType = 'req'
				rawTableName = 'zzz_adp_req_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")

		else:
			sys.exit("Unknown client")