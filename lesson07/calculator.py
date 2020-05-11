#!/usr/bin/env python3
"""Lekce #7 - Uvod do programovani, kalkulacka"""

# I. KROK
# Zadame pomocne promenne
NABIDKA = "DOSTUPNE OPERACE: "
OPERACE = "+", "-", "*", "/", "prum", "^"
ODDELOVAC = "-" * 25

# II. KROK
# Vytvorit hlavni ridici funkci
def main():
    while True:
        uvadec()
        vybrana_operace = input("OPERACE ('q'- konec): ")
        vyber_funkci(vybrana_operace)


# III. KROK
# Uvadeci funkce
def uvadec():
    print(NABIDKA, ODDELOVAC, "|".join(OPERACE), ODDELOVAC, sep="\n")


# IV. KROK
# Rozcestnik funkci
def vyber_funkci(operace):
    if operace in OPERACE[:4]:
        x1, x2, text = vezmi_dve_cisla(operace)
        vysledek = zakladni_operace(operace, x1, x2)
        print(ODDELOVAC, f"{text} {vysledek}", ODDELOVAC, sep="\n")

    elif operace == "prum":
        rada, text = vezmi_radu_cisel()
        vysledek = prumer(rada)
        print(ODDELOVAC, f"{text}, PRUMER = {vysledek}", ODDELOVAC, sep="\n")

    elif operace == "^":
        x1, x2, text = vezmi_dve_cisla(operace)
        vysledek = umocnovani(x1, x2)
        print(ODDELOVAC, f"{text} {vysledek}", ODDELOVAC, sep="\n")

    elif operace == "q":
        print("Doufam, ze se Vam kalkulacka libila! ^.^")
        exit()


# V. KROK
# Potrebujeme dva vstupy
def vezmi_dve_cisla(operace):
    cislo1 = int(input("CISLO 1: "))
    cislo2 = int(input("CISLO 2: "))
    odpoved = f"{cislo1} {operace} {cislo2} ="
    return cislo1, cislo2, odpoved


# VI. KROK
# Resime zakladni aritmeticke operatory
def zakladni_operace(operace, x1, x2):
    return {"+": x1 + x2, "-": x1 - x2, "*": x1 * x2, "/": x1 / x2}.get(operace)


# VII. KROK
# Potrebujeme radu cisel pro prumer
def vezmi_radu_cisel():
    rada_cisel = input("VLOZTE CISLA ODDELENA CARKOU: ")
    prevedene = [int(cislo) for cislo in rada_cisel.split(",")]
    odpoved = f"CISLA: {rada_cisel}"
    return prevedene, odpoved


# VIII. KROK
# Pocitam prumer z pomocne promenne
def prumer(rada_cisel):
    return round(sum(rada_cisel) / len(rada_cisel), 2)


# IX. KROK
# Umocnim cislo, exponentem
def umocnovani(cislo, exponent):
    return cislo ** exponent


# ad. II. KROK
# Volam svoji hlavni funkci
main()
