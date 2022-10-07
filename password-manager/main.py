from random import choice, shuffle
import json


class PasswordManager:
    passwords = {}

    def __init__(self):
        self.user_symbols = None
        self.user_numbers = None
        self.user_letters = None
        self.first_name = None
        self.last_name = None
        self.age = None
        self.site_name = None
        self.keyword = None
        self.key_char = None

    def create_user(self, first_name, last_name, age, site_name, keyword, key_char):
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

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v',
                   'w', 'x', 'y', 'z', 'A', 'B',
                   'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                   'W',
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

    def save_password(self, password):
        self.password = password
        new_data = {
            self.site_name: {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                "keyword": self.keyword,
                "key_char": self.key_char,
                "password": self.password,
            }
        }
        if len(self.first_name) == 0 or len(password) == 0:
            print("Please make sure your name and password is filled.")

        else:
            print(
                f"These are the details entered:\nEmail: {self.first_name} \nPassword: {password} \nIs it okay to save?")
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.JSONDecodeError:
                data = dict()

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

    def find_password(self, site_name_value):
        self.site_name_value = site_name_value
        if len(self.site_name_value) == 0:
            print("Make sure your site_name is filled!")
        else:
            try:
                with open("data.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("No data file found")
            else:
                if self.site_name_value in data:
                    name = data[self.site_name_value]["first_name"]
                    password = data[self.site_name_value]["password"]
                    print(f"First name: {name} \nPassword: {password}")
                else:
                    print(f"No details for {self.site_name_value} exists.")

    def update_password(self, site_name_value):
        self.site_name_value = site_name_value
        if len(self.site_name_value) == 0:
            print("Make sure your site_name is filled!")
        else:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                print("No data file found")
            else:
                if self.site_name_value in data:
                    name = data[self.site_name_value]["first_name"]
                    password = data[self.site_name_value]["password"]
                    letters = int(input("\nHow many letters do you want?\n"))
                    symbols = int(input("How many symbols do you want?\n"))
                    number = int(input("How many numbers do you want?\n"))
                    if letters != 0 and symbols != 0 and number != 0:
                        new_password = self.generate_password(letters, symbols, number)
                        print(f"Password for: {name} was: {password}")
                        with open("data.json", "r") as a_file:
                            json_object = json.load(a_file)
                        # print(json_object)
                        json_object[self.site_name_value]["password"] = new_password
                        print(f"New password for: {name} is: {new_password}")
                        with open("data.json", "w") as a_file:
                            json.dump(json_object, a_file,indent=4)
                    else:
                        # if all inputs are zero then no password is generated.
                        print("No new password generated...")
                else:
                    print(f"No details for {self.site_name_value} exists.")

    def delete_password(self):
        pass


if __name__ == "__main__":
    commands = ["c", "u", "d", "f", "q"]
    ask = True
    while ask:
        operation = input(
            "What you want to do?\n(create/update/delete/find Password)\nJust enter the commands (c/u/d/f)\n")

        if operation not in commands:
            print("Wrong argument.......\n")
        if operation == "c":
            first_name = input("Enter Your First Name:\n")
            last_name = input("\nEnter Your Last Name:\n")
            age = input("\nEnter Your age:\n")
            # write code to save the data in the users.json file
            site_name = input(
                "\nEnter the Site Name for which you need the password to be created and saved:\n")
            keyword = input(
                "\nEnter the Key Word that you want to identify the password with:\n")
            key_char = input("\nYour Unique Key Char for the Password:\n")
            new_instance = PasswordManager()
            new_instance.create_user(first_name, last_name, age, site_name, keyword, key_char)
            # ensure to create a new json file and store the data there if user is not available in users.json
            # else append the password directly to the user_name.json file with the key_char
            input_letters = int(input("\nHow many letters do you want?\n"))
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
                        new_instance.save_password(user_password)
                        print("Saved...\n")
                        correct_choice = True
                    elif user_choice == "n":
                        print("Exiting...\n")
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
        if operation == 'f':
            find_password = (input("Find password (y/n)?\n"))
            if find_password == 'y':
                site_name = (input("password for?\n"))
                new_instance = PasswordManager()
                new_instance.find_password(site_name)
                print()
            else:
                print("................................\n")
        if operation == 'u':
            update_password = (input("Update password (y/n)?\n"))
            if update_password == 'y':
                site_name = (input("password for?\n"))
                new_instance = PasswordManager()
                new_instance.update_password(site_name)
                print()
            else:
                print("................................\n")
        if operation == 'q':
            break
