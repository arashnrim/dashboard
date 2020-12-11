import os
from configparser import ConfigParser
from datetime import datetime

from PyInquirer import prompt

if not (os.path.exists("{}/config.ini".format(os.path.dirname(os.path.abspath(__file__))))):
    pass

config = ConfigParser()
config.read("config.ini")
name = config.get("DEFAULT", "name")
time = datetime.now().hour
phrase = ""

if time < 12:
    phrase = "morning"
elif 12 <= time < 17:
    phrase = "afternoon"
if time >= 18: phrase = "evening"

if name:
    print("Good {}, {}!".format(phrase, name))
else:
    print("Good {}!".format(phrase))

navigator = {
    "type": "list",
    "name": "activity",
    "message": "What would you like to do?",
    "choices": [
        "Get the latest news",
        "Get weather information",
        "Get details on your location",
        "Perform basic calculations",
        "Get information about radio stations",
    ]
}
request = prompt(navigator)
print(request)
