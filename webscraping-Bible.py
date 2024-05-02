import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request

#give random chapter between 1 -> 21
random_chapter = random.randint(1,22)
if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

# format the url to include the randomly selected chapter number
webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Wpipindows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

#print(soup.title.text)

page_verses = soup.findAll('div', class_='p')

#print(page_verses)

myverses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v)

mychoice = random.choice(myverses)

print(f"Chapter: {random_chapter} Verse:{mychoice}")
