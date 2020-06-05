![](../images/engeto.png)
# Python academy, lesson 09

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/5wIl0U-rRCSiJvbvBTPRUA/zachyceni-chyb/uvod-do-kurzu)
- [Formatovani retezcu](https://realpython.com/python-f-strings/)

# Dnesni ukol
V dnesni lekci se budeme bavit o potencialnich chybach uvnitr naseho kodu.

# Zkontroluj vstupni data
Nas dnesni program bude mit za ukol kontrolat datove typy, ktere do nej nacteme. Budeme chtit vedet, jestli vstupni udaje obsahuji pouze hodnoty, ktere lze prevadet na celociselne udaje (integer), prip. jestli data neobsahuji nejake nezadouci typy (nelze prevest na integer).

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
---------------------------------------
292436 --> OK, pokracuji...
---------------------------------------
731088 --> OK, pokracuji...
---------------------------------------
NEKONVERTOVATELNE --> ggrrrr, ValueError
---------------------------------------
875875 --> OK, pokracuji...
---------------------------------------
893647 --> OK, pokracuji...
```

# Prerequisites
- python 3.6.9+
- text. editor
- [while smycky](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [for smycky](https://github.com/Bralor/python_academy/tree/master/lesson05#for-cyklus)
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)

# Postup
Opet si otevreme novy soubor *check_type.py* a nakopirujeme sablonu nize:
```
#!usr/bin/env python3
"""Lekce #9 - Uvod do programovani, kontrola cisel"""

# I. KROK
# Vytvoreni hlavni funkce

# II. KROK
# Potrebujeme nacist soubor s udaji

# III. KROK
# Ciselne udaje zbavime symbolu pro novy radek "\n"

# IV. KROK
# Udaj naformatovat dle dohodnuteho vzoru

# V. KROK
# Kontrolujeme spravny vstupni datovy typ

# VI. KROK
# Napiseme funkci, ktera bude chtit zkontrolovat typ kazdeho detailu
# Pokud je to cislo, melo by byt zmenitelne pomoci funkce int()

# ad. I. KROK

```

# Cheatsheet s priklady
## Chyby v Pythonu
Ackoliv se staneme opravdovymi _pythonistas_, chybu udela prakticky kazdy. Chyby mohou zpusobit selhani naseho programu nebo minimalne nebude fungovat tak, jak ocekavame.

## Typy chyb
1. Syntakticke - jde o prohresek proti pravidlum skladebnich predpisu jazyka
2. Behove chyby - chyby, ktere se projevi az pri prekladani naseho kodu (delim nulou, pouzivam neco, co jeste neexistuje)
2. Logicke - funguje, ale jinak, nez ocekavame

## Vyjimka
Nicmene s chybami se pocita a proto je s nimi v Pythonu zachazeno jako s nejakymi objekty. Programatori jsou casto presvedceni, ze v jejich programech se chyba objevi jen zridka a proto je hromadne oznacuji jako vyjimky. Vyjimka je zase nejaky objekt, ktery nastane pokud se pri vykonavani programu objevi nejaka chyba (error) a nebo je nejaka cast zkratka podezrela (warning).

Priklad:
```
JMENO = "Matous"
if JMENO
File "<stdin>", line 1
    if JMENO
           ^
SyntaxError: invalid syntax
```

## Co s nimi?
1. Syntakticke chyby je nutne odstranit --> debugovat
2. Logicke chyby (+ behove chyby) je mozne hlidat --> error handling

## Debugovani
Povime si o nem a jeho metodach vice ve stredu

## Zachazeni s chybami
S logickymi chybami si lze poradit. Na celou operaci existuje opet presne popsana skladba, kterou muzeme odchytavat jednotlive chyby, nebo skupinu chyb. 

Teorie:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky>:
    <toto_se_stane_pokud_dostaneme_vyjimku>
```

Priklad:
```
def input_int() -> int:
    while True:
        try:
            x = int(input("VLOZTE CELE CISLO: "))
            break
        except ValueError:
            print("Neni cele cislo, zkuste znovu...")
    return x

print(f"\nZADALI JSTE CISLO: {input_int()} ")
```

## Vice vetvi *except*
Chyby muzeme specifikovat pomoci vice vyjimek (pripadne doplnit/zkratit aliasem)

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>

except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>
```

## Vetev *else*
Pokud nedojde k vyhodnoceni ve vetvi _try_ s vyjimkou. Proved vetev *else*

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>

except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>

else:
    <toto_proved_pokud_nedostaneme_vyjimku>
```

## Vetev *finally*
At uz vyhodnoceni bude s vyjimkou ci bez ni, proved to, co obsahuje vetev *finally*.

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky>:
    <toto_se_stane_pokud_dostaneme_vyjimku>

finally:
    <toto_proved_pokazde>
```
