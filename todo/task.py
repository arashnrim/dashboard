import csv
import datetime
import os
from time import sleep

from dateutil.parser import parse

from styles import Style


def addTask():
    """
    Creates and stores a new task.

    This function will prompt the user for a task name, due date, and importance. Appropriate validation checks are run
    to ensure that these values are as they should be. Once validated, the task is compiled and stored in the data.csv
    file for use later on.
    """
    while True:
        print("=== {bold}Add a new task{end} ===\n".format(bold=Style.BOLD, end=Style.END))

        name = input(
            "{blue}?{end} {bold}What is the name of task?{end} ".format(blue=Style.BLUE,
                                                                        end=Style.END,
                                                                        bold=Style.BOLD))
        due = input(
            "{blue}!{end} {bold}When is the task due?{end} {bold}(DD/MM/YYYY){end}: ".format(blue=Style.BLUE,
                                                                end=Style.END,
                                                                bold=Style.BOLD))
        try:
            due_date = parse(due, fuzzy=True)
        except ValueError:
            print("The due date format is invalid; we'll try again.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
            continue
        importance = input(
            "{blue}?{end} {bold}How important is the task?{end} (1 being least important to 3 being most): ".format(
                blue=Style.BLUE,
                end=Style.END,
                bold=Style.BOLD))
        try:
            importance = int(importance)
        except ValueError:
            print("The importance of the task should be a number between 1 and 3; we'll try this again.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
            continue
        else:
            if not (1 <= importance <= 3) or importance == float:
                print("The importance of the task should be between 1 and 3; we'll try this again.")
                sleep(1)
                os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
                continue

        task = {"name": name, "due": due_date, "importance": importance}
        file_exists = os.path.isfile("data.csv")
        with open("data.csv", "a") as file:
            fields = ["name", "due", "importance"]
            writer = csv.DictWriter(file, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            writer.writerow(task)
        break


def readTasks():
    """
    Reads the tasks stored in the data.csv file.

    :return: A list with the user's tasks.
    """
    tasks = []
    with open("data.csv") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            tasks.append(row)
    return tasks


def parseTasks():
    """
    Displays the tasks in a user-friendly way, allowing for user interaction with the task (by associating it with an
    inputtable number).

    :return: A list with the user's tasks
    """
    tasks = readTasks()
    for index, task in enumerate(tasks):
        due = datetime.datetime.now() > parse(task["due"])
        due_date = parse(task["due"]).strftime("%-d %b %Y")
        print(
            "{blue}{count}{end} [{importance}]{spaces}{color}{bold}{name}{end} {due_date}".format(blue=Style.BLUE,
                                                                                                  count=index + 1,
                                                                                                  end=Style.END,
                                                                                                  color=Style.RED if due else "",
                                                                                                  bold=Style.BOLD,
                                                                                                  name=task["name"],
                                                                                                  importance="!" * int(
                                                                                                      task[
                                                                                                          "importance"]),
                                                                                                  spaces=" " * (
                                                                                                          1 + (3 - int(
                                                                                                      task[
                                                                                                          "importance"]))),
                                                                                                  due_date="- " + due_date
                                                                                                  ))

    return tasks


def deleteTask(request):
    """
    Removes a user's task.
    :param request: The index of task to be deleted.
    :return:
    """
    request += 1
    with open("data.csv", "r") as source_file, open("data_temp.csv", "w") as copy_file:
        writer = csv.writer(copy_file)
        reader = csv.reader(source_file, delimiter=",")
        rows = [row for row in reader]
        rows.pop(request)
        writer.writerows(rows)

    os.rename("data.csv", "data_old.csv")
    os.rename("data_temp.csv", "data.csv")
    os.remove("data_old.csv")
