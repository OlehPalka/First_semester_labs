"""

"""

def read_crossword(path: str) -> list:
    """ Return list of tuples with crossword letters and it's positions

    >>> read_crossword('crossword_1_1.txt')
    [('c', (5, 1)), ('c', (6, 0)), ('u', (6, 1)), ('u', (2, 1)), ... ]
    """
    result = list()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = [line]
            line  = line[]
            result.append(line)
    return result
print(read_crossword('crossword_1_1.txt'))
def crossword_words(crossword: list) -> list:
    """ Return list of crossword words

    >>> crossword_words(crossword)
    ['cud', 'embog', 'embox', 'sri', 'tra', 'lubza', 'embus', 'cue']
    """
    pass


if __name__ == "__main__":
    crossword = read_crossword('crossword_1_1.txt')
    print(crossword_words(crossword))
