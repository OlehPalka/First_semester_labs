"""
This module makes operations with csv file with American states.
"""

import doctest
import pandas as pd


def read_data(path_to_file):
    """
    This function reads csv file, and returns dataframe object.
    """
    return pd.read_csv(path_to_file)


def max_counties(df_census):
    """
    This function returns name of the state with the biggest
    amount of counties.

    >>> print(max_counties(read_data("census.csv")))
    Texas
    """
    result = dict()
    for state in df_census["STNAME"]:
        # add names to the dictionary
        if state not in result:
            result[state] = 1
        else:
            result[state] += 1
    # take and sort itemes
    result = list(result.items())
    result.sort(key=lambda i: i[1])
    return result[-1][0]


def max_difference(df_census):
    """
    This function returns name of county which has the
    biggest absolute number of population.

    >>> print(max_difference(read_data("census.csv")))
    Harris County
    """
    tenth = list(df_census["POPESTIMATE2010"])
    eleventh = list(df_census["POPESTIMATE2011"])
    tvelth = list(df_census["POPESTIMATE2012"])
    thirteenth = list(df_census["POPESTIMATE2013"])
    fourteenth = list(df_census["POPESTIMATE2014"])
    fifteenth = list(df_census["POPESTIMATE2015"])
    # create lists for all years
    counter = 0
    result = list()
    while counter < len(tenth):
        sort_list = sorted([tenth[counter], eleventh[counter], tvelth[counter],
                            thirteenth[counter], fourteenth[counter], fifteenth[counter]])
        # sort itemes in list to find the biggest and the smallest meanings
        result.append(abs(sort_list[-1] - sort_list[0]))
        # list with population difference
        counter += 1
    df_census["POP"] = pd.Series(result)
    # create new part for differences
    df_census = df_census[df_census["SUMLEV"] == 50]
    return df_census.iloc[df_census["POP"].argmax()]["CTYNAME"]


def conditional_counties(df_census):
    """
    This function returns DataFrame object of counties from 1
    and 2 regions, and which names sgtarts with Washington.

    >>> print(conditional_counties(read_data("census.csv")))
                STNAME            CTYNAME
    896           Iowa  Washington County
    1419     Minnesota  Washington County
    2345  Pennsylvania  Washington County
    2355  Rhode Island  Washington County
    3163     Wisconsin  Washington County
    """
    result_0 = df_census[df_census["REGION"] != 4]
    result_0 = result_0[result_0["REGION"] != 3]
    # delete useless itemes
    result_0 = result_0[result_0["CTYNAME"] == "Washington County"]
    # choose which ones start with Washington County
    result_0 = result_0[result_0["POPESTIMATE2015"]
                        > result_0["POPESTIMATE2014"]]
    return result_0[['STNAME', 'CTYNAME']]
