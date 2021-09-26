"""
Function which returns words from dictionary
"""
import random
def generate_grid():
    """
    () -> list
    """
    alphabet = "абвгґджзеєиіїйклмнопрстуфхцчшщьюя"
    leters = list(alphabet)
    result = list()
    while True:
        counter = 0
        grid = random.choice(leters)
        for i in result:
            if i == grid:
                counter = 1
        if counter == 0:
            result.append(grid)
        if len(result) == 5:
            break
    return result

def get_words(file_open, letters):
    """
    (str, list) -> list()
    >>> print(get_words("base.lst", ['ь']))
    []
    """
    lst = []
    with open(file_open, 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(line)
    result = list()
    for i in lst:
        word_type = i.split(" ")
        try:
            if word_type[0][0] in letters:
                if ('/n' in word_type[1] or 'noun' in word_type[1]) and (len(word_type[0]) <= 5):
                    result.append((word_type[0], 'noun'))
                elif ('/v' in word_type[1] or 'verb' in word_type[1]) and (len(word_type[0]) <= 5):
                    result.append((word_type[0], "verb"))
                elif ('/adj' in word_type[1] or 'adj' in word_type[1]) and (len(word_type[0]) <= 5):
                    result.append((word_type[0], 'adjective'))
                elif 'adv' in word_type[1] and (len(word_type[0]) <= 5):
                    result.append((word_type[0], 'adverb'))
        except IndexError:
            word_type[0] = ""
    return result
print(get_words("base.lst", ['й', 'є', 'ю']))
def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    (list, str, list, list) -> list()
    >>> print(check_user_words([], "noun", [], get_words("base.lst", ["ь"])))
    ([], [])
        """
    rseult = list()
    for i in user_words:
        if i[0] in letters:
            rseult.append(i)
    list_of_true_words = list()
    for i in rseult:
        if (i, language_part) in dict_of_words:
            list_of_true_words.append(i)
            dict_of_words.remove((i, language_part))
    result_final = list()
    for i in dict_of_words:
        if i[1] == language_part:
            result_final.append(i[0])
    return list_of_true_words, result_final
