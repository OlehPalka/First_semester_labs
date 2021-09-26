"""
This module contains sorting and finding fucntions.
"""

import doctest
import math


def linear_search(list_of_values: list, value):
    """ Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    for index in enumerate(list_of_values):
        if list_of_values[index[0]] == value:
            return index[0]
    return -1


def binary_search(list_of_values, value):
    """
    This function returns index of the given element.
    If element not in list, fucntion reurns -1.

    >>> print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
    8
    >>> print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 23))
    -1
    """
    middle_element_inedx = math.ceil((len(list_of_values) - 1) // 2)
    start = 0
    end = len(list_of_values) - 1
    if list_of_values[start] == value:
        return start
    if list_of_values[end] == value:
        return end
    while len(list_of_values[start:end]) - 1 > 0:
        if list_of_values[middle_element_inedx] == value:
            return middle_element_inedx
        if list_of_values[middle_element_inedx] < value:
            start = middle_element_inedx
            middle_element_inedx = math.ceil((middle_element_inedx + end) / 2)
        elif list_of_values[middle_element_inedx] > value:
            end = middle_element_inedx
            middle_element_inedx = math.ceil(
                (start + middle_element_inedx) / 2)

    return -1


def merge(lst, start1, start2, end):
    """
    This function is helping function for mergesort.
    """
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for number in range(length):
        if ((index1 == start2) or ((index2 != end) and (lst[index1] > lst[index2]))):
            aux[number] = lst[index2]
            index2 += 1
        else:
            aux[number] = lst[index1]
            index1 += 1
    for number in range(start1, end):
        lst[number] = aux[number - start1]
    return aux


def merge_sort(lst) -> list:
    """
    This function sorts list of objects.

    >>> print(merge_sort([10, 6, 9, 5, 6, 7, 8, 9]))
    [5, 6, 6, 7, 8, 9, 9, 10]
    >>> print(merge_sort([]))
    []
    """
    list_lenth = len(lst)
    step = 1
    while step < list_lenth:
        for start1 in range(0, list_lenth, 2*step):
            start2 = min(start1 + step, list_lenth)
            end = min(start1 + 2*step, list_lenth)
            merge(lst, start1, start2, end)
        step *= 2
    return lst


def selection_sort(lst):
    """
    This function sorts list of objects.

    >>> print(selection_sort([10, 6, 9, 5, 6, 7, 8, 9]))
    [5, 6, 6, 7, 8, 9, 9, 10]
    >>> print(selection_sort([]))
    []
    """
    for first_num in range(len(lst) - 1):
        min_ind = first_num
        for second_num in range(first_num + 1, len(lst)):
            if lst[second_num] < lst[min_ind]:
                min_ind = second_num
        lst[first_num], lst[min_ind] = lst[min_ind], lst[first_num]
    return lst


def quick_sort(lst):
    """
    This function sorts list of objects.

    >>> print(quick_sort([10, 6, 9, 5, 6, 7, 8, 9]))
    [5, 6, 6, 7, 8, 9, 9, 10]
    >>> print(quick_sort([]))
    []
    """
    less = []
    pivot_list = []
    more = []
    if len(lst) <= 1:
        return lst
    if len(lst) >= 1:
        pivot = lst[0]
    for elemnt in lst:
        if elemnt < pivot:
            less.append(elemnt)
        elif elemnt > pivot:
            more.append(elemnt)
        else:
            pivot_list.append(elemnt)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivot_list + more
