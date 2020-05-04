![](../images/engeto.png)
# Python academy, lesson 05

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/jZRrTgDlSMyRKeVTUD6vDA/range-a-smycka-for/obsah-a-prerekvizity)
- [Sorted()](https://docs.python.org/3/library/functions.html#sorted)

# Dnesni ukol
V ramci dnesni lekce budeme chtit dokoncit teorii o smyckach v Pythonu. Rekneme si obecne o jejich pouziti, doplnujici zpusob prace s nimi. Nakonec bychom si jeste ve zkratce ukazali praci s gitem.

# Hledani nejcastejsich slov
Na uvod mame nahodny text, s nimz dnes budeme pracovat. Cilem bude zjistit pet nejcastejsich slov, ktere se v textu vyskytuji.

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
=======================
SLOVO: *he*, VYSKYT: 6x
=======================
SLOVO: *in*, VYSKYT: 5x
=======================
SLOVO: *up*, VYSKYT: 4x
=======================
SLOVO: *of*, VYSKYT: 3x
=======================
SLOVO: *ye*, VYSKYT: 3x
```
# Prerequisites
- python 3.6.9+
- text. editor
- [while cyklus](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [slovnik](https://github.com/Bralor/python_academy/tree/master/lesson03#slovnik)
- [podminky](https://github.com/Bralor/python_academy/tree/master/lesson02#podminkovy-zapis)

Pomocne promenne:
```
#!/usr/bin/env python3
""" Lekce #5 - Uvod do programovani, hledac slov """

# I. KROK
# Zadani nasi ulohy
XXXXXX

# II. KROK
# Prochazime promennou *text*

# III. KROK
# Rozdelime promennou *text*, abych prochazeli slova

# IV. KROK
# Zakomentuj krok 2.
# Prochazime znovu

# Zkusime napsat pomoci *while* cyklu

# VI. KROK
# Zakomentujeme krok 4.
# Vyzkousime seznamovou komprehenci
# Utridime slova do slovniku podle vyskytu

# VII. KROK
# Vytvorim pomocnou promennou *vyskyt_slov*
# Pocitam vyskyt slov

# VIII. KROK
# Vybere 5 nejcastejsich slov

# IX. KROK
# Upravit vystup abych mel hodnoty rozdelene


```

# Cheatsheet s priklady
# For cyklus
Jde o dalsi zpusob, kterym v Pythonu muzu opakovat casti kodu. Zatim co *while* se opakoval, pokud byla explicitne zadana podminka vyhodnocena jako *True*, for cyklus bezi, dokud neprojde celou zadanou sadu udaju. Pripadne, pokud jej jinak neukoncime.

Teorie:
```
for <libovolny_parametr> in <sada_udaju>:
    <telo_smycky>
```

Priklad:
```
>>> JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]
>>> 
>>> for jmeno in JMENA:
...     print(jmeno)
... 
Helmut
Helga
Harold
Hammet
Hetfield
```

# Metoda stringu split()
Metoda *.split(sep=None, maxsplit=-1)* vraci seznam ze zadane promenne. Tuto zadanou promennou rozdeli podle zadaneho oddelovace.

Priklad:
```
VETA1 = "Urcite na Linuxech. S casem, ktery nam zustane se budu gitu zrejme v Pycharmu."
print(VETA1.split())
print(VETA1.split("."))
print(VETA1.split(".", maxsplit=1))
```

# Metoda stringu strip()
Tato metoda vraci kopii zadaneho retezce (promenne), kdy z puvodniho udaje odstrani explicitne definovane symboly na zacatku/konci zadane promenne

Priklad:
```
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov, která však postrádají myšlenku a znalost.   "
VETA3 = "Není trapnější hloupost,..."
print(VETA2.strip())  # odstranime uvodni a zaverecne mezery
print(VETA3.strip(".,"))  # odstranime uvodni a zaverecne carky/tecky
```

# Seznamova komprehence
Jde o skladebni predpis na vytvoreni seznamu. Je to dalsi zpusob jak pouzit *for cyklus* ve zkracenem zapisu (nemusi byt prehlednejsi a pouzitelny vzdy).

Priklad:
```
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov, která však postrádají myšlenku a znalost.   "
vycisteny_seznam = [slovo.strip(",.") for slovo in VETA2.split()]
print(vycisteny_seznam)
```
# Trideni
Pomoci zabudovane funkce *sorted()* muzeme docilit serazeni definovane promenne.

Priklad:
```
HODNOTY = (1, 3, 4365, 23, 12, 90, 34, 7)
print(sorted(HODNOTY))

VYSKYT = {"A": 3, "B": 6, "C": 1, "D": 10}
print(sorted(VYSKYT), key=VYSKYT.get, reversed=True)
```
# Nestovane smycky for
Princip nestovani, zanorovani je v podstate vkladani jedne smycky (vnitrni) do nejake jine (vnejsi).

Priklad:
```
for number in range(0, 5):
    print("=" * 14)
    print(f"Radej cislo {number}")
    print("=" * 14)

    for cislo_bunky in range(1, 5):
        print(f"Bunka cislo {cislo_bunky}")
# Vystup
--------------
RADEK cislo 0
--------------
BUNKA cislo 1
BUNKA cislo 2
BUNKA cislo 3
BUNKA cislo 4
--------------
RADEK cislo 1
--------------
BUNKA cislo 1
BUNKA cislo 2
BUNKA cislo 3
BUNKA cislo 4
--------------
RADEK cislo 2
--------------
BUNKA cislo 1
BUNKA cislo 2
BUNKA cislo 3
BUNKA cislo 4
--------------
RADEK cislo 3
--------------
BUNKA cislo 1
BUNKA cislo 2
BUNKA cislo 3
BUNKA cislo 4
--------------
RADEK cislo 4
--------------
BUNKA cislo 1
BUNKA cislo 2
BUNKA cislo 3
BUNKA cislo 4

```
# Range()

# Enumerate()

