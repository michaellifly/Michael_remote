'''
main file to read from csv
Created By; MANUJ manujrastogi@gmail.com
'''
import re, csv, sys
from optparse import OptionParser, make_option


class ParseCsv(object):
    """
    Class to parse CSV
    """

    def __init__(self, path):
        """
        Constructor -- set the file path
        """
        self.csv_path = path
        # check if csv format is valid or not
        self.check_valid_csvformat(self.csv_path)
        """ empty dict to store all company names
        prepare initial company data in dictionary format """
        self.company_data = dict()

    def __call__(self):
        """
        Calls the cvsfileUsage function to start parsing
        """
        return self.csvfileUsage()

    def check_valid_csv_header(self, row):
        """
        Check if Header is correct
        """
        obj = re.match(re.compile('^Year\,Month\,.'),
                                            ','.join(row))
        if not obj:
            raise Exception("Invalid Headers must be `Year` `Month` Check Sample file")

    def check_valid_csv_data(self, row):
        """
        Check For valid csv data
        """
        obj = re.match(re.compile('^[0-9]{4}\,[A-Z]{1}[a-z]{2}\,.'),
                                            ','.join(row))
        if not obj:
            raise Exception("Invalid Data String must be like `1990` `Jan` Check Sample file")

    def check_valid_csvformat(self, csv_path):
        """
        Check if csv is in valid format with data
        """
        with open(self.csv_path, "rb+") as file_obj:
            reader = csv.reader(file_obj, delimiter=',')  # CSV DictReader object
            self.check_valid_csv_header(reader.next())
            self.check_valid_csv_data(reader.next())

    def parse_my(self, row):
        '''
        Parse month and year from each row
        '''
        month = row['Month']
        year = row['Year']
        return month, year

    def prepare_company_data(self, month, year, row, company_data):
        """
        Prepare the company's data
        """
        for key, value in row.items():
            if not company_data[key]:
                company_data[key] = {'year':year, 'month':month, 'value':value}
            else:
                """main operation updating the company's data per year
                    and month vise """
                company_data[key].update({'year':year, 'month':month, 'value':value})\
                             if company_data[key]['value'] < value else None

    def csvfileUsage(self):
        """
        Read the file and parse it
        """
        with open(self.csv_path, "rb+") as file_obj:
            reader = csv.DictReader(file_obj, delimiter=',')  # CSV DictReader object
            """ reader.fieldnames returns header , slicing intial 'Month' and
                'Year' header from list
            """
            for com_names in reader.fieldnames[2:]:
                self.company_data[com_names] = {}
            # iterating each row
            for row in reader:
                month, year = self.parse_my(row)  # parsing the year and month from row
                # pop the `Month` and `Year` Key to minimize iteration below
                row.pop('Month'), row.pop('Year')
                """ saving and updating the data at same point of time
                    each iteration time,  checking the max value and updating 
                    `Month` `Year` and `Value`
                """
                self.prepare_company_data(month, year, row, self.company_data)
            file_obj.close()  # close file
            return self.company_data

    def print_pretty(self, data):
        """
        print result data in pretty format
        """
        length = max(map(lambda x: len(x), data.keys()))
        print ('+-------------------------------------+')
        print ('| Company Name | Year | Month | Value |')
        print ('+-------------------------------------+')
        for key, value in data.items():
            print ('| %s    | %s | %s   | %s    |') % (key, \
            value['year'], value['month'], value['value'])
        print ('+-------------------------------------+')

if __name__ == '__main__':
    option_list = [make_option('--csvpath',
        dest='csvpath',
        default=False,
        help='''Generate report for an org. 
                Usage: --csvpath <path_to_csv_file>''')]
    parser = OptionParser(option_list=option_list)  # parse commandline argument
    (options, args) = parser.parse_args()
    if options.csvpath:  # if there is csv path then allow to execute
        try:
            parsecsvfile = ParseCsv(options.csvpath)  # Create Object
            data = parsecsvfile()  # call the csvparsing function
            parsecsvfile.print_pretty(data)  # print the pretty output
        except Exception as e:
            print (e)
    else:
        print ("Wrong Input: Run --help")
