from Client import Client as c


def load_preset():
    """
    Loads a list of preset clients

    :return: List of preset Clients
    """
    clients = [
        c("Jason Nwoke", 67, 192, 'male', 21, 'moderately active'),
        c("Calvon Spencer", 69, 175, 'male', 23, 'moderately active')
    ]

    return clients
