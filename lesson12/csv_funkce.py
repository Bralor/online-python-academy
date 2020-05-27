#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - csv funkce"""
import csv


def zapis_csv(upr_obsah: dict) -> None:
    with open("zamestnanci.csv", "a", newline="") as csvfile:
        zahlavi = ["ID", "EMAIL", "GENDER"]
        writer = csv.DictWriter(csvfile, fieldnames=zahlavi)
        writer.writeheader()
        for zamestnanec in upr_obsah:
            writer.writerow(
                {
                    "ID": upr_obsah[zamestnanec]["ID"],
                    "EMAIL": upr_obsah[zamestnanec]["EMAIL"],
                    "GENDER": upr_obsah[zamestnanec]["GENDER"],
                }
            )


def nacti_csv(jmeno_souboru: str) -> dict:
    seznam_json = list()
    try:
        with open(jmeno_souboru, "r") as csv_soubor:
            reader = csv.DictReader(csv_soubor, delimiter=",")
            for h in reader:
                seznam_json.append(h)

        return seznam_json
    except:
        print("SOUBOR .CSV NELZE NACIST!")
