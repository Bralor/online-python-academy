#!/usr/bin/env python3
"""
Lekce c.6 - trideni typu bytu
# P1
# Vyscrapovane informace z realitek
# Vlozime jej jako viceradkovy retezec
DATA = '''
byt 0001,55 m2,Olomouc,ul.Heyrovského,
byt 0003,65 m2,Olomouc,ul.Novosadský dvůr,
byt 0004,75 m2,Olomouc,ul.Wolkerova,
byt 0004,68 m2,Olomouc,ul.Zikova,
byt 0001,36 m2,Olomouc,ul.Nová Ulice,
byt 0003,46 m2,Olomouc,ul.Nové sady,
byt 0004,75 m2,Olomouc,ul.Nová Ulice,
byt 0003,42 m2,Olomouc,ul.Nová Ulice,
byt 0005,107 m2,Olomouc,ul.Nová Ulice,
byt 0003,74 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Nešverova,
byt 0002,55 m2,Olomouc,ul.Dělnická,
byt 0004,59 m2,Olomouc,ul.Zirmova,
byt 0007,92 m2,Olomouc,ul.Nová Ulice,
byt 0002,52 m2,Olomouc,ul.Nová Ulice,
byt 0004,76 m2,Olomouc,ul.Nová Ulice,
byt 0002,81 m2,Olomouc,ul.Nová Ulice,
byt 0003,64 m2,Olomouc,ul.Za vodojemem,
byt 0007,113 m2,Olomouc,ul.Jihoslovanská,
byt 0005,94 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Rošického,
byt 0003,75 m2,Olomouc,ul.Rošického,
byt 0004,48 m2,Olomouc,ul.Handského,
byt 0004,68 m2,Olomouc,ul.Komenského,
byt 0003,61 m2,Olomouc,ul.Jarmily Glazarové,
byt 0004,39 m2,Olomouc,ul.Přichystalova,
byt 0003,70 m2,Olomouc,ul.Foerstova,
byt 0005,61 m2,Olomouc,ul.Nová Ulice,
byt 0007,88 m2,Olomouc,ul.Nová Ulice,
byt 0003,92 m2,Olomouc,ul.U cukrovaru,
byt 0003,56 m2,Olomouc,ul.U cukrovaru,
byt 0004,56 m2,Olomouc,ul.Paseka,
byt 0002,74 m2,Olomouc,ul.Rokycanova,
byt 0007,116 m2,Olomouc,ul.U cukrovaru,
byt 0004,59 m2,Olomouc,ul.Řezáčova,
byt 0004,100 m2,Olomouc,ul.Libušina,
byt 0003,64 m2,Olomouc,ul.Řezáčova,
byt 0001,33 m2,Olomouc,ul.Libušina,
byt 0006,87 m2,Olomouc,ul.Černá cesta,
byt 0007,95 m2,Olomouc,ul.Kaštanová,
byt 0003,74 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nová Ulice,
byt 0004,86 m2,Olomouc,ul.Hněvotínská,
byt 0002,67 m2,Olomouc,ul.Polská,
byt 0007,120 m2,Olomouc,ul.Dvořákova,
byt 0004,90 m2,Olomouc,ul.Dvořákova,
byt 0004,86 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nešverova,
byt 0001,45 m2,Olomouc,ul.Zirmova,
byt 0006,114 m2,Olomouc,ul.Přichystalová,
"""

# P2
# Definujeme vzor, jak chceme data prevest
# Vzor prevadeni:
converting = {
    "byt 0001": "1+1",
    "byt 0002": "2+1",
    "byt 0003": "2+kk",
    "byt 0004": "3+1",
    "byt 0005": "3+kk",
    "byt 0006": "4+1",
    "byt 0007": "4+kk",
}

# P3
# Potrebujeme data rozdelit a upravit
spl_data = []

for line in DATA.split("\n"):
    flat_id, *rest = line.split(",")

    if line:
        spl_data.append([flat_id, *rest[:-1]])

# P4
# Potrebujeme menit oznaceni bytu za typ bytu
def classification(type, conv):
    return conv.get(type, None)


# P5
# Vytvorime smycku, kde aplikujeme nasi funkci
for line in spl_data:
    flat_id, *rest = line
    conv_type = classification(flat_id, converting)
    updated_l = conv_type, *rest
    print(updated_l)
