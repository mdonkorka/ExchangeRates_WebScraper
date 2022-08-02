from bs4 import BeautifulSoup
import requests

url = "https://www.exchangerates.org.uk/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

table = doc.find_all(class_="colthree")
Currency_ExRate = {}
for item in table:
    ExRate = float(item.find("strong").string)
    Country_Str = item.find(width='72').string
    Currency_ExRate[Country_Str] = ExRate

print("\n GET LIVE EXCHANGE RATE VALUES !\n")
CC = input("Enter CurrencyCode for Exchnage Rates: ")

NotFound = True
for Code in Currency_ExRate.keys():
    if CC == Code[:3]:
        NotFound = False
        break

if NotFound: 
    print("* Curreny Code does not exist *\n")
else:
    for item in Currency_ExRate:
        if item[:3] == CC:
            print(f"{item} - {Currency_ExRate[item]}")

