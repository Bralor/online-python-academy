#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - json funkce"""
import json


def nacti_json(jmeno_souboru) -> dict:
    try:
        with open(jmeno_souboru, "r") as json_soub:
            obsah = json.load(json_soub)
            return obsah

    except FileNotFoundError:
        print("SOUBOR NEEXISTUJE!")

    except json.decoder.JSONDecodeError:
        print("JSON POTREBUJE JAKO VSTUPNI UDAJE JEDEN OBJEKT!")


def zapis_json(obsah: dict) -> None:
    try:
        with open("zamestnanci.json", "w") as json_soubor:
            json.dump(obsah, json_soubor, indent=4)

    except:
        print("SOUBOR NELZE ZAPSAT JAKO .JSON")
