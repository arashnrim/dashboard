import os
from configparser import ConfigParser
from datetime import datetime
from time import sleep

from styles import Style

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

if name:
    print("\nGood {}, {}!".format(phrase, name))
else:
    print("\nGood {}!".format(phrase))

activities = [
    "Get the latest news",
    "Get weather information",
    "Get details on your location",
    "Perform basic calculations",
    "Get information about radio stations",
]

showPrompt = True
while True:
    if showPrompt:
        print("{blue}?{end} {bold}What would you like to do?{end}".format(blue=Style.BLUE, end=Style.END,
                                                                          bold=Style.BOLD))
        for index, activity in enumerate(activities):
            print("{bold}{index}{end} {activity}".format(bold=Style.BLUE, index=index + 1, end=Style.END,
                                                         activity=activity))
        print()

    request = input(
        "Enter a number from 1 to {activityCount} or enter q to quit: ".format(activityCount=len(activities)))

    if request not in "12345q" or request == "":
        print("The input was not valid; we'll try this again.")
        sleep(1.5)
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        continue

    if request == "1":
        # noinspection PyUnresolvedReferences
        import news
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    elif request == "2":
        # noinspection PyUnresolvedReferences
        import weather
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    elif request == "3":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        continue  # TODO: Implement location feature
    elif request == "4":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        continue  # TODO: Implement calculations feature
    elif request == "5":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        continue  # TODO: Implement radio feature
    elif request == "q":
        break
    continue
