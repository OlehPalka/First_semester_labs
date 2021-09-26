import random
import test
from num_type_gen import *
def numbers_Ulam(from_number ,to_number):
    if to_number <= 0:
        return None
    if to_number == 1:
        Ulam_numbers = [1]
    else:
        Ulam_numbers = [1, 2]
        while Ulam_numbers[-1] <= to_number:
            numbers_to_check = []
            for first_number in range(len(Ulam_numbers)-1):
                for second_number in range(first_number+1, len(Ulam_numbers)):
                    numbers_to_check.append(Ulam_numbers[first_number] + Ulam_numbers[second_number])
                    numbers_to_check.sort()
            check = True
            for number in numbers_to_check:
                if check:
                    if numbers_to_check.count(number) == 1 and number > Ulam_numbers[-1]:
                        Ulam_numbers.append(number)
                        check = False
    Ulam_numbers = Ulam_numbers[:-1]
    for number in Ulam_numbers:
        if number >= from_number:
            index_from = Ulam_numbers.index(number)
            break    
    return Ulam_numbers[index_from:]

def lucky_numbers(from_number ,to_number):
    numbers = list(range(1, to_number+1))
    step = 1
    if len(numbers) > 1:
        del numbers[step::numbers[step]]
        while numbers[step-1] < len(numbers):
            del numbers[numbers[step]-1::numbers[step]]
            step += 1
    for number in numbers:
        if number >= from_number:
            index_from = numbers.index(number)
            break 
    return numbers[index_from:]

def even_numbers(from_number ,to_number):
    even = []
    if from_number%2 == 0:
        for i in range(from_number, to_number, 2):
            even.append(i)
    else:
        for i in range(from_number+1, to_number, 2):
            even.append(i)
    return even

def generation_of_numbers(from_number ,to_number):
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

def game_with_all_numbers(from_number ,to_number):
    ulam = numbers_Ulam(from_number ,to_number)
    lucky = lucky_numbers(from_number ,to_number)
    even = even_numbers(from_number ,to_number)
    types = [ulam, lucky, even]
    score = 0
    output_numbers = generation_of_numbers(from_number ,to_number)
    while output_numbers != ['o']*10:
        for one_type in types:
            check = False
            for number in output_numbers:
                if number in one_type:
                    check = True
            if check == False:
                types.remove(one_type)
        type_of_number = random.choice(types)
        if type_of_number == ulam:
            print('Обери число Улама серед запропонованих:')
        elif type_of_number == lucky:
            print('Обери вдале число серед запропонованих:')
        elif type_of_number == even:
            print('Обери парне число серед запропонованих:')
        print(output_numbers)
        answer_of_user = input('Відповідь:\n')

        if int(answer_of_user) in type_of_number:
            score += 1
            print('Правильно, +1 бал')
        else:
            score -= 1
            print('Неправильно. -1 бал')

        if int(answer_of_user) in output_numbers:
            output_numbers[output_numbers.index(int(answer_of_user))] = 'o'
        else:
            print('Даного числа немає у списку запропонованих.')

        if score < 0:
            print('Ви програли. Гра завершена.')
            return
    print(output_numbers)
    print('Ви виграли. Ваша кількість балів:', score)




