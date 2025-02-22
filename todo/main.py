import os

from dateutil.parser import parse

from styles import Style
from task import add_task, parse_tasks, delete_task


def show_details(task, index):
    """
    Shows additional details and actions a user can take for a specific task.

    :param task: The task, in the form of a dictionary.
    :param index: The index of the task in the main tasks list.
    """
    while True:
        print("{bold}{name}{end}".format(bold=Style.BOLD, name=task["name"], end=Style.END))
        print("Due on {}".format(parse(task["due"]).strftime("%-d %b %Y")))
        result = input("\nType x to complete/delete, b to go back: ")

        if result == "x":
            delete_task(index)
            break
        elif result == "b":
            break
        else:
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")


while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    print("{}To-do{}".format(Style.BOLD, Style.END))

    # Checks if the user has any to-dos existing pre-existingly. If so, the tasks are parsed and loaded on screen.
    if os.path.exists("{}/data.csv".format(os.path.dirname(os.path.abspath(__file__)))):
        tasks = parse_tasks()

    # If there are to-do lists, the program checks if the data.csv file exists — if not, it's likely that the user has
    # not used this feature before. The end output is customised to these changes.

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

    if request == "a":
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
        add_task()
        os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
    if request == "q":
        break
    else:
        try:
            request = int(request)
        except ValueError:
            pass
        else:
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
            if 0 <= request <= len(tasks):
                show_details(tasks[request - 1], request - 1)
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
