"""
This is probably the hardest one out of these 6 small projects.
This will be similar to guessing the number, except we are guessing the word. The user needs to guess letters,
Give the user no more than 6 attempts for guessing wrong letter.
This will mean you will have to have a counter. You can download a ‘sowpods’ dictionary file or csv file
to use as a way to get a random word to use.
"""

import re
import random

# words1 = "Bottle".upper()
# words1 = "Dining Table in the kitchen".upper()

with open("Hangman_Words.txt", 'r') as rf:
    comp_words = rf.readlines()

    print("Computer chose a word...")
    words1 = random.choice(comp_words)


total_no_of_words = re.sub(r'\w', '_', words1.replace(" ", "/"))

total_no_of_words = list(total_no_of_words)[0:-1]  # [len(i) for i in words1.split()])
print(total_no_of_words)

hangman_dict = {
    1: """
--------
|      |
|      O
|
|
|
|
----------
""",
    2: """
    --------
|      |
|      O
|     |
|
|
|
----------
""",
    3: """
--------
|      |
|      O
|     | |
|
|
|
----------
""",
    4: """
--------
|      |
|      O
|     | |
|      |
|
|
----------
""",
    5: """
--------
|      |
|      O
|     | |
|      |
|     |
|
----------
""",
    6: """
--------
|      |
|      O
|     | |
|      |
|     | |
|
----------
"""
}

count = 0
winner_flag = True
correct_char_list = []
wrong_char_list = []
while count < 6:  # To give 6 wrong attempts
    user_input = input("Please enter your choice :: ").upper()
    for index, word in enumerate(words1):  # Iterate through the word
        if len(user_input) > 1:
            print("Please enter single character ... ")
            break
        if user_input == '':
            continue
        if user_input in words1:
            if user_input not in correct_char_list:  # Collect all valid chars in a list
                correct_char_list.append(user_input)  # Append correct chars in a list
            else:  # Inform user that char is already added
                print("Character already used... Please select new character \n")
                break

            get_index = [i for i, x in enumerate(words1) if x == user_input]  # This is to get all index of correct char
            for i in get_index:
                total_no_of_words[i] = user_input  # Modify total_no_of_words with guessed chars

            # print("HEREEEEEEEEEEE")
            # print(words1)
            # print("".join(total_no_of_words).replace("/", " ") + "\n")
            if "".join(total_no_of_words).replace("/", " ") + "\n" == words1:  # Verify if all words were guessed correctly
                count = 6
            break
        else:  # If user makes wrong guess
            wrong_char_list.append(user_input)  # Append correct chars in a list
            count += 1
            if count == 1:
                print(hangman_dict[count])
            elif count == 2:
                print(hangman_dict[count])
            elif count == 3:
                print(hangman_dict[count])
            elif count == 4:
                print(hangman_dict[count])
            elif count == 5:
                print(hangman_dict[count])
            elif count == 6:  # When all Wrong guesses are made
                print(hangman_dict[count])
                winner_flag = False
            break
    print(total_no_of_words)
    print(f"Correct characters chosen till now :: {correct_char_list}")
    print(f"Wrong characters chosen till now :: {wrong_char_list} \n")

if winner_flag:
    print("Congrats!! YOU WIN.......!!!!!!!")
else:
    print("YOU LOSE..!!!! :(")
    print(f'Word was -- {words1}')

