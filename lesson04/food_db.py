#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
from pprint import pprint as pp

# I. KROK
# Vytvorime promenne, se kterymi budeme pracovat
# Nabidku potravin, *POTRAVINY*
# Prazdny slovnik, *KOSIK*
# Oddelovac, *ODDELOVAC*
KOSIK = {}
ODDELOVAC = "=" * 39
POTRAVINY = {"mleko": 30, "maso": 100, "banan": 30, "jogurt": 10, "chleb": 20}

# II. KROK
# Vlozit 3 potraviny z vyberu do kosiku
# Pomoci input() + metod spojenymi se slovniky
pp(POTRAVINY)

vyber1 = input("VYBERTE ZBOZI c.1: ")
vyber2 = input("VYBERTE ZBOZI c.2  ")
vyber3 = input("VYBERTE ZBOZI c.3: ")

KOSIK[vyber1] = POTRAVINY.get(vyber1, "NENI SKLADEM")
KOSIK[vyber2] = POTRAVINY.get(vyber2, "NENI SKLADEM")
KOSIK[vyber3] = POTRAVINY.get(vyber3, "NENI SKLADEM")
print(KOSIK)

# III. KROK
# Celou ulohu predelame pomoci smycky *while*
# Definujeme pocitadlo, *pocitadlo*
pocitadlo = 0

while (vyber_n := input("VYBERTE ZBOZI: ")) != 'exit':
    KOSIK[vyber_n] = POTRAVINY.get(vyber_n, "NENI SKLADEM")
    CELKEM = sum(KOSIK.values())

else:
    print(KOSIK, sep="\n")
    print(f"Cena CELKEM: {CELKEM} CZK")
