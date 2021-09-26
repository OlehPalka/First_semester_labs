"""
Game for studying Even numbers, Ulam numbers and Lucky numbers
"""
import num_type_gen, plot_lines, all_num_types_game, single_num_type_game, bingo_game

def set_difficulty():
    """
    () -> int
    This function sets dificulty level.
    """

    difficulty = input("Вибери рівень складності:\n1 - простий\n2 - середній\n3 - складний\n")

    while difficulty not in ("1", "2", "3"):
        difficulty = input("Неправильне значення. Введіть число від 1 до 3\n")

    return int(difficulty)

def main():
    """
    This function is completed game.
    It has 5 mods, which you can chose.
    """
    plot_lines.vstup()
    plot_lines.study_begin()
    plot_lines.study_end()
    plot_lines.game_rules()
    plot_lines.game_start()

    while True:
        mod = int(input("""Вибери режим гри:
        Введи 1, якщо хочеш вивчити парні числа
        Введи 2, якщо хочеш вивчити вдалі числа
        Введи 3, якщо хочеш вивчити числа Улама
        Введи 4, якщо хочеш перевірити  свої знання з усіх чисел
        Введи 5, якщо хочеш зіграти у гру bingo
        Введи 6, якщо хочеш завершити гру
        """))

        if mod == 1: # even numbers mod
            difficulty = set_difficulty()

            plot_lines.even_numbers_start()

            won = single_num_type_game.main(difficulty, num_type_gen.even_numbers)

            if won:
                plot_lines.even_numbers_win()
            else:
                plot_lines.even_numbers_lose()

        elif mod == 2: # lucky numbers mod
            difficulty = set_difficulty()

            plot_lines.lucky_number_start()

            won = single_num_type_game.main(difficulty, num_type_gen.lucky_numbers)

            if won:
                plot_lines.lucky_number_win()
            else:
                plot_lines.lucky_number_lose()

        elif mod == 3: # ulam numbers mod
            difficulty = set_difficulty()

            plot_lines.ulam_number_start()

            won = single_num_type_game.main(difficulty, num_type_gen.numbers_Ulam)

            if won:
                plot_lines.ulam_number_win()
            else:
                plot_lines.ulam_number_lose()

        elif mod == 4: # all numbers mod
            difficulty = set_difficulty()

            plot_lines.all_numbers_start()
            all_num_types_game.main(difficulty)

        elif mod == 5: # bingo (all numbers) mod
            difficulty = set_difficulty()

            bingo_game.replace_type_with_number(difficulty)

        elif mod == 6: # exit
            print("Вітаємо, ти успішно пройшов усі потрібні тобі курси. До зустрічі 😊")
            return None

main()
