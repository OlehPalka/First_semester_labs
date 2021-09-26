"""
This module contains functions for main function named miniproject.py
I this module functions make sorting of films and books according to
user`s choice.
"""

import pandas as pd
from termcolor import colored, cprint
import random


def tsv_genres(read_file_tsv):
    """
    This function returns all genres for films in tsv file (IMDB).
    """
    genres_lst = list()
    for i in read_file_tsv["genres"]:
        try:
            i = i.split(",")
            for element in i:
                if element.lower() not in genres_lst and element != '\\N':
                    genres_lst.append(element.lower())
        except AttributeError:
            continue
    return genres_lst


def classification_genres(read_file_csv):
    """
    This function returns all genres for films in csv file (given file).
    """
    genres_lst = list()
    for i in read_file_csv["Genre"]:
        try:
            if i != "":
                element = i.split(" ")
                for part in element:
                    if part.lower() not in genres_lst and part.lower() != "":
                        genres_lst.append(part.lower())
        except AttributeError:
            continue
    return genres_lst


def genres(read_file_csv, read_file_tsv):
    """
    This function compares ti lists of genres.
    One of them is from films, another from books.
    As the result function returns list with possible genres
    for books, which are in film genres.

    ['Comedy', 'Romance', 'Drama', 'Fantasy', 'Horror', \
'Biography', 'Music', 'History', 'Mystery', 'Adult']
    """
    books_genres = classification_genres(read_file_csv)
    films_genres = tsv_genres(read_file_tsv)
    result = list()
    for genre in enumerate(films_genres):
        if genre[1] in books_genres:
            result.append(genre[1])
    return result


def year_film(read_file_tsv):
    """
    This function accepts year from user, and choose from tsv file (IMDB)
    those films, which were shoted after given year.
    """
    color_list = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    color = random.choice(color_list)
    print()
    print()
    print()
    print(colored("****************************************************", color))
    print(colored("*", color), end="")
    print("Do you want to see films shoted after chosen year?", end="")
    print(colored("*", color))
    print(colored("*", color), end="")
    print("If yes, enter year. If not, press Enter           ", end="")
    print(colored("*", color))
    print(colored("****************************************************", color))
    print()
    print()
    print()
    while True:
        year = str(input())
        print()
        try:
            if year == "":
                break
            year = int(year)
            break
        except ValueError:
            print("Enter a number!")
            print()
    year = str(year)
    if year != "":
        read_file_tsv = read_file_tsv[read_file_tsv["startYear"] >= year]
        read_file_tsv = read_file_tsv[read_file_tsv["startYear"] != "\\N"]
    return read_file_tsv


def age_check(read_file_tsv):
    """
    This function checkes if user is already 18 years old.
    If not, it deletes all films, which are for adults.
    If user is already 18, function does not make any changes in file.
    """
    color_list = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    color = random.choice(color_list)
    print()
    print()
    print()
    print(colored("*********************", color))
    print(colored("*", color), end="")
    print("Are you already 18?", end="")
    print(colored("*", color))
    print(colored("*", color), end="")
    print("Enter yes or no.   ", end="")
    print(colored("*", color))
    print(colored("*********************", color))
    print()
    print()
    print()
    while True:
        age = str(input())
        print()
        if age in ("yes", "no"):
            break
        print("You have not confirmed your age.")
        print("""Enter "yes" or "no".""")
        print()
    if age == "no":
        return read_file_tsv[read_file_tsv["isAdult"] == 0]
    return read_file_tsv


def titles_types_lst(read_file_tsv):
    """
    This function returns list of all possible titles for films
    in IMDB file.

    ['short', 'movie', 'tvShort', 'tvMovie', 'tvSeries', \
    'tvEpisode', 'tvMiniSeries', 'tvSpecial', 'video', \
    'videoGame', 'audiobook', 'radioSeries', 'episode']
    """
    result = list()
    for title in read_file_tsv["titleType"]:
        if title not in result:
            result.append(title)
    return result


