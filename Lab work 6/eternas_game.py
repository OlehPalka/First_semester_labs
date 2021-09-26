"""
This module creates a board and outputs all wining combinations
"""
def board_generation():
    """
    () -> list

    Generates a game board of 16 x 4 size, i.e. two dimensional list (array) of
    'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'],
          [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'],
          [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'],
          [0, 0, 'g', 'w']]

    """
    board = list()
    part_of_board = list()
    import random
    for i in range(16):
        i = 0
        part_of_board = list()
        for row_element in range(4):
            row_element = random.choice([i, 'g', 'w'])
            if row_element != 0:
                part_of_board.insert(-1, row_element)
            else:
                for other_case_of_row_element in range(4 - len(part_of_board)):
                    other_case_of_row_element = 0
                    part_of_board.insert(other_case_of_row_element, 0)
                break
        board.append(part_of_board)
    return board


def winning_combination(board):
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there
    is winning combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'],\
    [0, 0, 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'],\
    ['g', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'],\
    ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 0], [0, 0, 'g', 'g'],\
    [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0],\
    ['g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'],\
    ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'],\
    [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'],\
    [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0],\
    [0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0],\
    [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'],\
    [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'],\
    [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'],\
    [0, 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'],\
    ['w', 'g', 'w', 'g'], [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'],\
    ['g', 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'g'],\
    [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'],\
    ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'],\
    [0, 'w', 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'],\
    ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'w', 'g', 'w'],\
    [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 'w', 'w', 'w'], [0, 0, 0, 'w'],\
    [0, 'w', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'],\
    ['w', 'w', 'w', 'g'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w'],\
    [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 'g', 'w', 'g'],\
    ['g', 'g', 'w', 'g'], ['w', 'g', 'w', 'g']]) # doctest: +ELLIPSIS
    (True, [[(3, 11), (2, 12), (1, 13), (0, 14)],...(3, 8)]])
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0],\
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'],\
    ['w', 'w', 'g', 'g'], ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'],\
    [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 'g', 'w', 'w'],\
    [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([[0, 0, 'w', 'w'], [0, 0, 'w', 'w'],\
    ['g', 'g', 'g', 'w'], [0, 'w', 'g', 'g'], ['g', 'g', 'w', 'w'],\
    [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'g'],\
    [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 'w', 'w', 'w'], ['g', 'g', 'w', 'g'],\
    [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w']])
    (True, [[(3, 4), (3, 5), (3, 6), (3, 7)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'],\
    [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0],\
    [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'],\
    ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'],\
    ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']]) # doctest: +ELLIPSIS
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14),...(3, 2)]])
    """

    result = list()
    indexes = list()
    # check for coincedences in diagonals
    for i in range(16):
        list_of_true_combs = list()
        # chek if 4 itemes = each other
        if board[i][0] == board[(i + 1) % 16][1]\
        == board[(i + 2) % 16][2] == board[(i + 3) % 16][3]:
            #check if these itemes are not 0
            if board[i][0] !=  0:
                # add these itemes to result
                for row in range(4):
                    indexes.append(row)
                    indexes.append((row + i) % 16)
                    list_of_true_combs.append(tuple(indexes))
                    indexes = list()
                result.append(list_of_true_combs)


    indexes = list()
    # check for coincedences in diagonals
    for i in range(16):
        list_of_true_combs = list()
        # chek if 4 itemes = each other
        if board[i][3] == board[(i + 1) % 16][2]\
        == board[(i + 2) % 16][1] == board[(i + 3) % 16][0]:
        #check if these itemes are not 0
            if board[i][3] !=  0:
                # add these itemes to result
                for row in range(4):
                    indexes.append(3 - row)
                    indexes.append((row + i) % 16)
                    list_of_true_combs.append(tuple(indexes))
                    indexes = list()
                result.append(list_of_true_combs)

    list_of_true_combs = list()
    indexes = list()
    # check for coincedences in lines
    for pillar_meaning in range(4):
        for i in range(16):
            # chek if 4 itemes = each other
            list_of_true_combs = list()
            if board[i][pillar_meaning] == board[(1 + i) % 16][pillar_meaning]\
            == board[(2 + i) % 16][pillar_meaning] == board[(3 + i) % 16][pillar_meaning]:
            #check if these itemes are not 0
                if board[i % 16][pillar_meaning] != 0:
                    # add these itemes to result
                    for row in range(4):
                        indexes.append(pillar_meaning)
                        indexes.append((i + row) % 16)
                        list_of_true_combs.append(tuple(indexes))
                        indexes = list()
                    result.append(list_of_true_combs)



    list_of_true_combs = list()
    indexes = list()
    # check for coincedences in pillars
    for i in range(16):
        for row in range(3):
            # chek if 4 itemes = each other
            if board[i][row] == board[i][row + 1]:
                #check if these itemes are not 0
                if board[i][row] != 0:
                    # add these itemes to result
                    indexes = list()
                    indexes.append(row)
                    indexes.append(i)
                    list_of_true_combs.append(tuple(indexes))
                    if row == 2:
                        indexes = list()
                        indexes.append(row + 1)
                        indexes.append(i)

                        list_of_true_combs.append(tuple(indexes))
                else:
                    break
            else:
                break
        if len(list_of_true_combs) == 4:
            result.append(list_of_true_combs)
        list_of_true_combs = list()
    if len(result) == 0:
        final_result = False
    else:
        final_result = (True, result)
    return final_result
