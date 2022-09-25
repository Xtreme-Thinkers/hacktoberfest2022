import random


class PasswordManager:
    passwords = {}

    def __init__(self, first_name, last_name, age, site_name, keyword, key_char):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.site_name = site_name
        self.keyword = keyword
        self.key_char = key_char

    def generate_password(self):
        """helps to create Password"""
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
    site_name = input(
        "\nEnter the Site Name for which you need the password to be created and saved:\n")
    keyword = input(
        "\n Enter the Key Word that you want to identify the password with:\n")
    key_char = input("\nYour Unique Key Char for the Password")
    new_instance = PasswordManager(
        first_name, last_name, age, site_name, keyword, key_char)
    pass
