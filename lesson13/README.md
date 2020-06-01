![](../images/engeto.png)
# Python academy, lesson 13

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy, lekce 13](https://engeto.com/cs/kurz/python-5/studium/Fefwhy-AQ3WsXPnmjsUH5A/iteracni-protokol-comprehensions/iteracni-protokol/co-je-to-protokol)
- [Minula lekce, repo](https://engeto.com/cs/kurz/online-python-akademie/studium/ELexreXFQqOfbmaZJIJpUQ/formaty-souboru/kviz/json)
- [JSON, obecne](https://www.json.org/json-en.html)
- [CSV, obecne](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Funkce map()](https://www.geeksforgeeks.org/python-map-function/)

# Dnesni ukol
1. Komprehence
2. Lambda
3. map()
4. filter()
5. reduce()
6. functools(?)

# <Nejspis_nebude>
Nase ukoly:
```
hlavni.py           # spousti cely kod
csv_funkce.py       # obsahuje funkce s csv
...
```

# <nejspis_nebude>

```
XXX
```

```
XXX
```

```
XXX
```

# Prerequisites
- python 3.6+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)
- [Funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)


# Cheatsheet s priklady
## Komprehence
### Uvodem
Teorie:
```python
# Klasicka smycka *for*
<promenna> = []

for <lib_vyraz> in <kolekce_udaju>:
    <promenna>.append(<lib_vyraz>)

# Seznamova komprehence
<promenna> = [<lib_vyraz> for <lib_vyraz> in <kolekce_udaju>]   # obecny zapis
dvakrat = [cislo * 2 for cislo in range(101)]                   # konkretni priklad
```

### Podminkou..
Teorie:
```python
# Klasicka smycka *for*
<promenna> = []

for <lib_vyraz> in <kolekce_udaju>:
    if <podminka>:
        <promenna>.append(<lib_vyraz>)

# Seznamova komprehence
<promenna> = [<lib_vyraz> for <lib_vyraz> in <kolekce_udaju> <podminka>]   # obecny zapis
dvakrat = [cislo * 2 for cislo in range(101) if cislo % 2 == 0]            # konkretni priklad
```

### Slozitejsi podminky
Teorie:
```python
<promenna> = [<lib_vyraz> if <podminka> else <lib_vyraz_2> for <lib_vyraz> in <kolekce_udaju>]      # obecny zapis
suda_licha = ["Suda" if cislo % 2 == 0 else "Licha" for cislo in range(1, 21)]                      # konkretni priklad
```

## Pro srovnani
```python
import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]
def get_price(txn):
    return txn * (1 + TAX_RATE)
def get_prices_with_map():
    return list(map(get_price, txns))
def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]
def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices

>>> timeit.timeit(get_prices_with_map, number=100)
2.0554370979998566
>>> timeit.timeit(get_prices_with_comprehension, number=100)
2.3982384680002724
>>> timeit.timeit(get_prices_with_loop, number=100)
3.0531821520007725
```
# Anonymni funkce
## Standarni definovane funkce
1. [Zahlavi](#important-links)
2. Sada kodu jako odsazena cast

## Bezejmenne funkce
Nemaji definovane vlastni jmeno. Pozname je pomocni klicoveho vyrazu _lambda_. Pouzivame je zejmena pokud potrebujeme pomoc funkce na kratkou dobu. Dost casto ji pouzivame v ramci klasicke funkce, kde pusobi jako prostrednik, ktery nam poskytne vysledek.

Priklad:
```python
# Pomoci funkce
def vrat_zbytek(cislo1: int, cislo2: int) -> int:
    return cislo1 % cislo2

>>> vrat_zbytek(5, 2)
1

# Pomoci anonymni funkce
zbytek = lambda cislo1, cislo2: cislo1 % cislo2
>>> print(zbytek(5, 2))
1
```

Teorie:
```python
lambda <argumenty>: <vyraz>     # obecne
lambda x, y: x ** y             # priklad
```
## Funkce map()
Specialni funkce, typicka pro funkcionalni programovani je funkce [_map()_](#important-links). Tato funkce potrebuje dva argumenty. Prvni, ktery rekne, na jakou funkci chci pomoci _map()_ aplikovat, druhy, ktery obsahuje iterovatelnou promennou.

Priklad:
```python
ZVIRATA = ["kocka", "pes", "orel", "prase", "veverka"]
list(map(lambda zvire: zvire.upper(), ZVIRATA))
```

Ukol:
```python
FAHRENHEIT = [("Berlin", 84.2), ("Cairo", 96.8), ("Buenos Aires", 66.2), ("Los Angeles", 78), ("Tokyo", 80.6), ("new York", 82.4), ("London", 71.6), ("Beijing", 89.6)]
F2C = lambda data: (data[0], round((5/9)*data[1] - 32, 2))
list(map(F2C, FAHRENHEIT))
```

## Funkce filter()
Dalsi funkce, ktera potrebuje nejakou funkci jako prvni argument a iterovatelnou promennou jako druhy argument.

Priklad:
```python
jen_suda = lambda cislo: cislo % 2 == 0
list(filter(jen_suda, range(0, 21)))
```
## Funkce reduce()
Tato funkce od verze Python3 neni mezi standartnimi built-in funkcemi. Tudiz je nutne ji importovat.

Priklad:
```python
import functools                # potom pouzijeme jako functools.reduce()
from functools import reduce    # .. reduce()
```

Stejne jako predchozi funkce pouzijeme argument, iterovatelnou promennou (objekt).

Priklad2:
```python
PRVOCISLA = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
nasobeni = lambda x, y: x*y
reduce(nasobeni, PRVOCISLA)
```
Nicmene...

Priklad3:
```python
vysledek = 1
for cislo in PRVOCISLA:
    vysledek *= cislo
```
