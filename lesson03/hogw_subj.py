#!/usr/bin/env python3
"""Lekce c. 3, druhy projekt - Skolni rozvrh"""
# -------------------------------------------------------------------------------
# PREDMETY = ('Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
# 'Bylinkarstvi', 'Lektvary')

# SKUP_PREMENOVANI = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
#   'Ron', 'Hermiona]
# SKUP_ASTRONOMIE = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
# SKUP_OBRANA = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
# SKUP_BYLINKARSTVI = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
# SKUP_LEKTVARY = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']
#
# -------------------------------------------------------------------------------
# I. KROK
# Vytvorim prazdny slovnik "rozvrh"
ROZVRH = {}

# II. KROK
# Klice slovniku budou stringy z promenne PREDMETY
# Hodnoty klicu jsou seznamy skupin
ROZVRH["Premenovani"] = [
    "Adam",
    "Chelsea",
    "Marcus",
    "Oliver",
    "Alex",
    "Sandra",
    "Ann",
    "Ron",
    "Hermiona",
]
ROZVRH["Astronomie"] = [
    "Marcus",
    "Alex",
    "Glenn",
    "Samuel",
    "Hermiona",
    "Clara",
    "Chelsea",
]
ROZVRH["Obrana_proti_cerne_magii"] = ["Hermiona", "Adam", "Tyler", "Alex", "Clara"]
ROZVRH["Bylinkarstvi"] = ["Abraham", "Marcus", "Hermiona", "Alex", "Glenn", "Clara"]
ROZVRH["Lektvary"] = ["Alfred", "Curt", "Oliver", "Tyler", "Hermiona", "Ann"]

# III. KROK
# Vytvorime sety studentu v jednotlivych klicich
set_premenovani = set(ROZVRH["Premenovani"])
set_astronomie = set(ROZVRH["Astronomie"])
set_obrana = set(ROZVRH["Obrana_proti_cerne_magii"])
set_bylinkarstvi = set(ROZVRH["Bylinkarstvi"])
set_lektvary = set(ROZVRH["Lektvary"])

# IV. KROK
# Do *set_premenovani* studenta se jmenem *Harry*
# Ze setu *set_astronomie* odebereme *Samuel*
set_premenovani.add("Harry")
set_astronomie.discard("Samuel")

# V. KROK
# Vypiseme zmeny po pridani/odebrani
print(f"PRED PRIDANIM CLENA: ")
print(ROZVRH["Premenovani"])
print(f"PO PRIDANI CLENA: ")
print(set_premenovani, type(set_premenovani))

# VI. KROK
# Zjistime, kdo navstevuje vsechny predmety
print()
print("Kdo se ucastni vsech predmetu: ")
print(set_premenovani & set_astronomie & set_obrana & set_bylinkarstvi & set_lektvary)

# X. KROK
# bool test na podmnoziny (S.issubset())
# Je vsichni studenti z hodin obrany v hodine premenovani
print()
dotaz_1 = set(ROZVRH["Obrana_proti_cerne_magii"]).issubset(set_premenovani)
print(f"ODPOVED PODMNOZINY --> {dotaz_1}")

# XI. KROK
# S.isdisjoint()
# Jsou studenti v prom. *NOVI_STUDENTI* uplne odlisne hodnoty nez jsou v setu *Astronomie*
NOVI_STUDENTI = {"Matous", "Monika", "Aneta"}
dotaz_2 = NOVI_STUDENTI.isdisjoint(set_astronomie)
print(f"ODPOVED ODLISTNOST --> {dotaz_2}")
