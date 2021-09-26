"""
This module makes operations with recursive functions.
"""


def table_creater(column, series, first_lst):
    """
    This function generates a greed of numbers n*m type.
    >>> print(table_creater(2, 6, []))
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6]]
    """
    if column == 1:
        first_lst.append([column for _ in range(series)])
        return first_lst
    table_creater(column - 1, series, first_lst)
    first_lst.append([1])
    for num in range(series - 1):
        part = first_lst[column - 2][num + 1] + first_lst[column - 1][num]
        first_lst[column - 1].append(part)
    return first_lst


def create_table(column, series):
    """
    This function creates a table whith n*m type filled with
    numbers counted by formula A[i][j] = A[i-1][j] + A[i][j-1].
    A[0][j] = 1, A[i][0] = 1

    >>> print(create_table(2, 6))
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6]]
    """
    first_lst = list()
    return table_creater(column, series, first_lst)


def del_list(lst, final_lst):
    """
    This function removes all lists, from the 1 list.
    >>> del_list([1,[2]], [])
    [1, 2]
    """
    for element in lst:
        if isinstance(element, list):
            del_list(element, final_lst)
        else:
            final_lst.append(element)
    return final_lst


def flatten(lst):
    """
    This function cheks list for other lists existed in it, and
    returns list without any other lists in it.

    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten([])
    []
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    if not isinstance(lst, list):
        result = lst
    else:
        final_lst = list()
        result = del_list(lst, final_lst)
    return result
