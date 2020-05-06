#!/usr/bin/env python3
"""Lekce #6 - Uvod do programovani, nase prvni funkce"""

# I. KROK
# Zadani nasi ulohy
UDAJE = """
byt 0001,55 m2,Olomouc,ul.Heyrovského,
byt 0003,65 m2,Olomouc,ul.Novosadský dvůr,
byt 0004,75 m2,Olomouc,ul.Wolkerova,
byt 0004,68 m2,Olomouc,ul.Zikova,
byt 0001,36 m2,Olomouc,ul.Nová Ulice,
byt 0003,46 m2,Olomouc,ul.Nové sady,
byt 0004,75 m2,Olomouc,ul.Nová Ulice,
byt 0003,42 m2,Olomouc,ul.Nová Ulice,
byt 0005,107 m2,Olomouc,ul.Nová Ulice,
byt 0003,74 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Nešverova,
byt 0002,55 m2,Olomouc,ul.Dělnická,
byt 0004,59 m2,Olomouc,ul.Zirmova,
byt 0007,92 m2,Olomouc,ul.Nová Ulice,
byt 0002,52 m2,Olomouc,ul.Nová Ulice,
byt 0004,76 m2,Olomouc,ul.Nová Ulice,
byt 0002,81 m2,Olomouc,ul.Nová Ulice,
byt 0003,64 m2,Olomouc,ul.Za vodojemem,
byt 0007,113 m2,Olomouc,ul.Jihoslovanská,
byt 0005,94 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Rošického,
byt 0003,75 m2,Olomouc,ul.Rošického,
byt 0004,48 m2,Olomouc,ul.Handského,
byt 0004,68 m2,Olomouc,ul.Komenského,
byt 0003,61 m2,Olomouc,ul.Jarmily Glazarové,
byt 0004,39 m2,Olomouc,ul.Přichystalova,
byt 0003,70 m2,Olomouc,ul.Foerstova,
byt 0005,61 m2,Olomouc,ul.Nová Ulice,
byt 0007,88 m2,Olomouc,ul.Nová Ulice,
byt 0003,92 m2,Olomouc,ul.U cukrovaru,
byt 0003,56 m2,Olomouc,ul.U cukrovaru,
byt 0004,56 m2,Olomouc,ul.Paseka,
byt 0002,74 m2,Olomouc,ul.Rokycanova,
byt 0007,116 m2,Olomouc,ul.U cukrovaru,
byt 0004,59 m2,Olomouc,ul.Řezáčova,
byt 0004,100 m2,Olomouc,ul.Libušina,
byt 0003,64 m2,Olomouc,ul.Řezáčova,
byt 0001,33 m2,Olomouc,ul.Libušina,
byt 0006,87 m2,Olomouc,ul.Černá cesta,
byt 0007,95 m2,Olomouc,ul.Kaštanová,
byt 0003,74 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nová Ulice,
byt 0004,86 m2,Olomouc,ul.Hněvotínská,
byt 0002,67 m2,Olomouc,ul.Polská,
byt 0007,120 m2,Olomouc,ul.Dvořákova,
byt 0004,90 m2,Olomouc,ul.Dvořákova,
byt 0004,86 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nešverova,
byt 0001,45 m2,Olomouc,ul.Zirmova,
byt 0006,114 m2,Olomouc,ul.Přichystalová,
"""

# II. KROK
# Definujeme vzor, jak chceme UDAJE prevest
# Vzor prevadeni:
prevod_udaju = {
    "byt 0001": "1+1",
    "byt 0002": "2+1",
    "byt 0003": "2+kk",
    "byt 0004": "3+1",
    "byt 0005": "3+kk",
    "byt 0006": "4+1",
    "byt 0007": "4+kk",
}

# III. KROK
# Prochazime promennou *udaj* jeden radek za druhym
# for radek in UDAJE.split("\n"):
# print(radek)  # ukazat prazdne retezce na zacatku/ konci

# IV. KROK
# Napiseme seznamovou komprehenci s podminkou
rozdelene_radky = [radek for radek in UDAJE.split("\n") if radek != ""]
# print(rozdelene_radky)

# V. KROK
# Potrebujeme promennou *udaje* rozdelit
# Ukazka vicenasobneho prirazeni
# Rozsirene prirazovani
rozdelene_udaje = list()
pocet_zmen = 0

for cislo, radek in enumerate(rozdelene_radky, 1):
    pocet_zmen += 1
    # VI. KROK
    # Chybne prirazeni
    # print(f"RADEK {cislo}: {radek}")
    # break

    # VII. KROK
    # Spravne prirazeni
    ic_bytu, plocha, mesto, ulice, zbytek = radek.split(",")

    # VIII. KROK
    # chceme pouze ic a zbytek
    # rozbalovaci operator
    ic_bytu, *zbytek_informaci = radek.split(",")
    rozdelene_udaje.append([ic_bytu, *zbytek_informaci])


# IX. KROK
# Potrebujeme menit oznaceni bytu za typ bytu
# Uvod do funkci
# def zamenovac_oznaceni(typ):
#     if typ == "byt 0001":
#         return "1+1"


# Definice moji prvni funkce
# vstupy do funkci
# vystupy funkce
# X. KROK
def zamenovac_oznaceni(typ, prevodnik):
    return prevodnik.get(typ, None)


# XI. KROK
# Doplnime smycku s nasi novou funkci
aktualizovane = list()

for radek in rozdelene_udaje:
    puvodni_id, *zbytek = radek
    prevod = zamenovac_oznaceni(puvodni_id, prevod_udaju)
    aktualizovane.append([prevod, *zbytek[:-1]])

# XII. KROK
# moduly!
from pprint import pprint

print(aktualizovane)
