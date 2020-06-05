![](../images/engeto.png)
# Python academy, lesson 07

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/bVSNtM2eT7uxBrBeS8n14w/funkcni-ramce-a-vstupy/prehled-lekce)

# Dnesni ukol
Ucelem dnesni lekce je rozsirit znalosti o funkcich v Pythonu. V minule lekci jsme si rekli neco o funkcich na uvod a aplikovali to na skutecne uloze, kde jsme pouzili prave nasi prvni vlastni funkci. Dnes se budeme snazit naucit zapis pomoci vice funkci, na sobe zavislych.

# Kalkulator
Praktickym prikladem ke dnesni teorii bude napsat vlastni kalkulacku. Na teto uloze se budeme snazit veskere koncepty aplikovat a ukazat si praci s vice ruznymi funkcemi, ktere spolu komunikuji.

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
DOSTUPNE OPERACE: 
-------------------------
+|-|*|/|prum|^
-------------------------
OPERACE ('q'- konec): +
CISLO 1: 1234
CISLO 2: 866
-------------------------
1234 + 866 = 2100
-------------------------
DOSTUPNE OPERACE: 
-------------------------
+|-|*|/|prum|^
-------------------------
OPERACE ('q'- konec): q
Doufam, ze se Vam kalkulacka libila! ^.^
```

# Prerequisites
- python 3.6.9+
- text. editor
- [while smycky](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [for cyklus](https://github.com/Bralor/python_academy/tree/master/lesson05#for-cyklus)
- [funkce](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
Potrebne promenne:
```
NABIDKA = "DOSTUPNE OPERACE: "
OPERACE = "+", "-", "*", "/", "prum", "^"
ODDELOVAC = "-" * 25
```

# Postup
Opet si otevreme novy soubor *calculator.py* a nakopirujeme sablonu nize:
```
#!/usr/bin/env python3
"""Lekce #7 - Uvod do programovani, kalkulacka"""

# I. KROK
# Zadame pomocne promenne
XXX

# II. KROK
# Vytvorit hlavni ridici funkci

# III. KROK
# Uvadeci funkce

# IV. KROK
# Rozcestnik funkci

# V. KROK
# Potrebujeme dva vstupy

# VI. KROK
# Resime zakladni aritmeticke operatory

# VII. KROK
# Potrebujeme radu cisel pro prumer

# VIII. KROK
# Pocitam prumer z pomocne promenne

# IX. KROK
# Umocnim cislo, exponentem

# ad. II. KROK
# Volam svoji hlavni funkci
```

# Cheatsheet s priklady
## Metoda .join()
Metoda vracejici retezec spojeny preddefinovanym symbolem.

Priklad
```
SLOVA = ['mesto', 'more', 'kure' ,'staveni']
"+++".join(SLOVA)
>>>
'mesto+++more+++kure+++staveni'
```

## Jmenne prostory a.k.a. namespaces
Rikali jsme si, ze promenna je vytvorena, pokud ji priradime hodnotu. Pomoci konceptu [jmennych prostoru](https://engeto.com/cs/kurz/online-python-akademie/studium/cfXXcPh0TTaF8DGihbsP2A/funkcni-ramce-a-vstupy/funkcni-ramce/co-je-to-ramec), tedy namespace evidujeme/spravujeme tyto namapovana jmena promennych a jejich hodnot. V Pythonu obecne ma kazdy balicek, funkce, modul svoje vlastni jmenne, aby zabranilo potencialni kolizi se jmeny promennych.

Teorie:
```
JMENO = "Matous"
VEK = 56

# ilustrace jmenneho prostredi
namespace = {
    "JMENO": "Matous",
    "VEK": 56
}
```
[Priklad](https://engeto.com/cs/kurz/online-python-akademie/studium/gELVr5MdQUy9LQgqXFMKNw/funkcni-ramce-a-vstupy/funkcni-ramce/zmena-built-in-promennych):
```
# built-in sum()
HODNOTY_1 = [1, 2, 4, 8, 16, 32]
HODNOTY_2 = [1, 2, 4, 8, 16, 32, 64]
sum(HODNOTY_1)  # dostanu vystup, ktery secte vsechny cisla v prom.

# moje vlastni promenna sum
sum = 63

# opet potrebuji sum()
sum(HODNOTY_2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

```
## Prostredi v Pythonu
Aby byla aplikace jmennych prostoru osetrena, muzeme v Pythonu vymezit 4 druhy [prostredi](https://engeto.com/cs/kurz/online-python-akademie/studium/00LmkBYlTIOnTYVXRau8PQ/funkcni-ramce-a-vstupy/funkcni-ramce/built-in-a-globalni-ramec). Jejich rozdeleni je vytvoreno zamerne, aby Python vedel postup, kterym promenne hledat a jak/komu jej zpristupnit.

Rozdeleni LEGB:
1. Zabudovana jmena (built-in scope) - pr. def, str, sum
2. Globalni (global scope) - pr. promenne v ramci souboru
3. Uzavrene prostredi (enclosing scope) - funkce ve funkci
4. Lokalni (local scope) - pr. parametry funkci, promenne ve func

[Priklad](https://engeto.com/cs/kurz/online-python-akademie/studium/lue9xKseQ6OSse_8dK0O5Q/funkcni-ramce-a-vstupy/funkcni-ramce/stejnojmenne-promenne):
```
>>> jmeno = "Marek"
>>> def func1(jm):
...     jmeno = jm
...     print(jmeno)
... 
>>> func1('Matous')
Matous
>>> print(jmeno)
'Marek'
```
