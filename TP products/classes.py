import datetime


class Produit:
    def __init__(self, nom: str, prix: float, qt: int, discount=False):  # QT: Quantitee de stock
        self.nom = nom
        self.prix = prix
        self.qt = qt
        self.discount = discount

    def __str__(self):
        return f"🏷️ | NAME: {self.nom}\n📦 | PRICE: ${self.prix}\n💵 | QTY: x{self.qt}"

    def Edit(self):
        print("""        1 | Change product name
        2 | Change product price
        3 | Changer product quantity
        """)
        while True:
            temp = input("Choice: ")
            if temp == "1":
                newtemp = input("New name: ")
                self.nom = newtemp
                break
            elif temp == "2":
                newtemp = float(input("New price: "))
                self.prix = newtemp
                break
            elif temp == "3":
                newtemp = int(input("New QTY: "))
                self.qt = newtemp
                break
            else:
                print("Invalid input.")


# ===================================================================


class ProduitAlimentaire(Produit):
    def __init__(self, nom: str, prix: float, qt: int, discount:bool, date_exp: datetime):
        super().__init__(nom, prix, qt, discount)
        self.date_exp = date_exp

    def __str__(self):
        return f"🏷️ | NAME: {self.nom}\n📦 | PRICE: ${self.prix}\n💵 | QTY: x{self.qt}\n📅️ | EXP-DATE: {self.date_exp.strftime('%Y-%m-%d')}"

    def Edit(self):
        print("""        1 | Change product name
        2 | Change product price
        3 | Change product quantity
        4 | Change product Expiration date""")
        while True:
            temp = input("Choice: ")
            if temp == "1":
                newtemp = input("New name: ")
                self.nom = newtemp
                break
            elif temp == "2":
                newtemp = float(input("New price: "))
                self.prix = newtemp
                break
            elif temp == "3":
                newtemp = int(input("New QTY: "))
                self.qt = newtemp
                break
            elif temp == "4":
                newtemp = (input("New EXP Date: "))
                self.date_exp = newtemp
                break
            else:
                print("Invalid input.")


# ==========================================================================


class ProduitElectronique(Produit):
    def __init__(self, nom: str, prix: float, qt: int, discount: bool, garantie: int):
        super().__init__(nom, prix, qt, discount)
        self.garantie = garantie

    def __str__(self):
        return f"🏷️ | NAME: {self.nom}\n📦 | PRICE: ${self.prix}\n💵 | QTY: x{self.qt}\n🛡️ | WARRANTY: {self.garantie} year(s)"

    def Edit(self):
        print("""        1 | Change product name
        2 | Change product price
        3 | Change product quantity
        4 | Change product warranty date""")
        while True:
            temp = input("Choice: ")
            if temp == "1":
                newtemp = input("New name: ")
                self.nom = newtemp
                break
            elif temp == "2":
                newtemp = float(input("New price: "))
                self.prix = newtemp
                break
            elif temp == "3":
                newtemp = int(input("New QTY: "))
                self.qt = newtemp
                break
            elif temp == "4":
                newtemp = int(input("New Warranty: "))
                self.garantie = newtemp
                break
            else:
                print("Invalid input.")
