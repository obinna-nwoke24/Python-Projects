"""
Author: Obinna Jason Nwoke II
"""
import Phonebook.assets.phonebook as phonebook


def main(b: phonebook.Book() = phonebook.Book()):
    """
    Main function of the program with each prompt
    :param b:
    :return:
    """

    print("""-- Phone Book App --""")

    def main_prompt():
        """
        Main prompt for the user
        :return:
        """
        return input("""1 - Add an entry
2 - Delete an entry
V - View the directory
S - Search
Q - Quit
- """)

    def search_prompt():
        """
        Search prompt for searching by name or number
        :return:
        """
        return input("""1 - Search By Name
2 - Search By Number
Q - Quit
- """)

    rq1 = main_prompt()
    while rq1 not in ['Q', 'q']:
        if rq1 == "1":
            ret = b.add_entry(input("First Name: "), input("Last Name: "), input("Phone Number: "))
            if ret:
                print("-- Entry Added --")
        elif rq1 == '2':
            ret = b.del_entry(input("First Name: "), input("Last Name: "))
            if ret:
                print("-- Entry Deleted --")
        elif rq1 in ['V', 'v']:
            b.view_sheet()
        elif rq1 in ['S', 's']:
            rq2 = search_prompt()
            while rq2 not in ['Q', 'q']:
                if rq2 == '1':
                    b.search_by_name(input("Full Name: "))
                elif rq2 == '2':
                    b.search_by_number(input("Phone Number: "))
                else:
                    print("Invalid command")
                rq2 = search_prompt()
        else:
            print("Invalid command")
        rq1 = main_prompt()
