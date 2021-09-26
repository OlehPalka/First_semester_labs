"""
This module contains functions that generate specific numbers
in a specific ranges and each function returns a list with the
integers

"""

def numbers_Ulam(from_number: int, to_number: int) -> list:
    """
    Generates list of Ulam numbers in a specific range

    >>> numbers_Ulam(0, 10)
    [1, 2, 3, 4, 6, 8]
    >>> numbers_Ulam(5, 10)
    [6, 8]

    """
    if to_number <= 0:
        return None
    if to_number == 1:
        Ulam_numbers = [1]
    else:
        Ulam_numbers = [1, 2]
        while Ulam_numbers[-1] <= to_number:
            numbers_to_check = []
            for first_number in range(len(Ulam_numbers)-1):
                for second_number in range(first_number+1, len(Ulam_numbers)):
                    numbers_to_check.append(Ulam_numbers[first_number] + Ulam_numbers[second_number])
                    numbers_to_check.sort()
            check = True
            for number in numbers_to_check:
                if check:
                    if numbers_to_check.count(number) == 1 and number > Ulam_numbers[-1]:
                        Ulam_numbers.append(number)
                        check = False
    Ulam_numbers = Ulam_numbers[:-1]
    for number in Ulam_numbers:
        if number >= from_number:
            index_from = Ulam_numbers.index(number)
            break    
    return Ulam_numbers[index_from:]

def lucky_numbers(from_number: int, to_number: int) -> list:
    """
    Generates list of lucky numbers in a specific range

    >>> lucky_numbers(10, 30)
    [13, 15, 21, 25]

    """
    numbers = list(range(1, to_number+1))
    step = 1
    if len(numbers) > 1:
        del numbers[step::numbers[step]]
        while numbers[step-1] < len(numbers):
            del numbers[numbers[step]-1::numbers[step]]
            step += 1
    for number in numbers:
        if number >= from_number:
            index_from = numbers.index(number)
            break 
    return numbers[index_from:]

def even_numbers(from_number: int, to_number: int) -> list:
    """
    Generates list of even numbers in a specific range

    >>> even_numbers(20, 30)
    [20, 22, 24, 26, 28, 30]

    """
    result = [i for i in range(from_number, to_number+1) if i%2==0]
    return result

difficulty_ranges = {
        1:(0,50),
        2:(50,200),
        3:(200,500)
    }
