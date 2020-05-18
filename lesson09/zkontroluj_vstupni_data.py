#!usr/bin/env python3
"""Lekce #9 - Uvod do programovani, kontrola cisel"""

# I. KROK
# Vytvoreni hlavni funkce
def hlavni():
    nactena_cisla = nacitani_udaju("numbers.txt")
    ostripovana_data = ocisti_ciselne_udaje(nactena_cisla)
    zkontroluj_typ_udaje(ostripovana_data)


# II. KROK
# Potrebujeme nacist soubor s udaji
def nacitani_udaju(soubor):
    with open(soubor, "r") as txt:
        return txt.readlines()


# III. KROK
# Ciselne udaje zbavime symbolu pro novy radek "\n"
def ocisti_ciselne_udaje(neupravene):
    return [naformatuj_data(radek.strip()) for radek in neupravene]


# IV. KROK
# Udaj naformatovat dle dohodnuteho vzoru
def naformatuj_data(udaj):
    return f"ID: {udaj}, TYPE: {type(udaj)}"


# V. KROK
# Kontrolujeme spravny vstupni datovy typ
def zkontroluj_typ_udaje(upravene):
    overene_udaje = []

    while upravene:
        uvereni_typu(overene_udaje, upravene)


# VI. KROK
# Napiseme funkci, ktera bude chtit zkontrolovat typ kazdeho detailu
# Pokud je to cislo, melo by byt zmenitelne pomoci funkce int()
def uvereni_typu(uloziste, detail):
    try:
        vyber_cislo = detail.pop().split()[1][:-1]
        prevedena_hodnota = int(vyber_cislo)

    except ValueError as ve:
        print(f"NEKONVERTOVATELNE --> {vyber_cislo}, {ve.__class__.__name__}")

    else:
        print(f"{vyber_cislo} --> OK, pokracuji...")
        uloziste.append(prevedena_hodnota)

    finally:
        print("-" * 39)


# ad. I. KROK
hlavni()
