![](../images/engeto.png)
# Python academy, lesson 08

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/5BmOjpMWQXetDW5lEWZVlw/formatovani-stringu-a-textove-soubory/prehled-lekce)

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
## Jake mame zpusoby?
## Prace se soubory pomoci Pythonu
## Kontextovy manazer
