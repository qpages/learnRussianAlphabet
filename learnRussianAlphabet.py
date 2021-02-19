from time import sleep
from os import listdir
from os.path import isfile, join
import os
import vlc
import random

path = ""
lettersPath = [f for f in listdir("audio") if isfile(join("audio", f))]

def getUppercaseLetter(str):
    return str.split('.')[0].split('-')[1][0]

def getLowercaseLetter(str):
    return str.split('.')[0].split('-')[1][-1]

def playLetter(path):
    Instance = vlc.Instance('--fullscreen')
    player = Instance.media_player_new()
    Media = Instance.media_new(path)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(1)

def getRandomLetter():
    return random.choice(lettersPath)

def main():
    train = 0
    score = 0
    play = 1
    while (play):
        sleep(1.5)
        os.system('clear')  # For Linux/OS X
        train += 1
        letterPath = getRandomLetter()
        playLetter("audio/" + letterPath)
        userInput = input("Enter the corresponding letter: ")
        if userInput == getUppercaseLetter(letterPath):
            score += 1
            print("Good!")
        elif userInput == "q":
            play = 0
        else:
            print("Wrong, it was: " + getUppercaseLetter(letterPath))
    print("----------")
    print("You passed " + str(score) + " letters")
    print("You failed " + str(train - score) + " letters")
    print("Success rate: " + str(round((score / train) * 100, 2)))

main()