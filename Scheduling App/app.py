"""
Simple Staff scheduling app
Authors: Obinna Jason Nwoke II, Calvon Spencer
"""
import numpy as np

import schedule

version = '1.0.0'
"""
Staff database contains:
Staff name
Title
Phone Number
Email Address
Schedule/Shifts
"""
staff_database = {

}
timesheet = schedule.empty_schedule()


def menu():
    print('1 - Add Staff')
    print('2 - View All Staff Members')
    print('3 - Show Staff Details')
    print('4 - View Schedule')
    print('0 - Exit')
    try:
        val = int(input('Choice: '))
        return val
    except ValueError:
        print('\nYou did not input an integer value\n')
        menu()


def staff_menu():
    print('1 - Update Title')
    print('2 - Update Phone Number')
    print('3 - Update Email Address')
    print('0 - Back')
    try:
        val = int(input('Choice: '))
        return val
    except ValueError:
        print('\nYou did not input an integer value\n')
        staff_menu()


def schedule_menu():
    print('1 - Fill Shift')
    print('2 - Remove Shift')
    print('0 - Back')
    try:
        val = int(input('Choice: '))
        return val
    except ValueError:
        print('\nYou did not input an integer value\n')
        schedule_menu()


def run():
    value = menu()
    if value == 0:
        print('closing menu')
        exit()
    elif value == 1:
        name = input('\nStaff name (first and last) - ')
        title = input('Title: ')
        number = input('Phone Number: ')
        email_address = input('Email address: ')

        staff_database[name] = {'Title': title, 'Phone Number': number, 'Email Address': email_address, 'Shifts': []}
        print('Staff Database updated!\n')
    elif value == 2:
        if len(staff_database) == 0:
            print('\nThere are no staff members in your database\n')
        else:
            print('\nStaff Members')
            for name in staff_database.keys():
                print(name)
            print()
    elif value == 3:
        if len(staff_database) == 0:
            print('\nThere are no staff members in your database\n')
        else:
            who = input('\nEnter the staff you want to look up (first and last name) - ')
            if not staff_database.keys().__contains__(who):
                print(who + ' does not exist in our system!\n')
            else:
                print('\n' + who + ', ' + staff_database[who]['Title'])
                print('Phone number: ' + staff_database[who]['Phone Number'])
                print('Email address: ' + staff_database[who]['Email Address'])
                if len(staff_database[who]['Shifts']) == 0:
                    print('Shifts: No shifts\n')
                else:
                    print('Shifts')
                    for shift in staff_database[who]['Shifts']:
                        print(shift)
                        print()

                staff_value = ''
                while staff_value != 0:
                    staff_value = staff_menu()
                    if staff_value == 0:
                        print()
                        continue
                    elif staff_value == 1:
                        staff_database[who]['Title'] = input('Update title - ')
                        print('Title updated!\n')
                    elif staff_value == 2:
                        staff_database[who]['Phone Number'] = input('Update phone number - ')
                        print('Phone number updated!\n')
                    elif staff_value == 3:
                        staff_database[who]['Email Address'] = input('Update email address - ')
                        print('Email address updates!\n')
                    else:
                        print('\nYou did not choose an option above\n')

                    print(who + ', ' + staff_database[who]['Title'])
                    print('Phone number: ' + staff_database[who]['Phone Number'])
                    print('Email address: ' + staff_database[who]['Email Address'] + '\n')
    elif value == 4:
        print()
        print(timesheet)
        if len(staff_database) == 0:
            print('There are no staff to give a shift to\n')
        else:
            schedule_value = ''
            while schedule_value != 0:
                schedule_value = schedule_menu()
                if schedule_value == 0:
                    print()
                    continue
                elif schedule_value == 1:
                    day = input('What day do you want to fill - ')
                    shift = input('What shift do you want to fill - ')
                    person = input('Who do yu want to fill this shift - ')
                    coverage = input('Start time and end time of shift - ')

                    staff_database[person]['Shifts'].append(schedule.shift(day, shift, coverage))
                    timesheet.loc[shift, day] = person
                    print()
                elif schedule_value == 2:
                    day = input('What day do you want to open - ')
                    shift = input('What shift do you want to open - ')

                    for i in staff_database[timesheet.loc[shift, day]]['Shifts']:
                        if (day in i) & (shift in i):
                            staff_database[timesheet.loc[shift, day]]['Shifts'].remove(i)
                    timesheet.loc[shift, day] = 'Open Shift'

                else:
                    print('\nYou did not choose an option above\n')

                print(timesheet)

    else:
        print('\nInvalid command\n')

    run()


run()
