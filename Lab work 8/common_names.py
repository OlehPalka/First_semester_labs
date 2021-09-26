"""
This module finds same names in two files.
"""
def common_names(female_names: list, male_names: list) -> set:
    """
    This function returns set of names which occures in both files.

    >>> print(common_names(['lol'], ['lol']))
    {'lol'}
    """
    female_names = set(female_names)
    male_names = set(male_names)
    return male_names.intersection(female_names)

def names_read(file_name):
    """
    file.txt -> list()
    This function reads a file with names, and returns a list.
    """
    result_list = list()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            result_list.append(line[:-1])
    return result_list
