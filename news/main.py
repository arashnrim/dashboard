import os
import webbrowser

from .requests import news

from styles import Style

count = 0


def show_paginated(entries):
    print()
    for index in range(count, count + 5):
        entry = entries[index]
        print("{blue}{number}{end} {bold}{title}{end}".format(blue=Style.BLUE, number=index + 1, end=Style.END,
                                                              bold=Style.BOLD, title=entry.title))
        print("{source} | {date}".format(source=entry.source, date=entry.published[:-6]))


while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    show_paginated(news)
    print()
    result = input(
        "{blue}?{end} {bold}Type the article's number to open it.{end} Type n for the next page, p for the previous, "
        "s to stop: ".format(
            blue=Style.BLUE,
            end=Style.END,
            bold=Style.BOLD))
    if result.isdigit():
        if count <= int(result) <= count + 5:
            webbrowser.open(news[int(result) - 1].id)
    elif result == "n" or result == "N":
        count += 5
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
    elif result == "p" or result == "P":
        count -= 5
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
    elif result == "s" or result == "S":
        break