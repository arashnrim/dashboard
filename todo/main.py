import os

from dateutil.parser import parse

from styles import Style
from task import addTask, parseTasks, deleteTask


def showDetails(task, request):
    while True:
        print("{bold}{name}{end}".format(bold=Style.BOLD, name=task["name"], end=Style.END))
        print("Due on {}".format(parse(task["due"]).strftime("%-d %b %Y")))
        result = input("\nType x to complete (delete), b to go back: ")

        if result == "x":
            deleteTask(request)
            break
        elif result == "b":
            break


os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
print("{}To-do{}".format(Style.BOLD, Style.END))

while True:
    if os.path.exists("{}/data.csv".format(os.path.dirname(os.path.abspath(__file__)))):
        tasks = parseTasks()

    if not (os.path.exists("{}/data.csv".format(os.path.dirname(os.path.abspath(__file__))))):
        print("{yellow}!{end} There are no tasks.".format(yellow=Style.YELLOW, end=Style.END))
        request_message = "\n{blue}!{end} {bold}Navigate your to-dos.{end} Type a to add a task, q to exit: ".format(
            blue=Style.BLUE, end=Style.END, bold=Style.BOLD)
    else:
        if len(tasks) == 0:
            print("{yellow}!{end} There are no tasks.".format(yellow=Style.YELLOW, end=Style.END))
            request_message = "\n{blue}!{end} {bold}Navigate your to-dos.{end} Type a to add a task, q to exit: ".format(
                blue=Style.BLUE, end=Style.END, bold=Style.BOLD)
        else:
            request_message = "\n{blue}!{end} {bold}Navigate your to-dos.{end} Type the task number to view a task, " \
                              "a to add a task, q to exit: ".format(blue=Style.BLUE, end=Style.END, bold=Style.BOLD)

    request = input(request_message)

    try:
        request = int(request)
    except ValueError:
        if request == "a":
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
            addTask()
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        if request == "q":
            break
    else:
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        showDetails(tasks[request - 1], request - 1)
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
