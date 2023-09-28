import math


def expansion(base, number):
    """
    Get the expansion representation of a number given the base and the number
    :param base: int
    :param number: int
    :return: string
    """
    expansionRepresentation = ""

    while number != 0:
        remainder = number % base
        expansionRepresentation += str(remainder)
        number /= base
        number = math.floor(number)

    return expansionRepresentation[::-1]


def largestNumberOfDigitsToExpress(base, number):
    return math.ceil(math.log(number+1, base))

