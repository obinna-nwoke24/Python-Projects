"""
Author: Obinna Jason Nwoke II
"""
import json
import pandas as pd

json_file = "C:\\Users\\holdm\\OneDrive\\Desktop\\PythonProjects\\Phonebook\\assets\\phonebook.json"
code = {0: IOError, 1: "Success"}


class Book:
    def __init__(self):
        """
        Initialize the phonebook class 'Book'
        Start off with an empty dictionary, but then load the json file
        in the event there are any records to load.
        """
        self.book = {}
        self.book = self.load_book(json_file)

    def add_entry(self, first_name: str = "", last_name: str = "", number: str = "3478894656"):
        """
        Add and entry to the phonebook. This method catches any errors based on the defined format
        of a phone number.
        :param first_name:
        :param last_name:
        :param number:
        :return:
        """
        try:
            if len(number) < 10:
                print("-- Not a recognized phone number --")
                raise code[0]
            if len(number) > 11:
                print("-- Not a recognized phone number --")
                raise code[0]
            if len(number) == 10:
                number = "(" + number[:3] + ")" + "-" + number[3:6] + "-" + number[6:]
                self.book[first_name + " " + last_name] = {"First Name": first_name,
                                                           "Last Name": last_name,
                                                           "Phone Number": number}
                self.update_json()
                return 1
            elif len(number) == 11:
                number = "+" + number[0] + " (" + number[1:4] + ")" + "-" + number[4:7] + "-" + number[7:]
                self.book[first_name + " " + last_name] = {"First Name": first_name,
                                                           "Last Name": last_name,
                                                           "Phone Number": number}
                self.update_json()
                return 1
        except code[0]:
            return 0

    def del_entry(self, first_name: str = "", last_name: str = ""):
        """
        Deletes an entry from the book if the first and last name matches. Catches the error
        in the event  the names dont match any records in the phonebook.
        :param first_name:
        :param last_name:
        :return:
        """
        try:
            check = first_name + " " + last_name
            if check in self.book.keys():
                del self.book[check]
                self.update_json()
                return 1
            else:
                print("-- %s is not in this phone book --" % check)
                raise code[0]
        except code[0]:
            return 0

    def search_by_name(self, full_name: str = ""):
        """
        Searches the phonebook by name. Return any records that match the parameter.
        :param full_name:
        :return:
        """
        pb = self.book_to_df()
        rows = []
        try:
            for index in pb.index:
                if full_name in (pb.loc[index]['First Name'] + " " + pb.loc[index]['Last Name']):
                    rows.append(index)
            if len(rows) == 0:
                print("-- No matching names --")
                raise code[0]
            else:
                pb = pb.loc[rows]
                print(pb)
                return 1
        except code[0]:
            return 0

    def search_by_number(self, number: str = ""):
        """
        Searches the phonebook by phone number. Matches any records who have a phone number
        containing the numbers in the parameter.
        :param number:
        :return:
        """
        def reformat(phn: str = "(346)-639-6120"):
            """
            Reformats the phone number to be only numbers for ease of use.
            :param phn:
            :return:
            """
            take_out = ['(', ')', '-', '+', ' ']
            ph = ""
            for char in phn:
                if char not in take_out:
                    ph += char
            if len(ph) == 11:
                ph = ph[1:]
            return ph

        try:
            formatted_number = reformat(number)
            pb = self.book_to_df()
            rows = []
            for index in pb.index:
                if formatted_number in reformat(pb.loc[index]['Phone Number']):
                    rows.append(index)
            if len(rows) == 0:
                print("-- No matching phone numbers --")
                raise code[0]
            else:
                pb = pb.loc[rows]
                print(pb)
                return 1
        except code[0]:
            return 0

    def view_sheet(self):
        """
        Views all records in the phonebook
        :return:
        """
        sheet = self.book_to_df()
        if len(sheet) == 0:
            print("No numbers in the book")
        else:
            print(sheet)

    def book_to_df(self):
        """
        Creates a dataframe data structure for the phonebook
        :return:
        """
        df = pd.DataFrame(columns=['First Name', 'Last Name', 'Phone Number'])
        for key in self.book.keys():
            df.loc[len(df)] = [self.book[key]['First Name'],
                               self.book[key]['Last Name'],
                               self.book[key]['Phone Number']]
        return df

    def load_book(self, file: str = json_file):
        """
        Uses the JSON file to load all current entries
        :param file:
        :return:
        """
        with open(file, 'r') as readfile:
            json_object = json.load(readfile)
        for key in json_object.keys():
            self.book[key] = {"First Name": json_object[key]['First Name'],
                              "Last Name": json_object[key]['Last Name'],
                              "Phone Number": json_object[key]['Phone Number']}
        return self.book

    def update_json(self):
        """
        Updates the JSON file with the most up-to-date entries/records
        :return:
        """
        json_object = json.dumps(self.book, indent=4)
        with open(json_file, 'w') as outfile:
            outfile.write(json_object)
