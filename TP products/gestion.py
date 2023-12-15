from datetime import datetime

from classes import Produit
from classes import ProduitAlimentaire
from classes import ProduitElectronique

import pickle
STOCK = []
ARCHIVE = []


def Ajouter():
    global x
    nom = input("New product name: ")
    prix = float(input("New product price: $"))
    qt = int(input("New product initial quantity: x"))
    print("""Class types: 
1 | ProduitAlimentaire
2 | ProduitElectronique
3 | Not sure (Base class)""")
    temp = input("Choice: ")
    if temp == "1":
        extra1_1 = int(input("Input EXP year: "))
        extra1_2 = int(input("Input EXP month: "))
        extra1_3 = int(input("Input EXP day: "))
        x = ProduitAlimentaire(nom, prix, qt, False, datetime(extra1_1, extra1_2, extra1_3))
    elif temp == "2":
        extra1 = int(input("Input warranty years: "))
        x = ProduitElectronique(nom, prix, qt, False, extra1)
    else:
        x = Produit(nom, prix, qt, False)

    STOCK.append(x)
    print(x.__str__())

def AfficherINFO():
    for product in STOCK:
        print("――――――――――――――――――――――――――――――――――")
        print(product.__str__())

def Archive():
    AfficherINFO()
    searchResult = Search()
    if searchResult == -1:
        pass
    else:
        print("⋆★⋆ Element archived. ⋆★⋆")
        ARCHIVE.append(STOCK[searchResult])
        STOCK.pop(searchResult)


def AfficherARCH():
    for product in ARCHIVE:
        print("――――――――――――――――――――――――――――――――――")
        print(product.__str__())

def SauvgarderPRD():
    f = open(f"stock.pkl", "wb")
    for product in STOCK:
        pickle.dump(product, f)
        print(f"⋆★⋆ {product.nom} saved successfully ⋆★⋆")
    print("――――――――――――――――――――――――――――――――――")
    f = open(f"archive.pkl", "wb")
    for product in ARCHIVE:
        pickle.dump(product, f)
        print(f"⋆★⋆ {product.nom} saved successfully ⋆★⋆")


def LoadPRD():  # HADI 7FDHA
    f = open("stock.pkl", "rb")
    while True:
        try:
            obj = pickle.load(f)
            STOCK.append(obj)
        except EOFError:
            break
    f = open("archive.pkl", "rb")
    while True:
        try:
            obj = pickle.load(f)
            ARCHIVE.append(obj)
        except EOFError:
            break


def Search():
    print("――――――――――――――――――――――――――――――――――")
    temp = input("Product name: ").lower()
    print("――――――――――――――――――――――――――――――――――")
    for i in range(len(STOCK)):
        if STOCK[i].nom.lower() == temp:
            print(f"Product found:")
            STOCK[i].__str__()
            return i
    print("Not found")
    return -1


def Delete():
    print("――――――――――――――――――――――――――――――――――")
    temp = input(f"insert ''reset'' to clear the stock or any key to skip:")
    if temp.lower() == "reset":
        STOCK.clear()
        print("⋆★⋆ Stock cleared. ⋆★⋆")
    else:
        searchResult = Search()
        if searchResult == -1:
            pass
        else:
            print("⋆★⋆ Element deleted. ⋆★⋆")
            STOCK.pop(searchResult)


def EditObject():
    searchResult = Search()
    if searchResult == -1:
        pass
    else:
        STOCK[searchResult].Edit()
        print("Operation successful.")


def TrieDecroissant():
    for j in range(len(STOCK)):
        for i in range(len(STOCK) - 1):
            if STOCK[i].prix < STOCK[i + 1].prix:
                x = STOCK[i]
                STOCK[i] = STOCK[i + 1]
                STOCK[i + 1] = x
    print("⋆★⋆ Stock has been sorted by price ⋆★⋆")


def TrieCroissant():
    for j in range(len(STOCK)):
        for i in range(len(STOCK) - 1):
            if STOCK[i].prix > STOCK[i + 1].prix:
                x = STOCK[i]
                STOCK[i] = STOCK[i + 1]
                STOCK[i + 1] = x
    print("⋆★⋆ Stock has been sorted by price ⋆★⋆")

def TrieAlpha():
    for j in range(len(STOCK)):
        for i in range(len(STOCK) - 1):
            if STOCK[i].nom > STOCK[i + 1].nom:
                x = STOCK[i]
                STOCK[i] = STOCK[i + 1]
                STOCK[i + 1] = x
    print("⋆★⋆ Stock has been sorted by name ⋆★⋆")

def Filtrer(SelectedClass):
    print("――――――――――――――――――――――――――――――――――")
    print(f"Previewing {SelectedClass.__name__} only:")
    print("――――――――――――――――――――――――――――――――――")
    for product in STOCK:
        if isinstance(product, SelectedClass):
            print(product.__str__())


def PromotionAfficher():
    print("――――――――――――――――――――――――――――――――――")
    print("Discounted products: ")
    print("――――――――――――――――――――――――――――――――――")
    for product in STOCK:
        if product.discount:
            print(product.__str__())


def Discount():
    searchResult = Search()
    if searchResult == -1:
        pass
    else:
        if STOCK[searchResult].discount:
            print("⋆★⋆ Product discount removed. ⋆★⋆")
            STOCK[searchResult].discount = False
        else:
            print("⋆★⋆ Product discounted. ⋆★⋆")
            STOCK[searchResult].discount = True


# ----------------------------------------------------------------------------

