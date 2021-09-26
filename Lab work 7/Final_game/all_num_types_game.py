"""
This module is a game mode, in which all types of numbers
are combined together.

"""
import random
from num_type_gen import *
from plot_lines import correct_num
from plot_lines import incorrect_num

def generation_of_numbers(from_number, to_number):
    """
    This function generates a grid with all types of numbers
    and returns a grid.

    >>> random.seed(1)
    >>> generation_of_numbers(0, 20)
    [1, 8, 0, 14, 6, 12, 18, 20, 2, 9]

    """
    numbers = []
    for _ in range(random.randint(1, 5)):
        special_number = random.choice(numbers_Ulam(from_number ,to_number))
        if special_number not in numbers:
            numbers.append(special_number)
    for _ in range(random.randint(1, 5)):
        special_number = random.choice(lucky_numbers(from_number ,to_number))
        if special_number not in numbers:
            numbers.append(special_number)
    while len(numbers) != 10:
        special_number = random.choice(even_numbers(from_number ,to_number))
        if special_number not in numbers:
            numbers.append(special_number)
    random.shuffle(numbers)
    return numbers

def control_presence_of_types(types, output_numbers):
    """
    This function checks if proposed numbers in output_numbers are
    Ulam, Lucky or even, if in output_numbers one type of numbers is
    not present, it's type will be deleted from types lst, so the user will not be asked to
    input number with that type.

    """
    for one_type in types:
        check = False
        for number in output_numbers:
            if number in one_type:
                check = True
        if not check:
            types.remove(one_type)
    return types

def ask_user_to_choose_number(type_of_number, ulam, lucky, even, output_numbers):
    """
    This function takas randomly generated type of number from type_of_number lst,
    prints an instruction which number to enter and asks user to enter a specific number.

    """
    if type_of_number == ulam:
        print('Обери число Улама серед запропонованих:')
    elif type_of_number == lucky:
        print('Обери вдале число серед запропонованих:')
    elif type_of_number == even:
        print('Обери парне число серед запропонованих:')
    print(output_numbers)
    answer_of_user = input('Відповідь:\n')
    return answer_of_user

def check_user_answer(answer_of_user, type_of_number, output_numbers, score):
    """
    This function checks user's input number and checks if it is present in a grid
    and if it is, the value of a number in the grid will be changed to 'o'.
    If user's input is correct user's score = score + 1
    If user's input is incorrect user's score = score - 1

    """
    if int(answer_of_user) in type_of_number:
        score += 1
        correct_num()
    else:
        score -= 1
        incorrect_num()

    if int(answer_of_user) in output_numbers:
        output_numbers[output_numbers.index(int(answer_of_user))] = 'o'
        return score
    print('Даного числа немає у списку запропонованих.')
    return score

def main(difficulty):
    """
    This function is a game mode, it contains all upper functions. The game will
    not end until grid will be filled with 10 'o' or if user's score will be less than 0.

    """
    from_number, to_number = difficulty_ranges[difficulty]

    ulam = numbers_Ulam(from_number ,to_number)
    lucky = lucky_numbers(from_number ,to_number)
    even = even_numbers(from_number ,to_number)
    types = [ulam, lucky, even]

    score = 0
    output_numbers = generation_of_numbers(from_number ,to_number)
    while output_numbers != ['o']*10:
        types = control_presence_of_types(types, output_numbers)
        type_of_number = random.choice(types)
        answer_of_user = ask_user_to_choose_number(type_of_number, ulam, lucky, even, output_numbers)
        score = check_user_answer(answer_of_user, type_of_number, output_numbers, score)
        print("Рахунок:", score)
        if score < 0:
            print('Ви програли. Гра завершена.')
            return

    print(output_numbers)
    print('Ви виграли. Ваша кількість балів:', score)
