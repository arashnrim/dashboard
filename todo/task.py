import csv
import os
from time import sleep

from dateutil.parser import parse

from styles import Style


def addTask():
    while True:
        print("{bold}Add Task{end}\n".format(bold=Style.BOLD, end=Style.END))

        name = input(
            "{blue}!{end} {bold}Name of task{end}: ".format(blue=Style.BLUE,
                                                            end=Style.END,
                                                            bold=Style.BOLD))
        due = input(
            "{blue}!{end} {bold}Due date of task{end}: ".format(blue=Style.BLUE,
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
            "{blue}!{end} {bold}Importance of task{end} (1 being least important to 3 being most): ".format(
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
            if not (1 <= importance <= 3):
                print("the importance of the task should be between 1 and 3; we'll try this again.")
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
    tasks = []
    with open("data.csv") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            tasks.append(row)
    return tasks


def parseTasks():
    tasks = readTasks()
    for index, task in enumerate(tasks):
        print(
            "{blue}{count}{end} [{importance}]{spaces}{bold}{name}{end} ".format(blue=Style.BLUE, count=index + 1,
                                                                                 end=Style.END,
                                                                                 bold=Style.BOLD, name=task["name"],
                                                                                 importance="!" * int(
                                                                                     task["importance"]), spaces=" " * (
                        1 + (3 - int(task["importance"])))
                                                                                 ))
    return len(tasks)
