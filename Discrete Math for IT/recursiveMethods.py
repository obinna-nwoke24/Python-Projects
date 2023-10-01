def problem1(n):
    """
    f sub 0 = 4
    f sub n = f sub n-1 + 5n
    for n >= 1
    :param n:
    :return:
    """
    if n == 0:
        return 4
    else:
        return problem1(n-1) + (5*n)


def problem2(n):
    """
    f sub 0 = 4
    f sub n = n^2 * f sub n-1
    for n >= 1
    :param n:
    :return:
    """
    if n == 0:
        return 4
    else:
        return n**2 * problem2(n-1)


def problem3(n):
    """
    f0 = 2
    fn = -2 + fn-1  for n>=1
    :param n:
    :return:
    """
    if n == 0:
        return 2
    else:
        return (-2) + problem3(n-1)


def problem4(n):
    """
    f0 = 2
    f1 = 5
    fn = fn-2 * fn-1    for n>= 2
    :param n:
    :return:
    """
    if n == 0:
        return 2
    elif n == 1:
        return 5
    else:
        return problem4(n-2) * problem4(n-1)


print(problem1(3), problem2(3), problem3(3), problem4(3))
