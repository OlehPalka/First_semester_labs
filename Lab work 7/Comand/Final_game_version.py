import time, num_type_gen, plot_lines, all_num_types_game, single_num_type_game


def set_difficulty():

    difficulty = input("Вибери рівень складності:\n1 - простий\n2 - середній\n3 - складний\n")

    while difficulty not in ("1", "2", "3"):
        difficulty = input("Неправильне значення. Введіть число від 1 до 3\n")

    return int(difficulty)    


def main():
    plot_lines.vstup()
    plot_lines.study_begin()
    plot_lines.study_end()
    plot_lines.game_rules()
    plot_lines.game_start()

    while True:
        n = int(input("""Вибери режим гри:
        Введи 1, якщо хочеш вивчити парні числа
        Введи 2, якщо хочеш вивчити вдалі числа
        Введи 3, якщо хочеш вивчити числа Улама
        Введи 4, якщо хочеш перевірити  свої знання з усіх чисел
        Введи 5 якщо хочеш завершити гру
        """))

        if n == 1:
            difficulty = set_difficulty()
            
            plot_lines.even_numbers_start()

            won = single_num_type_game.main(difficulty, num_type_gen.even_numbers)

            if won:
                plot_lines.even_numbers_win()
            else:
                plot_lines.even_numbers_lose()

        elif n == 2:
            difficulty = set_difficulty()

            plot_lines.lucky_number_start()

            won = single_num_type_game.main(difficulty, num_type_gen.lucky_numbers)

            if won:
                plot_lines.lucky_number_win()
            else:
                plot_lines.lucky_number_lose()
                

        elif n == 3:
            difficulty = set_difficulty()

            plot_lines.ulam_number_start()

            won = single_num_type_game.main(difficulty, num_type_gen.numbers_Ulam)

            if won:
                plot_lines.ulam_number_win()
            else:
                plot_lines.ulam_number_lose()

        elif n == 4:
            difficulty = set_difficulty()

            plot_lines.all_numbers_start()
            all_num_types_game.main(difficulty)

        elif n == 5:
            print("Вітаємо, ти успішно пройшов усі потрібні тобі курси. До зустрічі 😊")
            return None

main()