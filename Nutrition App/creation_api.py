import Client


def create_client_from_input():
    """
    Creates a client from input

    :return: Client
    """
    name = input("Name (first and last name): ")
    height = int(input("Height (inches): "))
    weight = int(input("Weight (lbs): "))
    gender = input("Gender (male or female): ")
    client = Client.Client(name, height, weight, gender)
    return client
