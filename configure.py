from configparser import ConfigParser
from time import sleep

from styles import Style

config = ConfigParser()
config.read("config.ini")

print("Welcome to the Dashboard!")
sleep(2)
print("\nThe main aim of the Dashboard is to help you in using the computer.")
sleep(1.5)
print("Here, basic but common commands are available to run.")
print("Just use your arrow keys (↑ or ↓) and the enter key to select an option.")
print("In some prompts (indicated with {blue}?{end} or {blue}!{end}), you're allowed to type a response, too.".format(
    blue=Style.BLUE,
    end=Style.END))
sleep(2.5)

print("\n=== Setting Up ===")
print("Let's get started by getting to know you.")
sleep(1.5)
while True:
    name = input("{blue}?{end} {bold}What's your name?{end} ".format(blue=Style.BLUE, bold=Style.BOLD, end=Style.END))
    if not name:
        result = input(
            "{blue}!{end} {bold}You have not entered a name, continue anyway?{end} Type y to confirm, n to reject: ".format(
                blue=Style.BLUE, bold=Style.BOLD, end=Style.END))
        if result == "y" or result == "Y":
            config.set("DEFAULT", "name", name)
            print()
            break
        elif result == "n" or result == "N":
            print()
        else:
            print("The input was not valid; we'll try this again.", end="\n\n")
    else:
        result = input("{blue}?{end} {bold}Your name is {name}, correct?{end} Type y to confirm, n to reject: ".format(
            blue=Style.BLUE, end=Style.END, bold=Style.BOLD, name=name))
        if result == "y" or result == "Y":
            config.set("DEFAULT", "name", name)
            break
        elif result == "n" or result == "N":
            print("\nNot to worry; we'll do it again!")
        else:
            print("The input was not valid; we'll try this again.", end="\n\n")

sleep(1.5)

with open("config.ini", "w") as config_file:
    config.write(config_file)
print()
sleep(1.5)

print("That's all for setting up. Thank you for your time! If you wish to configure again, you may do so later on.",
      end="\n\n")
