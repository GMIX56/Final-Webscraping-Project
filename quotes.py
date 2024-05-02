from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from collections import defaultdict
import plotly.graph_objs as go

authorQuotes = defaultdict(list)
allTags = []

for i in range(1, 11):
    url = "https://quotes.toscrape.com/page/" + str(i) + '/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    quotes = soup.findAll(class_='quote')
    for q in quotes:
        quote = q.find(class_='text').string.strip()
        author = q.find(class_='author').string.strip()
        tags = [tag.text.strip() for tag in q.find_all(class_='tag')]
        allTags.append(tags)
        authorQuotes[author].append(quote)

allTags = [tag for sublist in allTags for tag in sublist]

quotesCount = defaultdict(int)
for author, quotes in authorQuotes.items():
    quotesCount[author] = len(quotes)
mostQuotes = max(quotesCount, key=quotesCount.get)
leastQuotes = min(quotesCount, key=quotesCount.get)

totalQuotes = 0
totalLength = 0
longestLength = 0
longestQuote = ""
shortestLength = 100000000000000
shortestQuote = ""

for quotes in authorQuotes.values():
    for quote in quotes:
        totalLength += len(quote)

        if len(quote) > longestLength:
            longestLength = len(quote)
            longestQuote = quote

        if len(quote) < shortestLength:
            shortestLength = len(quote)
            shortestQuote = quote


for quotes in authorQuotes.values():
    for quote in quotes:
        totalLength += len(quote)
    totalQuotes += len(quotes)
averageLength = totalLength/totalQuotes


tagCount = defaultdict(int)
for tag in allTags:
    tagCount[tag] += 1

topTag = max(tagCount, key=tagCount.get)
totalTags = sum(tagCount.values())


topAuthors = sorted(quotesCount.items(), key=lambda x: x[1], reverse=True)[:10]
authorNames = []
author_quoteCounts = []
for author, count in topAuthors:
    authorNames.append(author)
    author_quoteCounts.append(count)
fig1 = go.Figure([go.Bar(x=authorNames, y=author_quoteCounts)])
fig1.update_layout(title='Top 10 Authors by Number of Quotes')


topTags = sorted(tagCount.items(), key=lambda x: x[1], reverse=True)[:10]
tagNames = []
tag_counts = []
for tag, count in topTags:
    tagNames.append(tag)
    tag_counts.append(count)
fig2 = go.Figure([go.Bar(x=tagNames, y=tag_counts)])
fig2.update_layout(title='Top 10 Tags by Popularity')


print(f"Author with the most quotes: {mostQuotes}")
print()
print(f"Author with the least quotes: {leastQuotes}")
print()
print(f"Average length of quotes: {averageLength}")
print()
print(f"Longest quote: {longestQuote}")
print()
print(f"Shortest quote: {shortestQuote}")
print()

topTag = topTag.replace("Tags:", "").strip()
print(f"Most popular tag: {topTag}")
print(f"Total tags used across all quotes: {totalTags}")

fig1.show()
fig2.show()