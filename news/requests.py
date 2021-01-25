import feedparser
import os
from .sources import sources
from .styles import Style

news = []

os.system('cls' if os.name == 'nt' else "printf '\033c\n'")
print("{}News{}".format(Style.BOLD, Style.END))
print("One second, getting the latest news...")

for source in sources:
    for link in sources[source]:
        result = feedparser.parse(link)
        for entry in result.entries:
            entry["source"] = source
            news.append(entry)


# noinspection PyShadowingNames
def return_date(entry):
    return entry.published_parsed


news.sort(key=return_date, reverse=True)
