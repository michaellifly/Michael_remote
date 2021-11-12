'''
test file to read from csv
Created By; MANUJ manujrastogi@gmail.com
'''

import unittest
from main import ParseCsv

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.parsedData = {'Company A': {'year': '2000', 'value': '93', 'month': 'Jan'},
                    'Company B': {'year': '2000', 'value': '84', 'month': 'Aug'},
                    'Company C': {'year': '1992', 'value': '93', 'month': 'Jan'}}
        self.csvpath = 'bs.csv'
        self.format = True

    def test_csvformat(self):
        format = False
        try:
            parsercsv_obj = ParseCsv(self.csvpath)
            format = True
        except Exception as e:
            self.assertEqual(self.format, format)

    def test_parseData(self):
        data = {}
        try:
            parsercsv_obj = ParseCsv(self.csvpath)
            data = parsercsv_obj()
            self.assertEqual(self.parsedData, data)
        except Exception as e:
            self.assertEqual(self.parsedData, data)

if __name__ == '__main__':
    unittest.main()
