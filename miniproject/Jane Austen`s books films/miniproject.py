"""
This module contains main function of miniproject.
"""
import tabulate
import pandas as pd
from termcolor import colored, cprint
import random
import read_sort


def main_function(file_tsv, file_csv):
    """
    Ths function returns data Frame object of films,
    which are based on Jane Austen`s books.
    But before that, function filteres theese films
    whith parameteres user would like to enclude.
    """
    read_file_tsv = pd.read_csv(file_tsv, sep='\t', low_memory=False)
    read_file_csv = pd.read_csv(file_csv)
    possible_genres = read_sort.genres(read_file_csv, read_file_tsv)
    titles_type = read_sort.titles_types_lst(read_file_tsv)
    for genre in enumerate(possible_genres):
        possible_genres[genre[0]] = possible_genres[genre[0]].capitalize()
    read_file_tsv = read_sort.age_check(read_file_tsv)
    read_file_tsv = read_sort.year_film(read_file_tsv)
    read_file_tsv = read_sort.genres_bk_flm(
        read_file_csv, read_file_tsv, possible_genres)
    result = read_sort.titles_film_sort(read_file_tsv, titles_type)
    print()
    print()
    print()
    if result[["titleType", "primaryTitle", "startYear", "genres"]].empty:
        print("What a pity, we have not found any films whith your description 🥺")
        result = "You can try again!"
    else:
        result = result[["titleType", "primaryTitle",
                         "startYear", "genres"]]
    return result


if __name__ == "__main__":
    print(main_function("data.tsv", "classification.csv"))
