#!/usr/bin/env python3
""" Lekce #4 - Uvod do programovani, Nakupni kosik """
from pprint import pprint as pp

# I. KROK
# Vytvorime promenne, se kterymi budeme pracovat
# Nabidku potravin, *POTRAVINY*
# Prazdny slovnik, *KOSIK*
# Oddelovac, *ODDELOVAC*
KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": 30,
    "maso": 100,
    "banan": 30,
    "jogurt": 10,
    "chleb": 20,
    "jablko": 10,
    "pomeranc": 15,
}

# II. KROK
# Vypiseme nabidku potravin a oddelime
pp(POTRAVINY)
print(ODDELOVAC)

# III. KROK
# Vlozit 3 potraviny z vyberu do kosiku
# Pomoci input() + metod spojenymi se slovniky
vyber1 = input("VYBERTE ZBOZI c.1: ")
vyber2 = input("VYBERTE ZBOZI c.2  ")
vyber3 = input("VYBERTE ZBOZI c.3: ")

KOSIK[vyber1] = POTRAVINY.get(vyber1, "NENI SKLADEM")
KOSIK[vyber2] = POTRAVINY.get(vyber2, "NENI SKLADEM")
KOSIK[vyber3] = POTRAVINY.get(vyber3, "NENI SKLADEM")

print(ODDELOVAC)
print(KOSIK)
print(ODDELOVAC)
print(f"CELKEM: {sum(KOSIK.values())} CZK")

# IV. KROK
# Zakomentuj predchozi kod!
# Celou ulohu predelame pomoci smycky *while*
# Plnime kosik, dokud v nem nejsou 3 predmety

while len(KOSIK) < 3:
    vyber_n = input(f"VYBERTE ZBOZI (AKTUALNI POCET: {len(KOSIK)}): ")
    KOSIK[vyber_n] = POTRAVINY.get(vyber_n, "NENI SKLADEM")

# V. KROK
# Vytvorim *else* vetev
# Doplnime sumu veskereho zbozi v kosiku
else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI")
    print(KOSIK)
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(f"CENA CELKEM: {CELKEM} CZK")

# VI. KROK
# Aplikujeme nekonecnou smycku
# Koncept *break/continue* statement
pokracovat = True

while pokracovat:
    vyber_n = input(f"VYBERTE ZBOZI (AKTUALNI POCET: {len(KOSIK)}): ")
    if vyber_n not in POTRAVINY.keys():
        print("ZBOZI NENI SKLADEM!")
        continue
    else:
        KOSIK[vyber_n] = POTRAVINY[vyber_n]

    kontrola = input("POKRACOVAT V NAKUPU? (y/n)")
    if kontrola == "n":
        pokracovat = False

else:
    print(ODDELOVAC)
    print("UKONCUJI NAKUPOVANI...")
    print(KOSIK)
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(f"CENA CELKEM: {CELKEM} CZK")

# VII. KROK
# pouziti prirazovaciho operatoru *walrus operator*
while (vyber_n := input("VYBERTE ZBOZI: ")) != 'exit':
    if vyber_n not in POTRAVINY:
        print("NENI SKLADEM!")
        continue
    else:
        KOSIK[vyber_n] = POTRAVINY.get(vyber_n, "NENI SKLADEM")

else:
    print(ODDELOVAC)
    CELKEM = sum(KOSIK.values())
    print(KOSIK)
    print(ODDELOVAC)
    print(f"CENA CELKEM: {CELKEM} CZK")
