import csv
from requests import get
from googlesearch import search
from time import sleep
from os import mkdir, path
from PyInquirer import prompt


class Scraper():
    'Scraping data based on CSV file'

    # List of journals with full names
    __journals = []

    # Constructor
    def __init__(self):
        self.__askForFileOrName()
        # self.__file = file
        # self.__output = output
        # self.__setJournals()
        # self.__getFormattingUrl()

    # Asks for file or name of journal
    def __askForFileOrName(self):
        question = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Enter the Journal name or file path (CSV Only)',
                'validate': lambda answer: 'You must enter something to proceed.' if len(answer) == 0 else True
            }
        ]
        answer = prompt(question)
        name = answer['name']
        if answer['name'].find('.csv') > 0:
            question = [
                {
                    'type': 'input',
                    'name': 'output',
                    'message': 'Enter the Output file name (CSV Only)',
                    'validate': lambda answer: 'You must enter something to proceed.' if len(answer) == 0 else True
                }
            ]
            answer = prompt(question)
            output = answer['output']
            if answer['output'].find('.csv') < 1:
                output += '.csv'
                self.__initializeFileOperation(name, output)
        else:
            self.__showUrl(name)

    # Show Url on CLI
    def __showUrl(self, name):
        self.__journals = [name]
        self.__getFormattingUrl()

    # Initialize CSV file saving operation
    def __initializeFileOperation(self, name, output):
        self.__file = name
        self.__output = output
        self.__setJournals()
        self.__generate(self.__getFormattingUrl())

    # Sets Journal from CSV file
    def __setJournals(self):
        with open(self.__file, 'rt') as file:
            file = csv.reader(file)
            for journal in file:
                self.__journals.append(journal[0])

    # Print with seperator
    def __printWithSeperator(self, message):
        print('-----------------------------------------------------------')
        print(str(message))

    # Get formatting URL
    def __getFormattingUrl(self):
        data = []
        for journal in self.__journals:
            sleep(5)
            self.__printWithSeperator('Fetching formatting url for ' + journal)
            for url in search(journal + ' journal formatting', stop=1):
                data.append({'Journal': journal, 'Url': url})
                print('Formatting Url for ' + journal + ' is ' + url)
        return data

    # Generate CSV file
    def __generate(self, data):
        self.__printWithSeperator('Writing data into CSV...')
        try:
            if path.isdir('dist') == False:
                mkdir('./dist')
            with open('./dist/' + self.__output, 'w', newline='') as file:
                headers = ['Journal', 'Url']
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except OSError:
            self.__printWithSeperator(
                'We are unable to generate the output file. Please check the permissions.')
        else:
            self.__printWithSeperator(
                'Application has been executed successfully.')


scraper = Scraper()
