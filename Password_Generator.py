"""
Write a programme, which generates a random password for the user. Ask the user how long they want their
password to be, and how many letters and numbers they want in their password. Have a mix of
upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.
"""
import random
import string


class PasswordGenerator:
    def __str__(self):
        return "This is Password Generator Class"

    def test_decorator(func):
        def wrapper(*args):
            z = func(*args)
            return "".join(random.sample(z, len(z)))
        return wrapper

        # "".join(random.sample(password, len(password)))

    @test_decorator
    def generate_password(self):
        try:
            total_length = int(input("How long you want your Password to be ?  [Min - 6 character] :: "))
            if total_length < 6:
                return "The password should be a minimum of 6 characters long"
            char_length = int(input("How many letters you want in your password ? :: "))
            if char_length < 2:
                return "Please enter min. 2 characters as both upper and lower case are required in password"
            num_length = int(input("How many numbers you want in your password ? :: "))
            if num_length < 1:
                return "Please enter min 1 number, as number is mandatory in password"
        except:
            return "Inputs should be a number"

        if (char_length + num_length) > total_length:
            return f"Please make sure that (char + num) ia less than {total_length}"

        # Get random numbers
        total_numbers = random.sample(string.digits, num_length)  # This will give me random n numbers

        # Get random upper letters
        random_upper = random.randint(1, char_length - 1)
        total_upper_letters = random.sample(string.ascii_uppercase, random_upper)  # This will fetch me random CHARS

        # Get random lower letters
        remain = char_length - len(total_upper_letters)  # Remaining should be lower case
        total_lower_letters = random.sample(string.ascii_lowercase, remain)

        # Get random special characters
        spec_char = total_length - (char_length + num_length)
        if spec_char == 0:
            print("Since no space for special character, inserting from Computer")
            total_special_char = random.sample(string.punctuation, 1)
        else:
            total_special_char = random.sample(string.punctuation, spec_char)

        # Complete Password
        password = total_numbers + total_upper_letters + total_lower_letters + total_special_char
        print("***", password)
        return password
        # final_password = "".join(random.sample(password, len(password)))
        #
        # return final_password


if __name__ == '__main__':
    obj = PasswordGenerator()
    print(obj)
    print(obj.generate_password())





