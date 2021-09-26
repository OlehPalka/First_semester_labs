"""
This module makes operations with csv files.
"""
import math
import pandas as pd


def read_data():
    """
    This function reads csv file.
    """
    df_file = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df_file.columns:
        if col[:2] == '01':
            df_file.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df_file.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df_file.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df_file.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df_file.index.str.split('\\s\\(')  # split the index by '('

    # the [0] element is the country name (new index)
    df_file.index = names_ids.str[0]
    # the [1] element is the abbreviation or ID (take first 3 characters from that)
    df_file['ID'] = names_ids.str[1].str[:3]

    df_file = df_file.drop('Totals')
    # print(df)

    return df_file


def first_country(df_file):
    """
    This function returns information about te first country in the file.

    >>> print(first_country(read_data()))
    # Summer           13
    Gold                0
    Silver              0
    Bronze              2
    Total               2
    # Winter            0
    Gold.1              0
    Silver.1            0
    Bronze.1            0
    Total.1             0
    # Games            13
    Gold.2              0
    Silver.2            0
    Bronze.2            2
    Combined total      2
    ID                AFG
    Name: Afghanistan, dtype: object
    """
    return pd.Series(df_file.iloc[0])


def summer_biggest(df_file) -> str():
    """
    This function returns str with country, which has the biggest amount of gold medals.
    >>> print(summer_biggest(read_data()))
    United States
    """
    max_amount = max(list(df_file["Gold"]))
    # find max amount of gold medals
    return df_file[df_file["Gold"] == max_amount].index[0]


def difference_biggest(df_file):
    """
    This function returns country whith the biggest difference between golden medals
    in summer and winter games.

    >>> print(difference_biggest(read_data()))
    United States
    """
    gold_sum = list(df_file["Gold"])
    gold_win = list(df_file["Gold.1"])
    # lists for winter and summer gold medals
    counter = 0
    result = -1
    while counter <= len(gold_sum) - 1:
        # finds amount of medals after usage of the formula
        medals = math.sqrt((gold_sum[counter] - gold_win[counter]) ** 2)
        # find the biggest amount
        if medals > result:
            result = medals
            gold_sum_med = gold_sum[counter]
        counter += 1
    # find country for which this amount belongs
    return df_file[df_file["Gold"] == gold_sum_med].index[0]


def difference_biggest_relative(df_file):
    """
    This function returns the biggest difference between golden medals in summer and
    winter games but devided by total sum of gold medals.
    And without cuntries, which have 0 gold medals.

    >>> print(difference_biggest_relative(read_data()))
    Bulgaria
    """
    # find all countries which have more then one winter and summer medal
    df_file = df_file[df_file["Gold"] > 0]
    df_file = df_file[df_file["Gold.1"] > 0]
    # count difference with formula
    max_meaning = max(abs(df_file["Gold"] - df_file["Gold.1"]) /
                      (df_file["Gold"] + df_file["Gold.1"]))
    df_file = abs(df_file["Gold"] - df_file["Gold.1"]) / \
        (df_file["Gold"] + df_file["Gold.1"])
    # find country for which this amount belongs
    return df_file[df_file == max_meaning].index[0]


def get_points(df_file):
    """
    This function creates new column Points and writes down there points from all medals.
    >>> print(get_points(read_data()).index[0])
    Afghanistan
    """
    df_file["Points"] = df_file["Gold.2"] * 3 + \
        df_file["Silver.2"] * 2 + df_file["Bronze.2"]
    # create new part, and write ther down new points
    return df_file["Points"]
