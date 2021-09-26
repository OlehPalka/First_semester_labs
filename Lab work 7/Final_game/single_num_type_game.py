"""
This module contains 3 separate game modes,
with threetypes of numbers

"""

import random
from num_type_gen import *
import plot_lines

def main(difficulty, num_type, grid_size=10):
    """
    This function takes difficulty level and type of numbers, and based
    on the type of numbers the game mode will be started. If user wins the game mode,
    this function returns True, if not, it returns False.

    """

    valid_nums = num_type(*difficulty_ranges[difficulty]) #List of valid numbers based on difficulty

    invalid_grid = True
    score = 0

    #Main loop
    while score in range(0,10):

        #Grid gen
        if invalid_grid:
            grid = random.sample(range(*difficulty_ranges[difficulty]), grid_size-1)
            grid.insert(random.randint(0, grid_size), random.choice(valid_nums))
            invalid_grid = False

        print("Рахунок:", score)
        print(grid)

        veg_nums = {even_numbers:"картоплину", lucky_numbers:"морквину", numbers_Ulam:"помідор"}
        #Checks if user input is number, none, or exit
        usr_input = ""
        while not (usr_input.isnumeric() or usr_input in ("нема", "вийти")):
            usr_input = input(f"Викопай {veg_nums[num_type]}!(Якщо всю потрібну вже викопано, введи \"нема\"). Надоїло? Введи \"вийти\":")

        if usr_input=="нема":
            invalid_grid=True
            i=0

            while i<grid_size and invalid_grid:
                if grid[i] in valid_nums:
                    invalid_grid=False
                i+=1

            if invalid_grid:
                plot_lines.hprint("Переходимо на наступну грядку...")
            else:
                score-=1
                plot_lines.incorrect_num()

        elif usr_input=="вийти":
            return False

        else:
            usr_input = int(usr_input)

            if usr_input in grid and usr_input in valid_nums:
                score+=1
                plot_lines.correct_num()
                grid[grid.index(usr_input)] = "о"
                
            else:
                score-=1
                plot_lines.incorrect_num()
        
    #End message
    if score==10:
        return True

    return False
