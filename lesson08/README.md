![](../images/engeto.png)
# Python academy, lesson 08

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/5BmOjpMWQXetDW5lEWZVlw/formatovani-stringu-a-textove-soubory/prehled-lekce)
- [Formatovani retezcu](https://realpython.com/python-f-strings/)


# Dnesni ukol
V dnesnim webinari nas ceka opet prakticka uloha, kde si budeme trochu hrat s formatovanim retezcu. Soucasne si rekneme neco o praci s textovymi soubory pomoci Pythonu.

# Hangman
Ukol, ktery bude treba vyresit, je napsat pomoci Pythonu hru obesenec. Soucasne je to skvela moznost aplikovat oba nase dnesni teoreticke celky. Zpusobu jak tuto hru napsat jak spousta. My zalezi samozrejme na mnozstvi znalosti, ktera mame k dispozici.

# Nas cil
Hra je hodne zalozena na komunikace pocitace a hrace. Takze aplikace nejakeho formatovani retezcu je vazne nutna. Vystup by na konci lekce mohl vypadat nasledovne:
```
ZADEJTE JMENO: Matous
---------------------------------------------
HRAC: Matous | STAV: _ _ _ _ _ | ZBYVA: 6.0 |
---------------------------------------------
HADEJ PISMENO: a
---------------------------------------------
HRAC: Matous | STAV: _ a _ _ _ | ZBYVA: 5.0 |
---------------------------------------------
HADEJ PISMENO: m
---------------------------------------------
HRAC: Matous | STAV: m a _ _ _ | ZBYVA: 4.0 |
---------------------------------------------
HADEJ PISMENO: n
---------------------------------------------
HRAC: Matous | STAV: m a n _ _ | ZBYVA: 3.0 |
---------------------------------------------
HADEJ PISMENO: g
---------------------------------------------
HRAC: Matous | STAV: m a n g _ | ZBYVA: 2.0 |
---------------------------------------------
HADEJ PISMENO: o
---------------------------------------------
HRAC: Matous | STAV: m a n g o | ZBYVA: 1.0 |
---------------------------------------------
VYBORNE, Matous! UHADL JSI!
```

# Prerequisites
- python 3.6.9+
- text. editor
- [while smycky](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [for smycky](https://github.com/Bralor/python_academy/tree/master/lesson05#for-cyklus)
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)

# Postup
Opet si otevreme novy soubor *hangman.py* a nakopirujeme sablonu nize:
```
#!/usr/bin/env python3
"""Lekce #8 - Uvod do programovani, obesenec"""

# I. KROK
# Hlavni funkce + vymyslet postup

# II. KROK
# Pridame hrace

# III. KROK
# Zvolime slovo pro hadani + nacteme jej

# IV. KROK
# Schovame jej!

# V. KROK
# Vypisujeme stav hry

# VI. KROK
# Hrac hada pismeno

# VII. KROK
# Posouzeni hadaneho pismena

# VIII. KROK
# Prubeh kazdeho kola

# IX. KROK
# Zaverecny vystup
```

# Cheatsheet s priklady
## Formatovani retezcu
Formatovani retezcu muzeme chapat jako operaci, ktera udela retezce vizualne prehlednejsi a umozni nam jednodussi manipulaci s nimi.

Teorie:
```
JMENO = "Zdenek"
VEK = 22
ADRESA = "Hrncirska 11, Brno"
VETA1 = "Jmenuji se " + JMENO + ". Je mi " + str(VEK) + " a momentalne jsem k dispozici na " + ADRESA
Jmenuji se Zdenek. Je mi 22 a momentalne jsem k dispozici na Hrncirska 11, Brno
```
## Jake mame zpusoby?
1. %-formatting, formatovaci vyraz
2. str.format(), formatovaci metoda
3. f-string, 

## Formatovaci vyraz
Jde o prapuvodni [formatovani](https://engeto.com/cs/kurz/online-python-akademie/studium/Xja-0nBPQvuISQQy8lJdYA/formatovani-stringu-a-textove-soubory/formatovani-stringu/vkladani-formatovaci-vyrazy) v Pythonu jiz od jeho zacatku.  

Priklad:
```
JMENO = "Lukas"
VEK = 26
"Ahoj, jmenuji se %s a je mi %d let" % (JMENO, VEK)
```
Dneska se jiz oficialne nedoporucuje pouzivat, jelikoz casto selhava, prip. nespravne zobrazuje tuple nebo slovniky. Soucasne je vypisovani az prilis podrobne.

## Formatovaci metoda
Od verze Pythonu 2.6 mame k dispozici dalsi zpusob pro [formatovani](https://engeto.com/cs/kurz/online-python-akademie/studium/hMIgHcH5TqaFSJJzKF9X7g/formatovani-stringu-a-textove-soubory/formatovani-stringu/formatovani-hodnot-metoda-format) retezcu.

Priklad:
```
JMENO = "Eliska"
VEK = 25
"Ahoj, jmenuji se {} a je mi {} let" .format(JMENO, VEK)
```
Pouziti je trochu mene explicitni. Nicmene zapis muze byt pri pouziti vice promennych porad dost narocny na vypisovani.

## F-string
Od verze Pythonu 3.6 mame dostupnou dalsi, jeste lepsi variantu pro rychle formatovani retezcu. 

Priklad:
```
JMENO = "Lucie"
VEK = 27
f"Ahoj, jmenuji se {JMENO} a je mi {VEK} let"
```
Syntaxe je velice strucna ale rozhodne ne na ukor citelnosti. Zvlada ruzne platne operace v Pythonu i volani funkci. Akorat u slovniku pamatovat, ze pokud pouziju napr. dvojite uvozovky u retezce, potom vnitrni musim psat jako jednoduche, abych ty puvodni predcasne neukoncoval.

## Prace se soubory pomoci Pythonu
### open()
Pro praci s konkretnim souborem uvnitr Python souboru jej musime nejprve nahrat do nejake promenne.

### Cist/zapisovat?
K ucelu, za kterym chceme soubor pouzivat musime vhodne specifikovat rezim/mod. Jakym soubor otevreme.
1. "w" - zapis
2. "r" - cteni
3. "a" - pripisuji informace bez smazani stavajiciho obsahu

### Pracujeme se souborem
1. .write() - zapisujeme
2. .read() - cteme

### close()
Jakmile dokoncime celou proceduru. Soubor zavirame! Soubor, ktery zapomeneme zavrit muze zpomalit nas program/programy. Neulozime nektere provedene zmeny, hypoteticky nebudeme moci otevrit dalsi soubory.

Priklad:
```
nacteny_soubor = open("slova.txt", "a+")  # nahraji soubor
nacteny_soubor.seek(0)  # nastavim kurzor na pozici 0
nacteny_soubor.read()  # prectu vse za nim
nacteny_soubor.write("jahoda")  # pridam dalsi radek
nacteny_soubor.close()  # ukoncim praci na souboru
```

## Kontextovy manazer
Varianta jak zoptimalizovat praci se soubory v Pythonu je pouzit kontextovy manazer. Tento proces totiz automaticky po otevreni a provedeni veskerych kroku soubor automaticky zavira.

Priklad:
```
with open("slova.txt", "r") as txt:
    obsah = txt.readlines()

>>> obsah  # vypise,co promenna obsahuje
```
