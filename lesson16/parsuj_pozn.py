#!/home/mholinka/projects/python_academy/env/bin/python
"""Lekce #16 - Uvod do programovani, API intro"""

import sys
from typing import List, Generator

import sheet_writter


def hlavni(soubor) -> None:
    poznamky = ziskej_poznamky(soubor)
    rozdelene = parsuj_poznamky(poznamky)

    for index, poznamka in enumerate(generator_poznamek(rozdelene), 1):
        if index == 1:
            zahlavi = ("Kniha", "Popis", "Poznamka")
            sheet_writter.zapisovac(1, zahlavi)
        else:
            sheet_writter.zapisovac(index, poznamka)


def ziskej_poznamky(soubor) -> str:
    try:
        with open(soubor, "r") as txt_soub:
            obsah = txt_soub.read()
            return obsah

    except FileNotFoundError as fnf:
        print(f"{fnf.__class__.__name__}: Soubor neexistuje! -> {soubor}")


def parsuj_poznamky(pozn: str) -> List[str]:
    return [n.strip() for n in pozn.split("\n==========")]


def rozdel_poznamku(note: str) -> str:
    return list(filter(lambda x: x != "", note.split("\n")))


def generator_poznamek(poznamky: str) -> Generator[tuple, None, None]:
    for zprac_poznamka in poznamky:
        try:
            kniha, popis, pozn = rozdel_poznamku(zprac_poznamka)
            yield (kniha, popis, pozn)

        except ValueError as ve:
            print(f"{ve.__class__.__name__}: Nema 3 casti! > {zprac_poznamka}")


if __name__ == "__main__":
    soubor = sys.argv[1]
    hlavni(soubor)
