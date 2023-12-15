from gestion import *
import time
from scrapestock import *

LoadPRD()
print("""══════════════════════════════════════════════════════════
    🛒 WELCOME TO THE GROCERY MANAGEMENT SYSTEM.IO""")


while True:

    time.sleep(1)
    print("══════════════════════════════════════════════════════════")
    print("""    1 | Create New product 🌱
    2 | Adjust product 📝
    3 | Delete product 🗑️
    4 | Search product 🔍
    5 | Preview Stock 📋
    6 | Filter Stock 🔮
    7 | Apply a discount 📉
    8 | Re-arrange Stock 🔄
    9 | Archive product 📁
    10| Preview Archives 🗃
    11| Import from Jumia 🌐        ⭐
    12| Save Changes 💾
    
    0 | Quit 🚪
══════════════════════════════════════════════════════════
    """)
    inpt = input("Input: ")
    print("══════════════════════════════════════════════════════════")
    if inpt == "1":
        Ajouter()


    elif inpt == "2":
        AfficherINFO()
        EditObject()


    elif inpt == "3":
        AfficherINFO()
        Delete()


    elif inpt == "4":
        AfficherINFO()
        Search()


    elif inpt == "5":
        AfficherINFO()


    elif inpt == "6":
        print("""Filter by:
1 | Alimentary products
2 | Electronic products
3 | Discounted products""")
        temp = input("Choice: ")


        if temp == "1":
            Filtrer(ProduitAlimentaire)


        elif temp == "2":
            Filtrer(ProduitElectronique)


        elif temp == "3":
            PromotionAfficher()


        else:
            print("Invalid Input.")


    elif inpt == "7":
        AfficherINFO()
        Discount()


    elif inpt == "8":
        temp = input("""
1 | Sort by price (📈)
2 | Sort by price (📉)
3 | Sort by Alphabetical order (🅰️)

Choice: """)
        if temp == "1":
            TrieCroissant()


        elif temp == "2":
            TrieDecroissant()


        else:
            TrieAlpha()
        AfficherINFO()

    elif inpt == "9":
        Archive()

    elif inpt == "10":
        AfficherARCH()

    elif inpt == "11":
        Link = input("Link to scrape: ")
        try:
            ScrapeFromJumia(Link)
        except:
            print("There has been an error Importing data from the site.")

    elif inpt == "12":
        SauvgarderPRD()

    elif inpt == "0":
        temp = input("Would you like you save? (Y): ").upper()
        if temp == "Y":
            SauvgarderPRD()
            break
        else:
            print("Unsaved")
            break
