import os
from time import sleep

from parse import parse
from request import retrieve_data
from styles import Style

while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    print("{}Weather{}".format(Style.BOLD, Style.END))

    # Prompts the user for a location to find.
    location = input(
        "{blue}?{end} {bold}Where would you like to know the weather about?{end} Alternatively, type q to exit: "
            .format(blue=Style.BLUE, end=Style.END, bold=Style.BOLD))

    # Attempts to retrieve the weather information for the user-specified location.
    if location == "q":
        break
    else:
        data = retrieve_data(location)

    # If the data payload is not empty, then it will be displayed to the user.
    if data is not None:
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        country_code = data["sys"]["country"]

        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        print("=== {}Weather for {}, {}{} ===".format(Style.BOLD,
                                                      location,
                                                      country_code, Style.END))
        parse(data)

        sleep(4)
    else:
        sleep(1.5)
        continue

    result = input(
        "\n{blue}?{end} {bold}Enter another location?{end} Type y to repeat, n to stop: ".format(blue=Style.BLUE,
                                                                                                 end=Style.END,
                                                                                                 bold=Style.BOLD))
    if result == "y" or result == "Y":
        pass
    elif result == "n" or result == "N":
        break
    else:
        print("The input was not valid; we'll try that again.")
