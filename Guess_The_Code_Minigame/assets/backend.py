"""
Author: Obinna Jason Nwoke II
"""
import json


def load(json_file: str = ""):
    """
    Loads the JSON file and returns the object
    :param json_file:
    :return:
    """
    with open(json_file, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object


def update_json(management_variable, file_variable):
    """
    Updates the JSON file
    :param management_variable:
    :param file_variable:
    :return:
    """
    json_object = json.dumps(management_variable, indent=4)
    with open(file_variable, 'w') as outfile:
        outfile.write(json_object)
