import math
def generate_number(number, digit, position):
    """
    (int, int, int) -> int
    Number is integer. It can be >, < and = 0
    Digit - number from 0 to 9 included
    Position - integer > 0.
    Function has to return new number, where figure in position (position)
     will be replaced with figure (digit), if digit > figure (position).
     Positions in number are numerated from 0 from right side to left.
    If digit is > 9 or digit is < 0 function should return None.
    If position is <= 0 function should return None.

    >>> generate_number(-3746, -7, 5)
    None
    >>> generate_number(-3746, 17, 5)
    None
    >>> generate_number(-3746, 7, -5)
    None
    >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    >>> generate_number(3746, 5, 3)
    5746
    >>> generate_number(3746, 5, 4)
    53746
    >>> generate_number(3746, 5, 7)
    50003746
    >>> generate_number(-3746, 5, 7)
    -50003746
    """
    if digit < 0  or  digit > 9 or position < 0:
        return None
    # here i exclude minus digit meanig, and more then 9 digit meaning
    plus_numbers = int(math.sqrt(number ** 2))
    # here i turn all - and + numbers to plus numbers
    lenth = 0
    while True:
        whole_part = plus_numbers // 10 ** lenth
        if whole_part == 0:
            lenth_of_number = lenth
            break
        lenth += 1
    # Here i count the lenth of the input number
    if position < lenth_of_number:
        remainder = plus_numbers % 10 ** position
        # Here a remainder from the beggining number is found
        compared_number = plus_numbers // 10 ** position
        compared_number_remainder = compared_number % 10
        # Here the remainder of compared number is found
        if digit > compared_number_remainder:
            compared_number = (compared_number - compared_number_remainder) + digit
            result = (compared_number * (10 ** position)) + remainder
        else:
            result = (compared_number * (10 ** position)) + remainder
    else:
        result = digit * (10 ** position) + plus_numbers
    if number < 0:
        # Here i add minus if the input number was negative
        result = -result
    return result
