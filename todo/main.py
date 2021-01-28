import json
import os

from styles import Style
from task import addTask, parseTasks


def showDetails(request):
    print("".format(request))


os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
print("{}To-do{}".format(Style.BOLD, Style.END))

while True:
    if os.path.exists("{}/data.csv".format(os.path.dirname(os.path.abspath(__file__)))):
        tasks = parseTasks()

    request = input(
        "\n{blue}!{end} {bold}Navigate your to-dos.{end} Type the task number to view a task, a to add a task, "
        "q to exit: ".format(
            blue=Style.BLUE,
            end=Style.END,
            bold=Style.BOLD))

    if request in str(range(1, tasks + 1)):
        request = int(request)
        showDetails(request)

    elif request == "a":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        addTask()
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    if request == "q":
        break
