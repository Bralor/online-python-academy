<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 14

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Dulezite odkazy
- [Python Academy, lekce 14](https://engeto.com/cs/kurz/python-6/studium/FVHvYkaDTFahfXyiR8UNYQ/generatory-regex/generatory/generatorove-funkce)
- [Minula lekce, repozitar](https://github.com/Bralor/python_academy/tree/master/lesson13)
...


# Co nas ceka?
Cilem dnesni lekce bude seznameni se s tzv. __generatory__. Povedet si, co to je generator v Pythonu, jak jej muzu vytvorit a proc bych to mel pouzivat? Dalsi funkcionalitu priblizime na konkretnich prikladech. V zaveru lekce si ukazeme nove znalosti demonstrujeme pomoci prikladu.

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

## Generatory
Takovy generator v Pythonu si pro zjednoduseni muzeme predstavit jako 

## Duvod?
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
Podobne jako v vyse zmineme [prikladu](##-duvod?) tu mame smycku. S velkym rozdilem a to je klicovy vyraz __yield__. Tento klicovy vyraz funguje podobne jako __return__ tak, ze nam "poda" hodnotu. Nicmene neukonci funkci tak, jako __return__.

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

## Pomoci generatorovych funkci



