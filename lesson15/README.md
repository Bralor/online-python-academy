<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 15

# Dulezite odkazy
- [Python Academy, lekce 15](https://engeto.com/cs/kurz/online-python-akademie/studium/SYzMVJcBQSiagUXKNLvXfA/intro-do-scrapingu/slovo-na-uvod/co-te-ceka-v-teto-lekci)
- [Minula lekce, repozitar](https://github.com/Bralor/python_academy/tree/master/lesson14)
- [heroes III - cesko-slovenska liga](http://heroes3.cz/)

# Co nas ceka?
V ramci dnesniho webinare se budeme snazit _scrapovat_, tzn. ze za pomoci Pythonu se budeme snazit shromazdovat nejake informace umistene ve formatu html nekde na webu. Povime si o tom, jak tyto s temito udaji zachazet, jak je vyhledavat a jak je rozlisovat. Ve druhe casti lekce si ukazeme take praktickou ulohu s timto zamerenim.

# Prerequisites
- python 3.6+
- text. editor
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)
- [Csv](https://github.com/Bralor/python_academy/tree/master/lesson12)

# Teoreticke materialy
## Co bychom radi ukladali?
Vyhledam zamysleny web. Najdu co me zajima. Sledujme [odkaz](http://heroes3.cz/)


## V cem jsou nase udaje?
Data jsme nasly, jak je cist. Pravym tlacitkem mysi si rozbalime nabidku a v ni (Mozilla) najdeme __view page source__. Nyni koukame na zdrojovy kod. Vidime, ze jde o HTMLko.

```html
<!DOCTYPE html>
<html lang ="cs">
<head>
...
</head>
```

## HyperText Markup Language
Tvori strukturu webovych stranek. Je to hierarchicky usporadana struktura tvorena pomoci tagu. Z nasledujiciho vzoru muzeme rict, ktere tagy jsou rodicovske a ktere jejich potomci. My tuto strukturu na pozadi casto nevnimame. Prohlizec nam casteji zprostredkuje vyrenderovanou grafickou podobu.

Ukazka:
```html
<!-- Pouze vzorovy zapis -->
<div id="menu"><ul>
    <li>
        <a href="http://XXXXXXX.cz" title="">Homepage</a>
    </li>
</div>
```
## Tagy
Krome jejich strukturniho vyznamu (Markup) mohou mit doplnujici/upresnujici atributy.

```html
<div id="menu">
<a href="http://XXXXXXX.cz">
<div class="sloupec">
```

Vidime, ze format se hodne podoba slovnikum v Pythonu. Tedy __klic__= __"hodnota"__.

## Jak tedy ziskat potrebne udaje?
Abychom mohli s udaji, ktere jsou k dispozici na webu pracovat, je potreba ziskat a zpracovat konkretni HTML soubor.

## Stahujeme HTML pomoci Pythonu
Nejprve musime pomoci Pythonu vyslat __pozadavek__ na server, aby nam HTML konkretni format poskytl. Za timto ucelem budeme pracovat s modulem __requests__. Ve svem aktivovanem prostredi nainstalujeme balicek _requests_

Bud prikazem:
```bash
(env) matous@matous:~/projects/$ pip install requests
```
Nebo v editoru (viz. lekce)

Pote balicek nahrajeme do naseho pracovniho souboru:
```python
"""Lekce #15 - Uvod do programovani, web scraping"""

import requests
```

## Komunikace se serverem
1. __GET__ - vyzadame si udaje od serveru
2. __POST__ - posleme data, ktera server zpracuje a odpovi


### GET
Pouziti metody __.get()__ zavisi na jedinem povinnem parametru. Tim bude tedy _uniform resource locator_ (URL). Je mozne pouzit jeste dalsi parametry (nepovinne).

```python
URL = "http://heroes3.cz/hraci/"
import requests
odpoved_serveru = requests.get(url)
odpoved_serveru.status_code  # 200 -> viz. odkaz stavove kody
odpoved_serveru.encoding  # 'UTF-8'
odpoved_serveru.headers  # zobrazim zahlavi z odpovedi serveru
```

### POST




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
