from time import sleep
from PyInquirer import prompt

from .parse import parse
from .request import retrieve_data

from .styling import Style

while True:
    location = input("Enter a location: ")
    data = retrieve_data(location)

    if data is not None:
        country_code = data["sys"]["country"]

        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        print("=== {}Weather for {}, {}{} ===".format(Style.BOLD,
                                                      location,
                                                      country_code, Style.END))
        parse(data)

    sleep(4)
    result = prompt({
        "type": "confirm",
        "name": "repeat",
        "message": "Enter another location?",
        "default": False
    })
    if not result["repeat"]: break
