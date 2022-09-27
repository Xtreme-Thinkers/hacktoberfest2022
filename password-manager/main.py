from random import choice, shuffle


class PasswordManager:
    passwords = {}

    def __init__(self, first_name, last_name, age, site_name, keyword, key_char):
        self.user_symbols = None
        self.user_numbers = None
        self.user_letters = None
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.site_name = site_name
        self.keyword = keyword
        self.key_char = key_char

    def generate_password(self, user_letters, user_numbers, user_symbols):
        """
        Generates a random password.

        Parameters
        ----------
        :param user_letters: Number of letters to generate in the password.
        :param user_numbers: Number of numbers to generate in the password.
        :param user_symbols: Number of symbols to generate in the password.

        :return: Password as a string.
        """
        # To not take input from users generate_password function can have specific length of the password.
        self.user_letters = user_letters
        self.user_numbers = user_numbers
        self.user_symbols = user_symbols

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v',
                   'w', 'x', 'y', 'z', 'A', 'B',
                   'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                   'X',
                   'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # Specific length for password can be added here.
        p_letters = [choice(letters) for _ in range(0, user_letters)]
        p_symbols = [choice(symbols) for _ in range(0, user_symbols)]
        p_numbers = [choice(numbers) for _ in range(0, user_numbers)]
        pwd = p_letters + p_symbols + p_numbers
        shuffle(pwd)

        password = "".join(pwd)
        return password

    def show_password(self):
        pass

    def save_password(self):
        pass

    def find_password(self):
        pass

    def update_password(self):
        pass

    def delete_password(self):
        pass


if __name__ == "__main__":
    operation = input(
        "What you want to do?\n(create/update/delete/find Password)\n Just enter the commands (c/u/d/f)\n")
    first_name = input("Enter Your First Name:\n")
    last_name = input("\nEnter Your Last Name:\n")
    age = input("\nEnter Your age:\n")
    # write code to save the data in the users.json file
    site_name = input(
        "\nEnter the Site Name for which you need the password to be created and saved:\n")
    keyword = input(
        "\n Enter the Key Word that you want to identify the password with:\n")
    key_char = input("\nYour Unique Key Char for the Password")
    new_instance = PasswordManager(
        first_name, last_name, age, site_name, keyword, key_char)
    # ensure to create a new json file and store the data there if user is not available in users.json
    # else append the password directly to the user_name.json file with the key_char
    with open("save.txt", "a") as file:
        input_letters = int(input("How many letters do you want?\n"))
        input_symbols = int(input("How many symbols do you want?\n"))
        input_number = int(input("How many numbers do you want?\n"))
        # checks if users enters all inputs as 0.
        if input_letters != 0 and input_symbols != 0 and input_number != 0:
            user_password = new_instance.generate_password(input_letters, input_symbols, input_number)
            # shows the password latter show_password function can call it from json and show it if needed.
            print(f"Your password is: {user_password}")
            user_choice = input("Do you want to save it? y for yes and n for no.\n")
            correct_choice = False
            while not correct_choice:
                if user_choice == "y":
                    print("Saving...")
                    # saves the password in save.txt later a function can be called.
                    file.write(f"{user_password}\n")
                    print("Saved...")
                    correct_choice = True
                elif user_choice == "n":
                    print("Exiting...")
                    correct_choice = True
                else:
                    print("Wrong input...")
                    # continues to ask whether to save the password or not.
                    user_choice = input("Do you want to save it? y for yes and n for no.\n")
        else:
            # if all inputs are zero then no password is generated.
            print("No password generated...")
    # And after generate password save_password should be called and the respective saving operations
    # should be performed there.
    pass