def genres_bk_flm(read_file_csv, read_file_tsv, possible_genres):
    """
    This function returns read_file_tsv but before that
    sorts it according to the genre user will choose.
    """
    color_list = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    color = random.choice(color_list)
    print()
    print()
    print()
    print(colored("*****************************************************************", color))
    print(colored("*", color), end="")
    print("Do you want to choose possible genres for books of this author?", end="")
    print(colored("*", color))
    print(colored("*", color), end="")
    print("""Enter "yes" or "no".                                           """, end="")
    print(colored("*", color))
    print(colored("*****************************************************************", color))
    print()
    print()
    print()
    while True:
        genres_yes_no = input()
        print()
        if genres_yes_no in ("yes", "no"):
            break
        print("You have not answered the question.")
        print()
    if genres_yes_no == "yes":
        print(possible_genres)
        color = random.choice(color_list)
        print()
        print()
        print()
        print(colored(
            "************************************************************************", color))
        print(colored("*", color), end="")
        print(
            "Enter genre of the book, based on which you want to see a film.       ", end="")
        print(colored("*", color))
        print(colored("*", color), end="")
        print("""If you want to see all films based on Jane Austen books press "Enter".""", end="")
        print(colored("*", color))
        print(colored(
            "************************************************************************", color))
        print()
        print()
        print()
        while True:
            genre = input()
            print()
            if genre == "":
                read_file_csv = read_file_csv[read_file_csv["Genre"].notna()]
                break
            if genre not in possible_genres:
                print("Enter a genre from the list!")
                print()
            else:
                read_file_tsv = read_file_tsv[read_file_tsv["genres"] == genre]
                break
        titles_lst = list(read_file_csv["Title"])
        read_file_tsv = read_file_tsv[read_file_tsv["primaryTitle"].isin(
            titles_lst)]

    return read_file_tsv


def titles_film_sort(read_file_tsv, titles_type):
    """
    This returns sorted read_file_tsv by name of typeTitle.

    """
    color_list = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    color = random.choice(color_list)
    print()
    print()
    print()
    print(colored("************************************************************", color))
    print(colored("*", color), end="")
    print("Do you want to see films of the special chosen title type?", end="")
    print(colored("*", color))
    print(colored("*", color), end="")
    print("""If yes, enter "yes", in opther case press "Enter".        """, end="")
    print(colored("*", color))
    print(colored("************************************************************", color))
    print()
    print()
    print()
    while True:
        title_yes_no = input()
        print()
        if title_yes_no in ("yes", ""):
            break
        print("""Please, enter "yes" or press "Enter".""")
        print()
    if title_yes_no == "yes":
        color = random.choice(color_list)
        print()
        print()
        print()
        print(colored(
            "****************************************************************", color))
        print(colored("*", color), end="")
        print("Do you want to see list of possible types of titles for films?", end="")
        print(colored("*", color))
        print(colored("*", color), end="")
        print("""If yes, enter "yes", in opther case press "Enter".            """, end="")
        print(colored("*", color))
        print(colored(
            "****************************************************************", color))
        print()
        print()
        print()
        while True:
            titles_lst_yes_no = input()
            print()
            if titles_lst_yes_no in ("yes", ""):
                break
            print("""Please, enter "yes" or press "Enter".""")
            print()
        if titles_lst_yes_no == "yes":
            print(titles_type)
        color = random.choice(color_list)
        print()
        print()
        print()
        print(colored(
            "****************************************************", color))
        print(colored("*", color), end="")
        print("Please, enter a film type you chose.              ", end="")
        print(colored("*", color))
        print(colored("*", color), end="")
        print("""If you want to see films of all types enter "all".""", end="")
        print(colored("*", color))
        print(colored(
            "****************************************************", color))
        print()
        print()
        print()
        while True:
            film_type = input()
            print()
            if film_type in titles_type:
                break
            if film_type == "all":
                break
            print("Please, enter a title type of a film.")
            print()
        if film_type == "all":
            read_file_tsv = read_file_tsv[read_file_tsv["titleType"].isin(
                titles_type)]
        else:
            read_file_tsv = read_file_tsv[read_file_tsv["titleType"] == film_type]
    return read_file_tsv
