#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
from pprint import pprint as pp

# I. KROK
# Zkopirujeme zadane slovniky
# Vytvorim novy (prazdny) slovnik
ODDELOVAC = "=" * 39
film1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": 93,
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "HRAJI": ["Tim Robbins", "Morgan Freeman"],
    "STOPAZ": "144 min",
}

film2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": 92,
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "HRAJI": ["Al Pacino", "Marlon Brando"],
    "STOPAZ": "175 min",
}

film3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": 90,
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "HRAJI": ["Christian Bale", "Heath Ledger"],
    "STOPAZ": "152 min",
}
film0 = {}

# II. KROK
# Vlozime klice (opet zatim prazdne)
film0["JMENO"] = ""
film0["HODNOCENI"] = None
film0["ROK"] = None
film0["REZISER"] = None

# # III. KROK
# # Doplnime hodnoty klicu
# # Primo + update() metodou
# # Kombinace s input()
film0["JMENO"] = "Shawshank Redemption"
film0.update(HODNOCENI=9.3)
film0["REZISER"] = "Frank Darabont"

# ROK = input("Vlozte hodnoty pro klic *ROK* : ")
# film0["ROK"] = ROK

# IV. KROK
# Vytvorime dalsi dva klice s hodnotami
STOPAZ = "144 min"
HRAJI = ("Tim Robbins", "Morgan Freeman")
film0.update({"STOPAZ": STOPAZ, "HRAJI": HRAJI})

# Klic *STOPAZ* odstranime pomoci metody *pop*
# Z klice *HRAJI* odstranime pomoci funkce *del*
film0.pop("STOPAZ")
del film0["HRAJI"]

# V. KROK
# Vytvorime novy slovnik *filmova_db*
# Nestujeme dva zbyvajici slovniky ze zadani
filmova_db = {}

filmova_db[film1["JMENO"]] = film1
filmova_db[film2["JMENO"]] = film2

# VI. KROK
# Vytvorime pomyslneho interpreta nasi db
# Ten predstavi nase filmy
print(ODDELOVAC)
print("Vitejte v nasi skromne filmove databazi")
print(
    f"""{ODDELOVAC}
Mame v nabidce tyto snimky:
{list(filmova_db.keys())}
"""
)

# VII. KROK
# Vyzkousime metodu slovniku .get()
print(ODDELOVAC)
film = input("Vyberte film: ")

print(ODDELOVAC)
pp(filmova_db.get(film, "Vami zadany film neni v db"))

# VIII. KROK
# Vyzkousime metodu slovniku .setdefault()
# pp(filmova_db.get(film, filmova_db.setdefault(film, )))
