import os
import webbrowser

from requests import news

from styles import Style

count = 0


def show_paginated(entries):
    """
    Shows the news entries in a paginated order of five entries per page.

    :param entries: A list that stores all the news articles to display.
    """
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
    # If the user has entered a digit, the program presume that they'd like to read the article. Using the webbrowser
    # module, the user's default web browser is launched with the news article link directly.
    if result.isdigit():
        if count <= int(result) <= count + 5:
            webbrowser.open(news[int(result) - 1].id)
    elif result == "n" or result == "N":
        if count < len(news) - 5:
            count += 5
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
    elif result == "p" or result == "P":
        if count >= 5:
            count -= 5
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
    elif result == "s" or result == "S":
        break
