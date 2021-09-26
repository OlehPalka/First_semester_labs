"""
This module returns paskal triangle.
"""
def generate_pascal_triangle(lines_number):
    """
    This function returns paskal triangle with n lines.
    If lines_number <= 0 function returns []

    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> generate_pascal_triangle(-2)
    []
    """
    result = list()
    # make check for first 3 numbers
    if lines_number < 0:
        result = []
    elif lines_number == 0:
        result = []
    elif lines_number == 1:
        result = [[1]]
    elif lines_number == 2:
        result = result.append([1], [1, 1])
    else:
        # make cycle for all other numbers
        result = [[1], [1, 1]]
        number_of_repeats = lines_number - 2
        repeats_counter = 0
        while True:
            #add [1]
            repeats_counter += 1
            new_part = []
            last_part = result[-1]
            new_part.append(1)
            sum_index = 0
            while True:
                #add new sums of neighboring symbols
                new_part.append(last_part[sum_index] + last_part[sum_index + 1])
                sum_index += 1
                if sum_index == len(last_part) - 1:
                    break
            #add [1]
            new_part.append(1)
            result.append(new_part)
            if repeats_counter == number_of_repeats:
                break
    return result
