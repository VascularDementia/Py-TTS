import subprocess
import pyttsx3
import sys
import os

def color():
    subprocess.call("color a" if os.name == 'nt' else " ", shell=True)

def cls():
    subprocess.call("cls" if os.name == 'nt' else "clear", shell=True)

def title():
    print("====================")
    print("=        TTS       =")
    print("====================")
    print("| 'cls' to clear   |")
    print("|   ^C to exit     |")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tts():
    while True:
        usrInput = input("Write: ")
        if usrInput != "cls":
            speak(usrInput)
        elif usrInput == "cls":
            cls()
            title()

def main():
    color()
    cls()
    title()
    tts()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

