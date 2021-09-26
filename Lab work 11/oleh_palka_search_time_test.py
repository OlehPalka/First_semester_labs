"""
This module counts time of functions, and writes them into the file.
"""

from timeit import Timer as t


def linear_search_while(lst: list, value: int) -> int:
    """ Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_while([2, 5, 1, -3], 5)
    1
    >>> linear_search_while([2, 4, 2], 2)
    0
    >>> linear_search_while([2, 5, 1, -3], 4)
    -1
    >>> linear_search_while([], 5)
    -1
    """
    index = 0  # The index of the next item in lst to examine.
    # Keep going until we reach the end of lst or until we find value.
    while index != len(lst) and lst[index] != value:
        index += 1
        # If we fell off the end of the list, we didn't find value.
    if index == len(lst):
        return -1
    return index


def linear_search_for_loop(lst: list, value: int) -> int:
    """ Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_for_loop([2, 5, 1, -3], 5)
    1
    >>> linear_search_for_loop([2, 4, 2], 2)
    0
    >>> linear_search_for_loop([2, 5, 1, -3], 4)
    -1
    >>> linear_search_for_loop([], 5)
    -1
    """
    for index in enumerate(lst):
        if lst[index[0]] == value:
            return index[0]
    return -1


def linear_search_sentinel(lst: list, value: int) -> int:
    """ Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_for_loop([2, 5, 1, -3], 5)
    1
    >>> linear_search_for_loop([2, 4, 2], 2)
    0
    >>> linear_search_for_loop([2, 5, 1, -3], 4)
    -1
    >>> linear_search_for_loop([], 5)
    -1
    """
    # Add the sentinel.
    lst.append(value)
    index = 0
    # Keep going until we find value.
    while lst[index] != value:
        index = index + 1
        # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if index == len(lst):
        return -1
    return index


def linear_search_list_index(lst: list, value: int) -> int:
    """ Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_list_index([2, 5, 1, -3], 5)
    1
    >>> linear_search_list_index([2, 4, 2], 2)
    0
    >>> linear_search_list_index([2, 5, 1, -3], 4)
    -1
    >>> linear_search_list_index([], 5)
    -1
    """
    try:
        return lst.index(value)
    except ValueError:
        return -1


def comparing_func(lst: list, value: int):
    """
    This function returns sorted time of 4 differenr
    linear search functions in dictionary. (Time always changes)
    """
    list_of_time = \
        sorted([("linear_search_while - ",
                 t(lambda: linear_search_while(lst, value)).timeit()),
                ("linear_search_sentinel - ",
                 t(lambda: linear_search_sentinel(lst, value)).timeit()),
                ("linear_search_for_loop - ",
                 t(lambda: linear_search_for_loop(lst, value)).timeit()),
                ("linear_search_list_index - ",
                 t(lambda: linear_search_list_index(lst, value)).timeit())], key=lambda element: element[1])
    with open('newfile.txt', 'w', encoding='utf-8') as file:
        for element in list_of_time:
            file.write(str(element) + '\n')


print(comparing_func([3, 1, 4, 2, 5], 3))
