#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - hlavni funkce"""
import sys

from json_funkce import nacti_json, zapis_json
from csv_funkce import nacti_csv, zapis_csv
from spolecne_funkce import uprav_obsah


def hlavni() -> None:
    if FORMAT == "2csv":
        obsah_json = nacti_json(SOUBOR)
        upravene = uprav_obsah(obsah_json)
        zapis_csv(upravene)

    elif FORMAT == "2json":
        seznam_json = nacti_csv(SOUBOR)
        zapis_json(seznam_json)


if __name__ == "__main__":
    SOUBOR = sys.argv[1]
    FORMAT = sys.argv[2]
    hlavni()
else:
    print("SPUSTENI SOUBORU VYZADUJE ZADANI CESTU K JSON SOUBORU")
