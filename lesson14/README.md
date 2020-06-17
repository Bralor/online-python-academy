<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 14

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Dulezite odkazy
- [Python Academy, lekce 14](https://engeto.com/cs/kurz/python-6/studium/FVHvYkaDTFahfXyiR8UNYQ/generatory-regex/generatory/generatorove-funkce)
- [Minula lekce, repozitar](https://github.com/Bralor/python_academy/tree/master/lesson13)
- [Funkce zip()](https://docs.python.org/3/library/functions.html#zip)
- [Prvky generatoru](https://docs.python.org/2.5/whatsnew/pep-342.html)


# Co nas ceka?
Cilem dnesni lekce bude seznameni se s tzv. __generatory__. Povedet si, co to je generator v Pythonu, jak jej muzu vytvorit a proc bych to mel pouzivat? Dalsi funkcionalitu priblizime na konkretnich prikladech. V zaveru lekce si ukazeme nove znalosti pomoci prikladu.

# Prerequisites
- python 3.6+
- text. editor
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)

# Teoreticke materialy
## Rekapitulace
1. __Iterovatelny objekt (iterable)__ - jde o objekt, ktery muzeme udaj za udajem prochazet.
```python
for <promenna> in <iterable>:
    <sada_kodu>
```

2. __Iterator__ - objekt, ktery vznikne, kdyz do funkce iter() vlozime iterovatelny objekt. Iterator pouziva metodu _next()_, kterou si "podava" jeden udaj za druhym.
```python
VZOREK1 = 1234567890    # int neni iterovatelny obj.
VZOREK2 = "1234567890"  # str je iterovatelny obj.

>>> iter(VZOREK1)   # -> TypeError
>>> iter(VZOREK2)   # -> vytvoreni iteratoru
```

3. __Generator__ - je v podstate funkce, ktera vraci iterator

# Generatory
## Proc je pouzivat?
V nasich pocitacich mame urcity konecny pocet pameti. Kdyz nas program spoustime, nacitame jej do teto pameti. Tzn. vsechno ukladani, promenne aj. ukladame v nasi pameti.

Priklad:
```python
pokus = [cislo**2 for cislo in range(1000000000)]

for cislo in pokus
    print(cislo)

MemoryError/Killed
```

V vyse nachystane uloze totiz rozsah s hodnotami pouze neprochazim, ale soucasne umocnuji a ukladam. Hromadu ukonu v kazdem kroce.

## Generatorova funkce
Resenim techto narocnejsich procesu byva prave generatorova funkce.
```python
def generator(cislo: int) -> int:
    for cislo in range(cislo):
        yield i**2

g = generator(1000000000)

for i in g:
    print(i)
```
Podobne jako v vyse zmineme [prikladu](##-proc-je-pouzivat?) tu mame smycku. Novy je klicovy vyraz __yield__. Tento vyraz funguje podobne jako __return__ tak, ze nam "poda" hodnotu. Nicmene neukonci funkci tak, jako __return__. Spis ji docasne pozastavi.

## Vysledek?
Hlavni vyhoda generatorove funkce je tedy fakt, ze jakmile jej "nakrmime" cisly, okamzite nam poda vysledne hodnoty. Ale __NEUKLADA__ je. Sledujme rozdil ve vyuziti pameti v nasledujici uloze.

Priklad:
```python
def seznam_lidi(pocet_lidi: int) -> List[dict]:
    vysledek = []
    for i in range(pocet_lidi):
        osoba = {
                    'id': i,
                    'jmeno': random.choice(JMENA),
                    'predmet': random.choice(PREDMETY)
                }
        vysledek.append(osoba)
    return vysledek

def generator_lidi(pocet_lidi: int) -> Generator[dict]:
    for i in range(pocet_lidi):
        osoba = {
                    'id': i,
                    'jmeno': random.choice(JMENA),
                    'predmet': random.choice(PREDMETY)
                }
        yield osoba
```

# Prakticka uloha
## Hon na mys
Praktickou ulohou, bude spise graficky vystup. V nem se budeme nejprve snazit popsat pouziti generatoru. Nasledne zdanlive jednoduchou ulohu zkomplikuje o prvek nahody.

## Importujeme moduly
Nasim pomocnym modulem bude mimo jine modul _gameworld.py_ (autor: Sebastiaan Mathôt). Pomocny modul vykresluje mrizku a emoji pro kocku a mys.

```python
#!/home/mholinka/projects/python_academy/env/bin/python
"""Lekce #14 - Uvod do programovani, generatory"""

import time
from gameworld import Animal, draw_grid
```

## Pomoci generatorovych funkci
Nejprve vytvorime gen. funkce _kocky_ a _mysi_, ktere nam umozni vykreslovat pozici obou zvirat.

```python
def kocky():
    """Generator pro pozici kocky v mrizce"""

def mysi():
    """Generator pro pozici mysi v mrizce"""    
```

## Built-in zip()
Funkce [zip()](#-dulezite-odkazy) umoznuje sbirat udaje ze dvou iterovatelnych objektu a spojovat je k sobe (vraci iterator).

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
```

## Vyzkousime prvni cast
Pojdme nas program spustit a rekapitulovat, co jsme dosud zapsali.

## Jdeme dal!
Budeme chtit pridat do naseho programu prvek nahody! Aby si mohla mys bezet kam se jit zachce. Chceme dosahnout toho, aby generator pro mys pochopil, ze se jej kocka snazi pronasledovat a soucasne rict mysi, aby se od kocky snazila vzdalovat. Jinymi slovy, nase prvni cast generuje pozici kocky a mysi a vysledek vykreslujeme. My, chceme program upravit tak, abychom vysledek vykreslili a vratili jej zpet do generatoru, ktery vyhodnoti dalsi krok.

```python
...
import random
...
```
## Nova smycka
Komunikace mezi generatory pomoci for loops probihat nebude. Naopak chceme se spise spolehnout na nekonecnou smycku.

```python
while True:
    ...
    break
```

## Jak zavolame prislusne gen. funkce?
Vytvorim promenou, ktera obsahuje iterator, ktery nam podava zvirata.

```python
iterator_kocky = kocky()
iterator_mysi = mysi()
```

## Jake spustime generatory?
Jak teda dostanu konkretni zvire a jeho polohu pomoci nasich iteratoru? Pomoci metody generatoru __send()__.

```python
...
kocka = iterator_kocky.send(None)
mys = iterator_mysi.send(None)

while True:
    ...
```

## Metoda generatoru send()
Tato metoda slouzi k predani hodnoty do generatorove funkce.

Priklad:
```bash
def zdvojnasob():
    while True:
        x = yield
        yield x * 2
>>> generator = zdvojnasob()
>>> next(generator)     # dobehne az k prvni yieldu
>>> generator.send(10)  # dosadi 10 jako x = 10
20
>>> next(generator)     # dobehne k dalsim yieldu
>>> generator.send(5)   # dosadi 5 jako x = 5    
10
...
```

Pokud tedy potrebujeme spustit nas generator. Muzeme pouzit metodu _send()_. Jako argument dosadime hodnotu, kterou chceme uplatnit v prvnim __yield__ ohlaseni. V nasem prikladum, chceme generator jen spustit a proto vlozime __None__.

## StopIteration
Vypada, ze v tomto okamziku dostavame chybu... Nas generator vycerpal hodnoty a skoncil.

```python
except StopIteration:
    break
```

## Vedi o sobe?
Zatim muzeme rict, ze kocka i mys drzi smer, ktery jsme jim predepsali. Tzn. zatim v podstate pouze zobrazujeme souradnice z obou generatoru. Abychom donutili generatory k cinnosti staci jim poslat __None__. Nicmene, aby dostali pozadovany stav (tedy, ze mys utika a kocka jde za ni), musime predchystat situaci, kdy budou generatory [komunikovat](##-metoda-generatoru-send()).

```python
try:
    kocka = iterator_kocky.send(mys)
    mys = iterator_mysi.send(kocka)
```

## Vytvorime pocatecni bod
Zacneme u kocky. Zatim definice tohoto generatoru umoznuje, pouze pohyb ve smeru vertikalnim. Aby se mohla vykreslovat, tedy "pohybovat" v ruznych smerech, potrebujeme lepsi smycku.

```python
kocka = Animal(row=2, col=2)
```
## Upresnime pohyb lovce
Kocka, jako lovec, musi pronasledovat mys. Tudiz pokud mys unika smerem dolu (zvetsujeme hodnotu __row__), potom musime zvetsit hodnotu __row__ i u kocky a obracene. Obdobne to bude platit po __col__.

```python
if mys.row > kocka.row:
    kocka = move(kocka, row=1)
```

## Upresnime pohyb mysi
Krome startovni pozice plati vse, co u generatorove funkce s kockou. Pokud se dostane kocka na stejny radek jako mys (__row__), pouzijeme random.choice(), at za nas rozhodne, kam se ma mys vydat.

## Konec lovu
Doplnim ukoncuji podminku, ktera zakonceni generovani jednotlivych pozic v nasi mrizce. Tedy, pokud si budou souradnice kocky a mysi odpovidat musim nejak cely proces ukoncit.

```python
if mys.row == kocka.row and mys.col == kocka.col:
    draw_grid(kocka, mys)
    raise RuntimeError
```

# Souhrn ke generatorum
1. Je rozumne pouzivat generator pro snizeni naroku na pamet
2. Muzeme zuzitkovat rozumne nekonecne smycky s while
3. Muzeme pouzivat pomoci zkraceneho zapisu
