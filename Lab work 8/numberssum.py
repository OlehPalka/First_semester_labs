"""
This module counts to different lists and
appends multiplication of i elements from both lists
"""
def narayana(number):
    """
    This function returns list of numbers.
    A(i) = A(i-1) + A(i-3), де A(0) = A(1) = A(2) = 1

    >>> narayana(12)
    [1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41]

    """
    result = [1, 1, 1]
    for element in range(3, number):
        result.append((result[element - 1]) + (result[element - 3]))
    return result

def lucas(number):
    """
    This function returns list of numbers.
    A(i) = A(i-1) + A(i-3), де A(0) = A(1) = A(2) = 1

    >>> lucas(12)
    [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]

    """
    result = [2, 1]
    for element in range(2, number):
        result.append(result[element - 1] + result[element - 2])
    return result

def numberssum(number):
    """
    This function returns multiplication of i element
    from naryanas() and from lucas()

    >>> numberssum(12)
    [2, 1, 3, 8, 21, 44, 108, 261, 611, 1444, 3444, 8159]
    """
    result = list()
    for element in range(number):
        result.append(narayana(number)[element] * lucas(number)[element])
    return result
