"""
This module makes operations with dictionary
"""


def dict_reader_tuple(file_dict):
    """
    file -> list
    This function returns list of tuples with pronansuation.
    """
    result = list()
    with open(file_dict, 'r', encoding='utf-8') as file:
        for line in file:
            part = list()
            line = line.split()
            third_part = list()
            for i in range(2, len(line)):
                third_part.append(line[i])
            part.append(line[0])
            part.append(int(line[1]))
            part.append(third_part)
            part = tuple(part)
            result.append(part)
    return result


# print(dict_reader_tuple("cmudict"))


def dict_reader_dict(file_dict):
    """
    file -> dict()
    This function returns dictionary with tuples with pronansuation of words.
    """
    words_list = dict_reader_tuple(file_dict)
    final_result = dict()
    for i in range(len(words_list) - 1):
        value = set()
        value.add(tuple(words_list[i][2]))
        if words_list[i][0] in final_result:
            final_result[words_list[i][0]].add((tuple(words_list[i][2])))
        else:
            final_result[words_list[i][0]] = value
    return final_result


def dict_invert(dct):
    """
    dict() -> dict()
    This function returns dictionary with
    words and their pronansuations. If word has more than 1 pronansuation,
    it is written down under another key.

    >>> print(dict_invert({'WATER':{('W','A','T','E','R')}}))
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    """
    result = dict()
    if isinstance(dct, list):
        final_result = dict()
        for i in range(len(dct) - 1):
            value = set()
            value.add(tuple(dct[i][2]))
            if dct[i][0] in final_result:
                final_result[dct[i][0]].add((tuple(dct[i][2])))
            else:
                final_result[dct[i][0]] = value
        dct = final_result
    for words in dct:
        key = len(dct[words])
        if key not in result:
            result[key] = set()
        for elements in dct[words]:
            pair = words, elements
            result[key].add(pair)
    return result
