import pandas as pd
import Client


def generate_table(client_list: list = None):
    """
    Generates table from a list of given clients

    :return: Client DataFrame
    """
    client_sheet = pd.DataFrame(columns=['Name', 'Height (in)', 'Weight (lbs)', 'Gender', 'Age', 'Activity Level',
                                         'Maintenance Calories', 'Weight Loss (1lb/wk)', 'Weight Gain (1lb/wk)'])

    sum_of_bad_types = 0
    try:
        for client in client_list:
            if type(client) != Client.Client:
                sum_of_bad_types += 1
        if sum_of_bad_types > 0:
            raise TypeError
    except TypeError:
        if sum_of_bad_types > 0:
            print("There is at least 1 object in the list that is not a client")
            return TypeError
    # If the code reaches here, we can code the dataframe

    for number in range(len(client_list)):
        row = [client_list[number].name, client_list[number].height, client_list[number].weight,
               client_list[number].gender, client_list[number].age, client_list[number].activity_level,
               client_list[number].maintenance, client_list[number].lose_weight(), client_list[number].gain_weight()]
        client_sheet.loc[number] = row

    return client_sheet


def to_excel(client_list: list = None, file_name: str = "clients.xlsx"):
    """
    Uses the client list to export data to excel

    :param file_name:
    :param client_list:
    :return: None
    """
    if client_list is None:
        client_list = []
    sheet = generate_table(client_list)
    if type(sheet) == type:
        print("Cannot convert to excel")
        exit()
    sheet = sheet.set_index("Name")
    sheet.to_excel(file_name, sheet_name='Clients')
