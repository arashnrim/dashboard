import os
from configparser import ConfigParser
from datetime import datetime

from PyInquirer import prompt

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
    print("Good {}, {}!".format(phrase, name))
else:
    print("Good {}!".format(phrase))

activities = [
    "Get the latest news",
    "Get weather information",
    "Get details on your location",
    "Perform basic calculations",
    "Get information about radio stations",
]

navigator = {
    "type": "list",
    "name": "activity",
    "message": "What would you like to do?",
    "choices": activities,
    "default": int(config.get("DEFAULT", "commonactivity"))
}
request = activities.index(prompt(navigator)["activity"])

if request == 0:
    pass  # TODO: Implement news feature
elif request == 1:
    # noinspection PyUnresolvedReferences
    import weather
elif request == 2:
    pass  # TODO: Implement location feature
elif request == 3:
    pass  # TODO: Implement calculations feature
elif request == 4:
    pass  # TODO: Implement radio feature
