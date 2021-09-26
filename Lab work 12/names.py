"""
This module makes operations with given names file.
"""


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


def find_names(file_path):
    """
    This function returns names with usage of algorithms of sorting.
    """
    with open(file_path, encoding='utf-8') as file:
        lst = []
        for line in file:
            line = line.split()
            line.reverse()
            lst.append(line)
    final_result_three = dict()
    final_result_dict = dict()
    lst = lst[1:]
    for i in lst:
        i[0] = eval(i[0])
        if i[1][0] not in final_result_dict:
            final_result_dict[i[1][0]] = [1, i[0]]
        else:
            final_result_dict[i[1][0]][0] += 1
            final_result_dict[i[1][0]][1] += i[0]
    for i in final_result_dict:
        final_result_three[tuple(final_result_dict[i])] = i
    result = quick_sort(lst)
    part_for_second_result = {name[1] for name in result if name[0] == 1}
    final_result_three = max(final_result_three.items())
    final_result_one = {result[-1][1], result[-2][1], result[-3][1]}
    final_result_two = (len(part_for_second_result), part_for_second_result)
    final_result_three = (
        final_result_three[1], final_result_three[0][0], final_result_three[0][1])
    return (final_result_one, final_result_two, final_result_three)
