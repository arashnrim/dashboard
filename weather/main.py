import os
from time import sleep
from styles import Style
from parse import parse
from request import retrieve_data

os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
print("{}Weather{}".format(Style.BOLD, Style.END))

while True:

    while True:
        location = input(
            "{blue}?{end} {bold}Where would you like to know the weather about?{end} ".format(blue=Style.BLUE,
                                                                                     end=Style.END,
                                                                                          bold=Style.BOLD))

    
    data = retrieve_data(location)

    if data is not None:
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        country_code = data["sys"]["country"]

        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        print("=== {}Weather for {}, {}{} ===".format(Style.BOLD,
                                                      location,
                                                      country_code, Style.END))
        parse(data)

    sleep(4)
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
