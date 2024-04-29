
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
stock_data = soup.findAll("div",attrs={"class":"table-cell"})

print(len(stock_data))
print(stock_data[1].text)
print(stock_data[12].text)
counter = 1

#name, change pct, last price, calculated(previous price)

for x in range(5):
    name = stock_data[counter].text
    change = float(stock_data[counter+2].text.strip("+").strip("%")) #Remove + and period
    last_price = float(stock_data[counter+3].text)


    prev_price = round(last_price / (1+(change/100)),2)

    print(f"Company Name: {name}")
    print(f"Change: {change}")
    print(f"Price: {last_price}")
    print(f"Previous: {prev_price}")
    counter += 11

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


##
##
##
##

