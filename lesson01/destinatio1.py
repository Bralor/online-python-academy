#!/usr/bin/env python3
""" Lekce #1 - Uvod do programovani, 1/2 Destinatio """

# I. KROK:
# Definujeme promenne, se kterymi chceme pracovat
SEZNAM_MEST = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
SEZNAM_CEN = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# II. KROK:
# Pozdravime uzivatele a doplnime oddelovace '='
# Zobrazit uzivateli nasi nabidkou - lokalita | cena
print(ODDELOVAC)
print("Vitejte u nasi aplikace Destinatio!")
print(ODDELOVAC)
print(
    """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)
print(ODDELOVAC)

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstupy
# Cislo destinace, jmeno, prijmeni, vek, email, heslo
por_cislo = int(input("Vyberte cislo lokality: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
vek = int(input("VEK: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)

# IV. KROK:
# Modifikujeme tyto hodnoty,
destinace = SEZNAM_MEST[por_cislo - 1]  # --> destiance[0] pokud bude por_cislo = 1
cena = SEZNAM_CEN[por_cislo - 1]

# VI. KROK:
# Vystupni sekce, vypisujeme konkretni udaje
# Jmeno, destinaci, cenu, email
print("UZIVATEL: " + jmeno)
print("DESTINACE: " + destinace)
print("CENA(cil:" + destinace + "): " + str(cena))
print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
