import random
import test
from num_type_gen import *

def single_num_type_mode(difficulty, num_type, grid_size=10):
    difficulty_ranges = {
        1:(0,50),
        2:(50,200),
        3:(200,500)
    }
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

        print("score =", score)
        print(grid)

        #Checks if user input is number, none, or exit
        usr_input = ""
        while not (usr_input.isnumeric() or usr_input in ("none", "exit")):
            usr_input = input("Enter a number from the grid or none or exit...")

        if usr_input=="none":
            invalid_grid=True
            i=0

            while i<grid_size and invalid_grid:
                if grid[i] in valid_nums:
                    invalid_grid=False
                i+=1

            if invalid_grid:
                print(test.correct_num())
            else:
                score-=1
                print(test.incorrect_num)

        elif usr_input=="exit":
            return False

        else:
            usr_input = int(usr_input)

            if usr_input in grid and usr_input in valid_nums:
                score+=1
                print("Answer valid.")
                grid[grid.index(usr_input)] = "O"
                
            else:
                score-=1
                print("Answer invalid.")
        
    #End message
    if score==10:
        return True

    return False
