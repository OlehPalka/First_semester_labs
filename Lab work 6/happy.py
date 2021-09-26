"""
Finds lucky numbers and does some operations with them
"""
def happy_number(number: int) -> bool:
    """
    This function rerturns True if summary of first 4 numbers in
    number = summary of other four numbers.
    If not, function returns False.

    >>> happy_number(123)
    False
    >>> happy_number(43211234)
    True
    """
    length = len(str(number))
    if length < 8:
        # add zeroes if number lenth is smaller then 8
        number = "0" * (8 - length) + str(number)
    sum_1 = 0
    sum_2 = 0
    for i in range(8):
        number = str(number)
        if i < 4:
            #count sum for first four numbers
            sum_1 += int(number[i])
        else:
            #count sum for first four numbers
            sum_2 += int(number[i])
    if sum_1 == sum_2:
        return True
    else:
        return False

def count_happy_numbers(number: int) -> int:
    """
    This function returns amount of happy numbers in in numbers from 0 to n.

    >>> count_happy_numbers(123)
    1
    """
    counter = 0
    #count how many happy numbers ar in range of input number
    for i in range(number):
        if happy_number(i) == True:
            counter += 1
    return counter
def happy_numbers(start_number, finish_number: (int, int)) -> list:
    """
    This function returns list of lucky numbers from m to n.

    >>> happy_numbers(0, 1)
    [0]
    """
    list_of_lucky_nums = list()
    #count amount of happy numbers from m to n
    while True:
        if happy_number(start_number) == True:
            list_of_lucky_nums.append(start_number)
        start_number += 1
        if start_number > finish_number:
            break
    return list_of_lucky_nums
