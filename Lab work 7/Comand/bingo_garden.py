import random
from num_type_gen import *

def generation_of_board():
    board_with_types = []
    for _ in range(3):
        types = ['U', 'L', 'E']
        random.shuffle(types)
        board_with_types.append(types)
    return board_with_types

def rules(number_of_rule):
    if number_of_rule == 1:
        print('Правила:')
        print('U - сорт картоплі "Число Улама" (Ulam number)')
        print('L - сорт картоплі "Вдале число" (Lucky number)')
        print('E - сорт картоплі "Парне число" (Even number)')
        print('Посади картоплю на правильній грядці.')
        print('Для цього посади картоплю на грядку(встав число на місце букви,')
        print('яка відповідає потрібному сорту (типу цього числа).')
        print('Як?')
        print('Просто введи координати цієї букви, де перша цифра - номер рядка, а друга - номер стовпчика.') 
        print('Приклад: 01')
        print('Якщо картопля(число) не підходить до жодної грядки(до жодного із запропонованих типів чисел),')
        print('залиш її першокурсникам, що прийдуть у наступному році(введи 0).')
    if number_of_rule == 2:
        print('Правила:')
        print('Ти побачиш номери кожної картоплини, яку треба пересадити та вказівку, куди пересадити.')
        print('Обери серед усіх картоплин(чисел) лише 3, які підходять для відповідного ряду.')
        print('Будь уважним. Кожну картоплину ти можеш пересадити рівно 1 раз.')
        print('Тому радимо завчасно прорахувати, як буде виглядати кожен ряд.')

def words_from_bingo_garden(number_of_phrase):
    if number_of_phrase == 1:
        print('Ця картоплина не мала рости тут. Ти програв.')
    if number_of_phrase == 2:
        print('На цій грядці вже росте картопля. Обери іншу, будь ласка.')
    if number_of_phrase == 3:
        print('Ехх, картопля в цьому році буде не по сортам рости. Але дякую за роботу!')
    if number_of_phrase == 4:
        print('Залишив картоплю для першачків, що прийдуть у наступному році?')
    if number_of_phrase == 5:
        print('Ти нічого не посадив... Дякую за роботу! Попрошу пересадити когось іншого.')
    if number_of_phrase == 6:
        print('Ти мав використовувати лише картоплю, що вже садив раніше.')
    if number_of_phrase == 7:
        print('Дякую за роботу! Попрошу когось іншого пересадити картоплю.')
    if number_of_phrase == 8:
        print("Гарно попрацював! Тепер твої грядки мають такий вигляд: ")


        

def replace_type_with_number(from_number, to_number):
    ulam_list = numbers_Ulam(from_number ,to_number)
    lucky_list = lucky_numbers(from_number ,to_number)
    even_list = even_numbers(from_number ,to_number)
    board = generation_of_board()
    rules(1)
    number_of_replacements = 0
    while True:
        print('    0    1    2')
        for one_line in range(len(board)):
            print(one_line, board[one_line])
        number = random.choice([random.choice(ulam_list), random.choice(lucky_list), random.choice(even_list)])
        print('Число(номер картоплини):', number)
        user_answer = input('Саджу на грядку: ')
        if user_answer in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
            user_answer = list(user_answer)
            patch = board[int(user_answer[0])][int(user_answer[1])]
            if patch == 'U':
                if number in ulam_list:
                    board[int(user_answer[0])][int(user_answer[1])] = number
                    number_of_replacements += 1
                else:
                    words_from_bingo_garden(1)
                    return
            elif patch == 'L':
                if number in lucky_list:
                    board[int(user_answer[0])][int(user_answer[1])] = number
                    number_of_replacements += 1
                else:
                    words_from_bingo_garden(1)
                    return
            elif patch == 'E':
                if number in even_list:
                    board[int(user_answer[0])][int(user_answer[1])] = number
                    number_of_replacements += 1
                else:
                    words_from_bingo_garden(1)
                    return
            else:
                words_from_bingo_garden(2)
            if number_of_replacements == 9:
                sorts_of_potato = ['Числа Улама', 'Вдалі числа', 'Парні числа']
                random.shuffle(sorts_of_potato)
                print('    0    1    2')
                for one_line in range(len(board)):
                    print(one_line, board[one_line])
                print(f'Молодець, ти посадив картоплю на всі грядки. Але чому вона посаджена в різнобій?\nВ одному \
ряду має бути картопля лише одного сорту.\nПересади її за такою схемою: \
у першому ряду посади картоплю сорту "{sorts_of_potato[0]}",\nу другому - \
сорту "{sorts_of_potato[1]}", у третьому - сорту "{sorts_of_potato[2]}".')
                continue_or_not = input('Пересадиш? Напиши "так" або "ні": ')
                if continue_or_not == 'так':
                    sort_one_line_one_type(sorts_of_potato, ulam_list, lucky_list, even_list, board)
                elif continue_or_not == 'ні':
                    words_from_bingo_garden(3)
                return
        else:
            words_from_bingo_garden(4)

def sort_one_line_one_type(sorts_of_potato, ulam_list, lucky_list, even_list, board):
    rules(2)
    types = []
    row = ['першого', 'другого', 'третього', 'першому', 'другому', 'третьому']
    for one_sort in sorts_of_potato:
        if one_sort == 'Числа Улама':
            types.append(ulam_list)
        elif one_sort == 'Вдалі числа':
            types.append(lucky_list)
        else:
            types.append(even_list)
    numbers_on_board = []
    for one_line in board:
        numbers_on_board.extend(one_line)
    new_board = []
    for i in range(3):
        print('Картопля, яку треба пересадити:', numbers_on_board)
        row_with_one_sort = input(f'Напиши через пробіл номери картоплі {row[i]} ряду (сорт "{sorts_of_potato[i]}"): ')
        if row_with_one_sort == '':
            words_from_bingo_garden(5)
            return
        row_with_one_sort = row_with_one_sort.split()
        for number_of_potato in range(len(row_with_one_sort)):
            row_with_one_sort[number_of_potato] = int(row_with_one_sort[number_of_potato])
        new_board.append(row_with_one_sort)
        check = True
        for potato in new_board[i]:
            if potato not in numbers_on_board:
                check = False
        if check == False:
            words_from_bingo_garden(6)
            words_from_bingo_garden(7)
            return
        check = True
        for potato in new_board[i]:
            if potato not in types[i]:
                check = False
        if check == False:
            print(f'Неправильно посадив, не вся картопля відповідає сорту "{sorts_of_potato[i]}".')
            words_from_bingo_garden(7)
            return
        else:
            for transplanted_potato in row_with_one_sort:
                numbers_on_board.remove(transplanted_potato)
            print(f'Молодець! Тепер у {row[i+3]} ряду лише картопля сорту "{sorts_of_potato[i]}".')
    words_from_bingo_garden(8)
    print('    0    1    2')
    for one_line in range(len(new_board)):
        print(one_line, new_board[one_line])

