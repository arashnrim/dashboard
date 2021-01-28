import os

import feedparser
from sources import sources
from styles import Style

news = []


def return_date(entry):
    """
    Returns the date of the given entry.

    :param entry: A news entry, in the form of a dictionary.
    :return: The published date of the entry, in datetime-compatible format.
    """
    return entry.published_parsed


os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
print("{}News{}".format(Style.BOLD, Style.END))
print("One second, getting the latest news...")

for source in sources:
    for link in sources[source]:
        result = feedparser.parse(link)
        for entry in result.entries:
            entry["source"] = source
            news.append(entry)

# Inverts the sorting of the news articles — the newest articles are at the top while olders one fall below.
news.sort(key=return_date, reverse=True)
