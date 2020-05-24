#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - hlavni funkce"""
import sys
from typing import List

from pomocne_funkce import zkontroluj_cestu
from pomocne_funkce import nacti_soubor
from pomocne_funkce import vytvor_soubory


def hlavni() -> None:
    if zkontroluj_cestu(ABS_CESTA):
        obsah = nacti_soubor(JMENA_SOUBORU)
        vytvor_soubory(obsah, ABS_CESTA)

    else:
        print("SOUBORY NELZE VYTVORIT! VRACENA HODNOTA --> False")


if __name__ == "__main__":
    ABS_CESTA = sys.argv[1]
    JMENA_SOUBORU = sys.argv[2]
    hlavni()
