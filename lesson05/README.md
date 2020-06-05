![](../images/engeto.png)
# Python academy, lesson 05

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/jZRrTgDlSMyRKeVTUD6vDA/range-a-smycka-for/obsah-a-prerekvizity)
- [Sorted()](https://docs.python.org/3/library/functions.html#sorted)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)

# Dnesni ukol
V ramci dnesni lekce budeme chtit dokoncit teorii o smyckach v Pythonu. Rekneme si obecne o jejich pouziti, doplnujici zpusob prace s nimi. Nakonec bychom si jeste ve zkratce ukazali praci s gitem.

# Hledani nejcastejsich slov
Spolecne si zadame nahodny text, s nimz dnes budeme pracovat. Cilem bude zjistit pet nejcastejsich slov, ktere se v textu vyskytuji.

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
==========================
1, SLOVO: *he*, VYSKYT: 6x
==========================
2, SLOVO: *in*, VYSKYT: 5x
==========================
3, SLOVO: *up*, VYSKYT: 4x
==========================
4, SLOVO: *of*, VYSKYT: 3x
==========================
5, SLOVO: *ye*, VYSKYT: 3x
```
# Prerequisites
- python 3.6.9+
- text. editor
- [while cyklus](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [slovnik](https://github.com/Bralor/python_academy/tree/master/lesson03#slovnik)
- [podminky](https://github.com/Bralor/python_academy/tree/master/lesson02#podminkovy-zapis)

Pomocne promenne:
```
TEXT = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual. 
"""
```

# Postup
Opet si otevreme novy soubor *.py* a nakopirujeme sablonu nize:
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
## For cyklus
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

## Metoda stringu split()
Metoda *.split(sep=None, maxsplit=-1)* vraci seznam ze zadane promenne. Tuto zadanou promennou rozdeli podle zadaneho oddelovace.

Priklad:
```
VETA1 = "Urcite na Linuxech. S casem, ktery nam zustane se budu gitu zrejme v Pycharmu."
print(VETA1.split())
print(VETA1.split("."))
print(VETA1.split(".", maxsplit=1))
```

## Metoda stringu strip()
Tato metoda vraci kopii zadaneho retezce (promenne), kdy z puvodniho udaje odstrani explicitne definovane symboly na zacatku/konci zadane promenne

Priklad:
```
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov, která však postrádají myšlenku a znalost.   "
VETA3 = "Není trapnější hloupost,..."
print(VETA2.strip())  # odstranime uvodni a zaverecne mezery
print(VETA3.strip(".,"))  # odstranime uvodni a zaverecne carky/tecky
```

## Seznamova komprehence
Jde o skladebni predpis na vytvoreni seznamu. Je to dalsi zpusob jak pouzit *for cyklus* ve zkracenem zapisu (nemusi byt prehlednejsi a pouzitelny vzdy).

Priklad:
```
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov, která však postrádají myšlenku a znalost.   "
vycisteny_seznam = [slovo.strip(",.") for slovo in VETA2.split()]
print(vycisteny_seznam)
```
## Trideni
Pomoci zabudovane funkce *sorted()* muzeme docilit serazeni definovane promenne.

Priklad:
```
HODNOTY = (1, 3, 4365, 23, 12, 90, 34, 7)
print(sorted(HODNOTY))

VYSKYT = {"A": 3, "B": 6, "C": 1, "D": 10}
print(sorted(VYSKYT), key=VYSKYT.get, reversed=True)
```
## Nestovane smycky for
Princip [nestovani](https://engeto.com/cs/kurz/online-python-akademie/studium/HX7RYlaNSk2AjSbGAM_kXw/range-a-smycka-for/smycka-for/vnorene-smycky), zanorovani je v podstate vkladani jedne smycky (vnitrni) do nejake jine (vnejsi).

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
## Range()
Je v podstate [nezmenitelny datovy typ](https://engeto.com/cs/kurz/online-python-akademie/studium/PHnlRhS8RQK7xyKhRoEGlA/range-a-smycka-for/datovy-typ-range/range-vytvareni-a-princip), podobne jako string nebo tuple. Jde o interval hodnot, ktery se velice casto pouziva prave u for cyklu.

Priklad:
```
# range(pocatek, konec-1, krok)
# 1. zpusob
print(list(range(10)))

# 2. zpusob
print(list(range(1, 10)))

# 3. zpusob
print(list(range(1, 10, 2)))
```

## Enumerate()
Opet zabudovana funkce slouzici jako nejake [pocitadlo](https://engeto.com/cs/kurz/online-python-akademie/studium/wU-iRPKaQluG8Jz2HRA82A/range-a-smycka-for/smycka-for/for-loop-enumerate). Vraci nam tuply, ve kterych je v paru ulozeno cislo (poradove) a hodnota.

Priklad:
```
JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]
ocislovane = enumerate(JMENA, 1)
print(list(ocislovane))

for cislo, jmeno in enumerate(JMENA, 1):
    print(f"{cislo}.: {jmeno}")
```

# Cheatsheet, Git
## Co to je Git?
Open-source [verzovaci system](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/studium/FlBFHaGbRGaeMDpPH9S4Yw/rychlokurz/ide-vs-terminal). Umoznuje verzovat zmeny naseho projektu, zaznamenava historii, umoznuje kolaboraci atd.

## Jak zacit?
1. Vytvorit si vlastni GitHub ucet [zde](https://github.com/)
2. Vytvorit novy repozitar (pravy horni roh obrazovky)
3. Vytvarim VZDALENY repozitar
4. Download zip/ Pycharm --> VCS --> Get from version control
5. Nova pracovni vetev
6. Commit --> popis lokalnich zmen + push
7. Zmena na vzdalenem repozitari
8. git pull
9. Zmenim, co je nutne opravit --> add + commit + push
10. Vytvorim zadost o spojeni s hlavni master vetvi
