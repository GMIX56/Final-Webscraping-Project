from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title.soup

cryptos = soup.findAll("tr")  



for row in cryptos[1:6]:
    td = row.findAll('td')
    name = td[2].text.strip()
    current_price = td[3].text.strip()
    pChange24 = td[5].text.strip()

    current_price = float(current_price.replace("$", "").replace(",", "").strip())
    pChange24 = float(pChange24.replace("%", "").strip())
    corr_price = (current_price) * (1 + pChange24 / 100)
    
    print(f"{name}")
    print(f"Current Price:       ${current_price}")
    print(f"% Change 24H:        {pChange24}%")
    print(f"Corresponding Price: {corr_price:.2f}")
    print()


