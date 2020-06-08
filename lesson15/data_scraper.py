#!/home/mholinka/projects/python_academy/env/bin/python
"""Lekce #15 - Uvod do programovani, web scraping"""

import csv
from typing import List

import requests
from bs4 import BeautifulSoup

URL = "http://heroes3.cz/hraci"


def hlavni() -> None:
    odpoved = ziskej_odpoved()
    naparsovano = vytahni_udaje(odpoved)

    tabulka = hledej_tabulku(naparsovano)
    radky = hledej_radky(tabulka)

    konecne_udaje = (hraci_info(row) for row in radky)
    uloz_csv(list(konecne_udaje))


def ziskej_odpoved():
    with requests.Session() as s:
        return s.get(URL)


def vytahni_udaje(resp):
    return BeautifulSoup(resp.text, "html.parser")


def hledej_tabulku(cont):
    return cont.find("table", {"class": "tab_top"})


def hledej_radky(tabl) -> list:
    return tabl.find_all("tr")[1:]


def hraci_info(tr) -> dict:
    try:
        poradi = tr.find_all("td")[0].text
        hrac = tr.find_all("td")[2].text
        body = tr.find_all("td")[3].text
        uspesnost = tr.find_all("td")[7].text
        return {"poradi": poradi, "hrac": hrac, "body": body, "uspesnost": uspesnost}

    except AttributeError:
        print("Indexy u jednotlivych bunek v radku nejsou v poradku")


def uloz_csv(data: List[dict]):
    with open("hraci.csv", "a", newline="") as csv_soubor:
        zahlavi = ["PORADI", "UZIVATEL", "BODY", "USPESNOST"]
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()

        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "PORADI": data[index]["poradi"],
                    "UZIVATEL": data[index]["hrac"],
                    "BODY": data[index]["body"],
                    "USPESNOST": data[index]["uspesnost"],
                }
            )


if __name__ == "__main__":
    hlavni()
