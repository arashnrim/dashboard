from configparser import ConfigParser
from time import sleep

from PyInquirer import prompt

config = ConfigParser()
config.read("config.ini")

print("Welcome to the Dashboard!\n")
sleep(2)
print("The main aim of the Dashboard is to help you in using the computer.")
sleep(1.5)
print("Here, basic but common commands are available to run.")
print("Just use your arrow keys (↑ or ↓) and the enter key to select an option.")
print("In some prompts, you're allowed to type a response, too.")
sleep(2.5)

print("\n=== Setting Up ===")
print("Let's get started by getting to know you.")
sleep(1.5)
while True:
    name = input("What's your name? ")
    if not name:
        result = prompt({
            "type": "confirm",
            "name": "no_name",
            "message": "You have not entered a name, continue anyway?",
            "default": False
        })
        if result["no_name"]:
            config.set("DEFAULT", "name", name)
            break
    else:
        result = prompt({
            "type": "confirm",
            "name": "name_confirmation",
            "message": "Your name is {}, correct?".format(name),
            "default": False
        })
        if result["name_confirmation"]:
            config.set("DEFAULT", "name", name)
            break
        else:
            print("\nNot to worry; we'll do it again!")

sleep(1.5)
print()
activities = [
    "Getting the latest news",
    "Getting weather information",
    "Getting details on your location",
    "Performing basic calculations",
    "Getting information about radio stations",
]
while True:
    activity_result = prompt({
        "type": "list",
        "name": "activity",
        "message": "Great! Now, what is the most often thing you think you will do?",
        "choices": activities
    })
    confirmation_result = prompt({
        "type": "confirm",
        "name": "activity_confirmation",
        "message": "Your most common activity is {}, correct?".format(activity_result["activity"].lower()),
        "default": False
    })
    if activity_result["activity"]:
        config.set("DEFAULT", "commonActivity", str(activities.index(activity_result["activity"])))
        break
    else:
        print("\nNot to worry; we'll do it again!")

with open("config.ini", "w") as config_file:
    config.write(config_file)
print()
sleep(1.5)

print("That's all for setting up. Thank you for your time! If you wish to configure again, you may do so later on.",
      end="\n\n")
