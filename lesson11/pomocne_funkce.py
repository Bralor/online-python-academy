#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - pomocne funkce"""
import os
from typing import List


def zkontroluj_cestu(abs_cesta):
    try:
        vytvor_adresar(abs_cesta)
        print(f"VYTVARIM ...({os.path.basename(abs_cesta)})")
        return True

    except FileNotFoundError:
        print(f"NEPLATNA ABS.CESTA ({os.path.dirname(abs_cesta)})")
        return False

    except FileExistsError:
        print(f"ADRESAR JIZ EXISTUJE! ({os.path.abspath(abs_cesta)})")
        return False


def vytvor_adresar(abs_cesta):
    return os.mkdir(abs_cesta)


def nacti_soubor(soubor):
    try:
        with open(soubor, "r") as txt:
            obsah = [jmeno.strip() for jmeno in txt.readlines()]
            return obsah

    except FileNotFoundError:
        print(f"SOUBOR NEEXISTUJE ({os.path.abspath(soubor)})")


def vytvor_soubory(obsah, abs_cesta):
    try:
        for jmeno in obsah:
            novy_soubor = os.path.join(abs_cesta, jmeno)
            with open(novy_soubor, "w") as nf:
                print(f"Vytvarim {novy_soubor}")

    except TypeError as te:
        print(f"CHYBA PRI NACITANI OBSAHU: {te.__class__.__name__}")
