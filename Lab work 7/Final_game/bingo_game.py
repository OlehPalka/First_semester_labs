""" Game mode "Bingo" """
import random
from num_type_gen import *
import plot_lines

def generation_of_grid() -> list:
    """ Returns grid for game """
    grid_with_types = []
    for _ in range(3):
        types = ['U', 'L', 'E']
        random.shuffle(types)
        grid_with_types.append(types)
    return grid_with_types

def printing_of_grid(grid):
    """ prints grid """
    print('    0    1    2')
    for one_line in range(len(grid)):
        print(one_line, grid[one_line])
      

def replace_type_with_number(difficulty):
    """ The first part of the game is Bingo.
    The player must choose numbers of a certain type.
    """
    from_number, to_number = difficulty_ranges[difficulty]

    ulam_list = numbers_Ulam(from_number ,to_number)
    lucky_list = lucky_numbers(from_number ,to_number)
    even_list = even_numbers(from_number ,to_number)
    types = [ulam_list, lucky_list, even_list]
    patches = ['U', 'L', 'E']
    grid = generation_of_grid()
    plot_lines.rules(1)

    number_of_replacements = 0
    while True:
        printing_of_grid(grid)
        number = random.choice([random.choice(ulam_list), random.choice(lucky_list), random.choice(even_list)])
        print('Число(номер картоплини):', number)
        user_answer = input('Саджу на грядку: ')
        if user_answer in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
            user_answer = list(user_answer)
            patch = grid[int(user_answer[0])][int(user_answer[1])]
            if patch not in patches:
                plot_lines.words_from_bingo_garden(2)
                return
            for i in range(3):
                if patch == patches[i]:
                    if number in types[i]:
                        grid[int(user_answer[0])][int(user_answer[1])] = number
                        number_of_replacements += 1
                    else:
                        plot_lines.words_from_bingo_garden(1)
                        return
            if number_of_replacements == 9:
                sorts_of_potato = ['Числа Улама', 'Вдалі числа', 'Парні числа']
                printing_of_grid(grid)
                if ask_user_if_continue(sorts_of_potato) == 'так':
                    sort_one_line_one_type(sorts_of_potato, ulam_list, lucky_list, even_list, grid)
                    return
                else:
                    plot_lines.words_from_bingo_garden(3)
                    return
        else:
            plot_lines.words_from_bingo_garden(4)


def ask_user_if_continue(sorts_of_potato:list) -> str:
    """ Asks user if he wants he continue to play or not """ 
    random.shuffle(sorts_of_potato)
    print(f'Молодець, ти посадив картоплю на всі грядки. Але чому вона посаджена в різнобій?\nВ одному \
ряду має бути картопля лише одного сорту.\nПересади її за такою схемою: \
у першому ряду посади картоплю сорту "{sorts_of_potato[0]}",\nу другому - \
сорту "{sorts_of_potato[1]}", у третьому - сорту "{sorts_of_potato[2]}".')
    continue_or_not = ''
    while continue_or_not != 'так' and continue_or_not != 'ні':
        continue_or_not = input('Пересадиш? Напиши "так" або "ні": ')
    return continue_or_not


def sort_one_line_one_type(sorts_of_potato: list, ulam_list: list, lucky_list: list, even_list: list, grid: list):
    """ The second part of the game is Bingo (if the user decided to play further).
    Now the player needs to fill the game field in the correct order.
    """
    plot_lines.rules(2)
    types = []
    numbers_on_board = []
    row = ['першого', 'другого', 'третього', 'першому', 'другому', 'третьому']
    for one_sort in sorts_of_potato:
        if one_sort == 'Числа Улама':
            types.append(ulam_list)
        elif one_sort == 'Вдалі числа':
            types.append(lucky_list)
        else:
            types.append(even_list)
    for one_line in grid:
        numbers_on_board.extend(one_line)
    new_grid = []
    for i in range(3):
        print('Картопля, яку треба пересадити:', numbers_on_board)
        row_with_one_sort = input(f'Напиши через пробіл номери картоплі {row[i]} ряду (сорт "{sorts_of_potato[i]}"): ')
        try:
            row_with_one_sort = row_with_one_sort.split()
            for number_of_potato in range(len(row_with_one_sort)):
                row_with_one_sort[number_of_potato] = int(row_with_one_sort[number_of_potato])
            new_grid.append(row_with_one_sort)
        except ValueError:
            plot_lines.words_from_bingo_garden(5)
            return
        check = True
        for potato in new_grid[i]:
            if potato not in numbers_on_board:
                check = False
        if check == False:
            plot_lines.words_from_bingo_garden(6)
            plot_lines.words_from_bingo_garden(7)
            return
        check = True
        for potato in new_grid[i]:
            if potato not in types[i]:
                check = False
        if check == False:
            print(f'Неправильно посадив, не вся картопля відповідає сорту "{sorts_of_potato[i]}".')
            plot_lines.words_from_bingo_garden(7)
            return
        else:
            try:
                for transplanted_potato in row_with_one_sort:
                    numbers_on_board.remove(transplanted_potato)
            except ValueError:
                plot_lines.words_from_bingo_garden(5)
                return
            print(f'Молодець! Тепер у {row[i+3]} ряду лише картопля сорту "{sorts_of_potato[i]}".')
    plot_lines.words_from_bingo_garden(8)
    printing_of_grid(new_grid)
