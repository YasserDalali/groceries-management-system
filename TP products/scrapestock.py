import requests
from bs4 import BeautifulSoup
from classes import *
from gestion import *


def ScrapeFromJumia(Link):
    url = Link
    site = requests.get(url).content
    soup = BeautifulSoup(site, 'lxml')

    articles = soup.find_all("article", {"class": "prd _fb col c-prd"})

    for article in articles:
        name = article.find("h3", {"class": "name"}).text.strip()
        price = article.find("div", {"class": "prc"}).text.replace(" ", '').replace("Dhs", '').replace(",","").strip()

        x = Produit(name, float(price), 0)
        print(x.__str__())
        print("――――――――――――――――――――――――――――――――――")
        STOCK.append(x)
