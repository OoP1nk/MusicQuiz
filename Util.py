# ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░░██████╗░██╗░░░██╗██╗███████╗
# ████╗░████║██║░░░██║██╔════╝██║██╔══██╗██╔═══██╗██║░░░██║██║╚════██║
# ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝██║██╗██║██║░░░██║██║░░███╔═╝
# ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗╚██████╔╝██║░░░██║██║██╔══╝░░
# ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝░╚═██╔═╝░╚██████╔╝██║███████╗
# ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝

import json
import random

# Select a random song from storage.json
def getRandomSong():
    # Applys storage.json file to variable
    with open('storage/storage.json') as file:
        data = json.load(file)
    # Creates new array
    items = []
    # Loops through all the songs and add a seperator to seperate song/artist
    for (key, value) in data.items():
        items.append((key + "/" + value))
    # Randomise an integer
    index = random.randint(0, 21)
    # Gets the song artist
    songArtist = items[index]
    # Splits the songArtist where there is a '/'
    output = songArtist.split('/')
    return output


def getTitle(value):
    # ---------
    # 0 = Correct
    # 1 = Incorrect
    # 2 = Login
    # 3 = Register
    # ---------
    if value == 0:
        print('▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ▀▀█▀▀ ')
        print('▒█░░░ ▒█░░▒█ ▒█▄▄▀ ▒█▄▄▀ ▒█▀▀▀ ▒█░░░ ░▒█░░ ')
        print('▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄█ ░▒█░░')
    elif value == 1:
        print('▀█▀ ░█▄─░█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ ▀▀█▀▀ ')
        print('░█─ ░█░█░█ ░█─── ░█──░█ ░█▄▄▀ ░█▄▄▀ ░█▀▀▀ ░█─── ─░█── ')
        print('▄█▄ ░█──▀█ ░█▄▄█ ░█▄▄▄█ ░█─░█ ░█─░█ ░█▄▄▄ ░█▄▄█ ─░█──')
    elif value == 2:
        print('████████████████▀█████████████')
        print('█▄─▄███─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█')
        print('██─██▀█─██─█─██▄─██─███─█▄▀─██')
        print('▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀')
    elif value == 3:
        print('█████████████████▀█████████████████████████████')
        print('█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█')
        print('██─▄─▄██─▄█▀█─██▄─██─██▄▄▄▄─███─████─▄█▀██─▄─▄█')
        print('▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀')
    else:
        print("Invalid title input! Please try again.")
