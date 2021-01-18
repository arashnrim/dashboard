import feedparser
from .sources import sources

news = []

print("\nOne second, fetching news to read!\n")

for source in sources:
    for link in sources[source]:
        result = feedparser.parse(link)
        for entry in result.entries:
            entry["source"] = source
            news.append(entry)


def return_date(entry):
    return entry.published_parsed


news.sort(key=return_date, reverse=True)
