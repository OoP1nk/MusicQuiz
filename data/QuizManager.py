# ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░░██████╗░██╗░░░██╗██╗███████╗
# ████╗░████║██║░░░██║██╔════╝██║██╔══██╗██╔═══██╗██║░░░██║██║╚════██║
# ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝██║██╗██║██║░░░██║██║░░███╔═╝
# ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗╚██████╔╝██║░░░██║██║██╔══╝░░
# ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝░╚═██╔═╝░╚██████╔╝██║███████╗
# ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝

# IMPORTS
from time import *
from Util import *
import os


def start(user):
    # Initialise score variable
    score = 0
    # Loop infinitely
    while True:
        # Gets random song from Utils file
        randomSong = getRandomSong()
        # Creates the variables (song letters and gets artist)
        song = randomSong[0]
        artist = randomSong[1]
        songWords = song.split(' ')
        songArray = []
        for word in songWords:
            songArray.append(word[0])
        songLtr = ''.join(songArray)
        # Add spaces between questions to clear the console
        cls()
        # Outputted data
        print(f"*Score: {score}")
        ans = str(input(f"What song is '{songLtr.upper()}' while the artist is {artist}: "))
        # Checks answer and adds scores
        score = checkAnswer(ans, song, score, user)


def checkAnswer(answer, song, score, user):
    # Checks if the answer is correct and handles second chance
    if answer.lower() == song.lower():
        getTitle(0)
        score += 3
        sleep(3)
    else:
        getTitle(1)
        ans = str(input("Please try again: "))
        if ans.lower() == song.lower():
            getTitle(0)
            score += 1
        else:
            getTitle(4)
            endQuiz(user, score)
        sleep(3)
    return score


def endQuiz(user, score):
    # Apply users.json to variable
    with open('storage/users.json') as file:
        data = json.load(file)
    # Checks if the user exists and updates the users score
    if data[f"{user.lower()}"]:
        data[f"{user.lower()}"] = {
            "name": data[f"{user.lower()}"]["name"],
            "surname": data[f"{user.lower()}"]["surname"],
            "password": data[f"{user.lower()}"]["password"],
            "lastScore": score
        }
    # Removes user.json file to append new data
    os.remove('storage/users.json')
    # Dumps the new data in users.json
    with open('storage/users.json', "a+") as file:
        json.dump(data, file)
    cls()
    # Gets the leaderboard
    getLeaderboard()
    print(f"Quiz has ended! Thanks for playing {user}")
    exit()


def getLeaderboard():
    # Apply users.json to variable
    with open('storage/users.json') as file:
        data = json.load(file)
    # Creates empty array
    scores = []
    # Loops through all users and adds their score to the array
    for user in data:
        userScore = data[f"{user}"]["lastScore"]
        scores.append(f"{userScore} - {user}")
    # Sorts the array
    scores.sort()
    num = 1
    index = 0
    print("Current Leaderboard")
    # Prints out the first 5 indexes in array
    while index < 5:
        try:
            print(f"{num}. {scores[index]}")
        except IndexError:
            print(f"{num}. No score found")
        # Increments so it doesn't infinitely loop
        num += 1
        index += 1


# Seperator function
def cls():
    print("\n" * 1)
