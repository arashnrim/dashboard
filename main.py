import os
import subprocess
import sys
from configparser import ConfigParser
from datetime import datetime
from time import sleep

from styles import Style

# Checks if the user is running the program in IDLE — due to its limitations, the program will reject running on IDLE.
if "idlelib" in sys.modules:
    print("\nPlease run this program from the Terminal instead of IDLE.\n")
    sys.exit()

# Checks if the user has configured the dashboard by use by detecting the presence of a config.ini file in the project
# root directory.
if not (os.path.exists("{}/config.ini".format(os.path.dirname(os.path.abspath(__file__))))):
    # noinspection PyUnresolvedReferences
    import configure

config = ConfigParser()
config.read("config.ini")
name = config.get("DEFAULT", "name")
time = datetime.now().hour
phrase = ""

if time < 12:
    phrase = "morning"
elif 12 <= time < 17:
    phrase = "afternoon"
elif time >= 18:
    phrase = "evening"

activities = [
    "Get the latest news",
    "Get weather information",
    "Manage your tasks",
]

showPrompt = True
while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c\n'")

    if name:
        print("Good {}, {}!".format(phrase, name))
    else:
        print("Good {}!".format(phrase))

    if showPrompt:
        print("{blue}?{end} {bold}What would you like to do?{end}".format(blue=Style.BLUE, end=Style.END,
                                                                          bold=Style.BOLD))
        for index, activity in enumerate(activities):
            print("{bold}{index}{end} {activity}".format(bold=Style.BLUE, index=index + 1, end=Style.END,
                                                         activity=activity))
        print()

    request = input(
        "Enter a number from 1 to {} or enter q to quit: ".format(len(activities)))

    # Receives the user's input which is either a numeric value associated with a feature or q to quit.
    # Once received, the feature is launched using the subprocess module.
    if request == "1":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        subprocess.call(["python3", "main.py"], cwd="news")
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    elif request == "2":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        subprocess.call(["python3", "main.py"], cwd="weather")
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    elif request == "3":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        subprocess.call(["python3", "main.py"], cwd="todo")
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    elif request == "q":
        break
