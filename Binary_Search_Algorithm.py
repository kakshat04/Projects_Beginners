"""
Create a random list of numbers between 0 and 100 with a difference of 2 between each number.
Ask the user for a number between 0 and 100 to check whether their number is in the list. The programme
should work like this. The programme will half the list of numbers and see whether the users number matches
the middle element in the list. If they do not match, the programme will check which half the number lies in,
and eliminate the other half. The search then continues on the remaining half, again checking whether the
 middle element in that half is equal to the user’s number. This process keeps on going until the programme
 finds the users number, or until the size of the subarray is 0, which means the users number isn't in the list.

If you are struggling with any of these, then feel free to message me, or just have a look online as there
are plenty of solutions available on platforms such as youtube.


Since question is not clear, I am making modifictions as per my understandings and to learn and implement Binary Search
Algorithm
"""

import random
import math
import time

random_num = random.randrange(0, 50)
print(f"Computer generated random list of {random_num} elements")
time.sleep(1)
generated_lst = []
for data in range(random_num):
    generated_lst.append(random.randrange(1, 100))
sorted_lst = sorted(list(set(generated_lst)))
print(sorted_lst)

# len_half = math.ceil(len(sorted_lst)/2)
len_half = len(sorted_lst) // 2

left_lst = sorted_lst[:len_half]
right_lst = sorted_lst[len_half:]
middle_number = sorted_lst[len_half]
print(middle_number)

user_input = int(input(f"Please enter number between {0, 100}"))

new_lst = []

if middle_number == user_input:
    print("Number in list")
else:
    while len(new_lst) != 1:
        if user_input == middle_number:
            break
        elif user_input < middle_number:
            new_lst = sorted_lst[:len_half]
            print("New List :: ", new_lst)
            # len_half = math.ceil(len(new_lst) / 2)
            len_half = len(new_lst) // 2
            try:
                middle_number = new_lst[len_half]
            except:
                break
            sorted_lst = new_lst
        elif user_input > middle_number:
            new_lst = sorted_lst[len_half:]
            print("New List :: ", new_lst)
            # len_half = math.ceil(len(new_lst) / 2)
            len_half = len(new_lst) // 2
            try:
                middle_number = new_lst[len_half]
            except:
                break
            sorted_lst = new_lst

if len(new_lst) == 1 and new_lst[0] == user_input:
    print("Number in list", new_lst)
elif len(new_lst) > 1:
    print("Number in list", new_lst)
else:
    print("Number not found")
