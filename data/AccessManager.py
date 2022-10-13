# ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░░██████╗░██╗░░░██╗██╗███████╗
# ████╗░████║██║░░░██║██╔════╝██║██╔══██╗██╔═══██╗██║░░░██║██║╚════██║
# ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝██║██╗██║██║░░░██║██║░░███╔═╝
# ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗╚██████╔╝██║░░░██║██║██╔══╝░░
# ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝░╚═██╔═╝░╚██████╔╝██║███████╗
# ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝

# IMPORTS
from data.QuizManager import *
from data.StorageManager import *
import os


def authorize():
    # Gets specified title from Utils file
    getTitle(2)
    if getStorageProvider() == 'JSON':
        # Needed variables to login
        username = str(input("What is your username?\n"))
        password = str(input("What is your password?\n"))
        # Added json object in users.json into data variable
        with open('storage/users.json') as file:
            data = json.load(file)
        # Checks if the user exists
        if data[str(username.lower())] and data[str(username.lower())]['password'] == password:
            print(f"Access granted! Welcome {username}")
            start(username)
        else:
            # Incorrect information/user does not exist
            print("Access denied! Please try again later.")
    elif getStorageProvider() == 'MYSQL':
        return
    else:
        # Unexpected error handler
        print('Unexpected error occurred while authorizing user!')


def register():
    # Gets specified title from Utils file
    getTitle(3)
    if getStorageProvider() == 'JSON':
        # Variables
        firstName = str(input("What is your first name?\n"))
        lastName = str(input("What is you last name?\n"))
        password = str(input("Password: "))
        RTPassword = str(input("Re-type Password: "))
        # Checks if passwords are the same
        if password != RTPassword: return exit()
        # Applys users.json to variable
        with open('storage/users.json') as file:
            data = json.load(file)
        # Creates new user
        username = firstName[0] + firstName[1] + lastName[::-1][0]
        data[f"{username.lower()}"] = {
            "name": firstName,
            "surname": lastName,
            "password": password,
            "lastScore": NULL,
        }
        # Removes users.json file to append new data
        os.remove('storage/users.json')
        # Open file and dump the new data
        with open('storage/users.json', 'a+') as file:
            json.dump(data, file)
        print(f"Your username is {username}")
        # Run authorize function to login new user
        authorize()
    elif getStorageProvider() == 'MYSQL':
        return
    else:
        # Unexpected error handler
        print('An unexpected error occurred while registering this user!')
