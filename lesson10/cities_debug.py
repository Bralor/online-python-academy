#!/usr/local/bin/python3.8
"""Lekce #10 - Uvod do programovani, debugging"""

# I. KROK - Prochazime soubor radek po radku
# II. KROK - Nacteme radek
# III. KROK - Ostripujeme jej
# IV. KROK - Pomoci podminky zastavime ("quit")
# V. KROK - Rozdelit stat/mesto
# VI. KROK - Ostripovat
# VII. KROK - Prevest na zadany format
# VIII. KROK - Vypsat spravny vysledek
from typing import List


def zpracuj_udaje() -> None:
    obsah_souboru = nacti_udaje("cities.txt")
    projdi_soubor(obsah_souboru)


def nacti_udaje(jmeno_souboru) -> List[str]:
    try:
        with open(jmeno_souboru, "rt") as soubor:
            obsah = soubor.read().split("\n")
            return obsah

    except FileNotFoundError:
        print("Tady neni zadny takovy soubor, spatna cesta")


def projdi_soubor(soubor: List[str]) -> None:
    for radek in soubor:
        radek = radek.strip()
        if "quit" in radek.lower():
            return
        zeme, mesto = radek.split(",")
        mesto = mesto.strip()
        zeme = zeme.strip()
        print(zeme.title(), mesto.title(), sep=",")


zpracuj_udaje()
