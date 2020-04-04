"""
Make a rock-paper-scissors game where it is the player vs the computer.
The computer’s answer will be randomly generated, while the program will ask the user for their input.
This project will better your understanding of while loops and if statements.
"""
import random
import time


class RockPaperScissorGame:
    def __str__(self):
        return "This is Rock Paper Scissor Game"

    def new_game(self):
        try:
            input_trails = int(input("Enter number of Trials for the game(1-5) :: "))
        except:
            return "Number of Trials should be an integer,  Moron !!"

        if not 1 <= input_trails <= 5:
            return "Maximum trails should be in range 1-5"

        comp_choices = ['Rock', 'Paper', 'Scissors']
        total_trials = 0
        comp_won = 0
        user_won = 0

        while total_trials < input_trails:
            user_choice = input(f"Enter {total_trials + 1} number trial :: ")
            if not user_choice.isalpha() or user_choice.upper() not in [data.upper() for data in comp_choices]:
                return f"User Input should be between {comp_choices} "

            time.sleep(1)
            comp_choice = random.choice(comp_choices)
            print(f"Computer Chose {comp_choice}")
            time.sleep(0.5)

            if comp_choice.upper() == user_choice.upper():
                print("Strange..!! Both chose same option... Try again")
            elif comp_choice.upper() == 'ROCK' and user_choice.upper() == "PAPER":
                user_won += 1
                print(f"Congratulations !!, you one {total_trials} game")
                print(f'Total Score is \n Comp - {comp_won} : User - {user_won}')
            elif comp_choice.upper() == 'PAPER' and user_choice.upper() == "SCISSOR":
                user_won += 1
                print(f"Congratulations !!, you one {total_trials} game")
                print(f'Total Score is \n Comp - {comp_won} : User - {user_won}')
            elif comp_choice.upper() == 'SCISSOR' and user_choice.upper() == "ROCK":
                user_won += 1
                print(f"Congratulations !!, you one {total_trials} game")
                print(f'Total Score is \n Comp - {comp_won} : User - {user_won}')
            else:
                comp_won += 1
                print(f"Ooo... you lost {total_trials} game")
                print(f'Total Score is \n Comp - {comp_won} : User - {user_won}')

            total_trials += 1

        if comp_won > user_won:
            return f"Computer WON.... Better luck next time \n Final Score - Comp - {comp_won} : User - {user_won}' "
        elif comp_won < user_won:
            return f"Congratulations... YOU WIN \n Final Score - Comp - {comp_won} : User - {user_won}' "
        else:
            return f"Match Tied..  \n Final Score - Comp - {comp_won} : User - {user_won}' "

        # if comp_won > user_won:
        #     return f"Computer WON.... Better luck next time \n Final Score - Comp - {comp_won} : User - {user_won}' "
        # elif comp_won < user_won:
        #     return f"Congratulations... YOU WIN \n Final Score - Comp - {comp_won} : User - {user_won}' "
        # else:
        #     return f"Match Tied..  \n Final Score - Comp - {comp_won} : User - {user_won}' "


if __name__ == '__main__':
    game = RockPaperScissorGame()
    print(game)
    print(game.new_game())