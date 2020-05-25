#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - hlavni funkce"""
import sys

from pomocne_funkce import zkontroluj_cestu
from pomocne_funkce import nacti_soubor
from pomocne_funkce import vytvor_soubory

# I. KROK
# Vytvorime hlavni funkci
def hlavni() -> None:
    # III. KROK
    # Existuje absolutni cesta?
    if zkontroluj_cestu(ABS_CESTA):
        # IV. KROK
        # Nacti obsah souboru
        obsah = nacti_soubor(JMENA_SOUBORU)
        # V. KROK
        # Vytvor soubory
        vytvor_soubory(obsah, ABS_CESTA)

    else:
        print("SOUBORY NELZE VYTVORIT! VRACENA HODNOTA --> False")


# II. KROK
# Volame funkci *hlavni()*
# __name__ == "__main__"
if __name__ == "__main__":
    ABS_CESTA = sys.argv[1]
    JMENA_SOUBORU = sys.argv[2]
    hlavni()
