"""
The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice.
When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer
you prefer — the number of sides on the die is up to you.) The program will print what that number is.
It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number
that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a
function that randomly grabs a number within that range and prints it.
Concepts to keep in mind:
"""

import random
import time


class DiceRolling:
    def __init__(self):
        pass

    def __str__(self):
        return "Object of Rolling Dice Class"

    def start_game(self):
        print("Welcome to Dice Rolling Game..")
        time.sleep(.5)
        dice_values_lst = [1, 2, 3, 4, 5, 6]
        dice_number = random.choice(dice_values_lst)
        print(f"Number is :: {dice_number}")
        time.sleep(.5)

        user_input = "YES"
        max_chances = 0
        while user_input == "YES":
            user_input = input("Do you want to try another time ? -- Yes/No :: ").upper()
            if user_input not in ["YES", "NO"]:
                return "Please enter in only Yes or No"
            elif max_chances == 4:
                return "Maximum Trials allowed are 5. Please run the program again for more trials"
            elif user_input == "YES":
                dice_number = random.choice(dice_values_lst)
                print(f"Number is :: {dice_number}")
                time.sleep(.5)
            max_chances += 1

        return "Thank you for playing.."


if __name__ == '__main__':
    dice_obj = DiceRolling()
    print(dice_obj)
    print(dice_obj.start_game())

