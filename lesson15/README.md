<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 15

# Dulezite odkazy
- [Python Academy, lekce 15](https://engeto.com/cs/kurz/online-python-akademie/studium/SYzMVJcBQSiagUXKNLvXfA/intro-do-scrapingu/slovo-na-uvod/co-te-ceka-v-teto-lekci)
- [Minula lekce, repozitar](https://github.com/Bralor/python_academy/tree/master/lesson14)
- [heroes III - cesko-slovenska liga](http://heroes3.cz/)

# Co nas ceka?
V ramci dnesniho webinare se budeme snazit _scrapovat_, tzn. ze za pomoci Pythonu se budeme snazit shromazdovat nejake informace umistene ve formatu HTML nekde na webu. Povime si o tom, jak s temito udaji zachazet, jak je vyhledavat a jak je rozlisovat. Soubezne s obecnym vykladem teorie se budeme snazit vyresit dnesni ukol.

# Screjpuj tabulku hracu
Cilem bude extrahovat data z webu a ulozit je lokalne do nejakeho textoveho souboru (optimalni CSV).

# Prerequisites
- python 3.6+
- text. editor
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)
- [Csv](https://github.com/Bralor/python_academy/tree/master/lesson12)

# Teoreticke materialy & ukol
## Co bychom radi ukladali?
Vyhledam zamysleny web. Najdu co me zajima. Sledujme [odkaz](http://heroes3.cz/)


## V cem jsou nase udaje?
Data jsme nasly. Ted jak je cist? Pravym tlacitkem mysi si rozbalime nabidku a v ni najdeme __view page source__(Mozilla). Nyni koukame na zdrojovy kod. Vidime, ze jde o format typu HTML.

```html
<!DOCTYPE html>
<html lang ="cs">
<head>
...
</head>
```

## HyperText Markup Language
Tvori strukturu webovych stranek. Je to hierarchicky usporadana struktura tvorena pomoci tagu. Z nasledujiciho vzoru muzeme rict, ktere tagy jsou rodicovske, a ktere jejich potomci. My tuto strukturu na pozadi casto nevnimame. Prohlizec nam casteji zprostredkuje vyrenderovanou grafickou podobu.

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
Abychom mohli s udaji, ktere jsou k dispozici na webu, pracovat, je potreba stahnout konkretni _HTML_ soubor.

## Stahujeme HTML pomoci Pythonu
Nejprve musime pomoci Pythonu vyslat __pozadavek__ na server, aby nam _HTML_ konkretni format poskytl. Za timto ucelem budeme pracovat s modulem __requests__. Ve svem aktivovanem prostredi nainstalujeme balicek _requests_

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
Pouziti metody __.get()__ zavisi na jedinem povinnem parametru. Tim bude _uniform resource locator_ (URL). Je mozne pouzit jeste dalsi parametry (nepovinne).

```python
URL = "http://heroes3.cz/hraci/"
import requests
odpoved_serveru = requests.get(url)
odpoved_serveru.status_code  # 200 -> viz. odkaz stavove kody
odpoved_serveru.encoding  # 'UTF-8'
odpoved_serveru.headers  # zobrazim zahlavi z odpovedi serveru
```

### POST
Metoda __.post()__ je velice podobna metode __.get()__. Mrkneme se spolecne do naseho virtualniho prostredi, kde tuto metodu nalezneme. Potrebujeme zase zapsat kam (url), chceme nami vyplnene udaje odeslat. Dale potrebujeme __parametry__. Tyto parametry maji specifikovat serveru, o jaky konkretni udaj mame zajem.

Nahrajeme modul:
```python
import requests
```

Zadane konkretni adresu:
```python
url = "XXX"
```
Ukazeme si, kde najit parametry:
```python
params = {
    'kraj': -1,
    'okres': -1,
    'razeni': 1, 'archiv': 0,
    'typ_polozky': -1,
    'page': 1
}
```

Odesleme pozadavek pomoci metody _post_ na server, ktery jej vyhodnoti a zpracuje:
```python
odpoved_serveru = requests.post(url, params=params)
odpoved_serveru.status_code
odpoved_serveru.text
```

## Mame zdroj!
Jakmile se nam konecne podari udaje nashromazdit. Musime se nimi probrat.

```python
odpoved_serveru = requests.get(URL)
odpoved_serveru.text  # metoda text nam umozni prohlednout obsah
```

## Aplikujeme v nasi uloze
```python
"""Lekce #15 - Uvod do programovani, web scraping"""

import csv
from typing import List

import requests
from bs4 import BeautifulSoup

URL = "http://heroes3.cz/hraci"


def hlavni() -> None:
    pass

if __name__ == "__main__":
    hlavni()
```
Pomocna funkce:
```python
def ziskej_odpoved():
    return requests.get(URL)
```

## Jak jej prochazet?
Zkusime z naseho zdroje neco dohledat:
```python
odpoved_serveru.text[0]  # ...
odpoved_serveru.text[1]  # ...
odpoved_serveru.text.split()  # ...
```
Nami zname zpusoby, kterymi muzeme text [parsovat](https://en.wikipedia.org/wiki/Parsing)(prochazet) tady nejsou moc platne. Budeme potrebovat silnejsi kalibr.

## Beautiful Soup
Nainstalujeme si do naseho prostredi dalsi [balicek](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

```bash
(env) matous@matous:~/projects/$ pip install beautifulsoup4
```

Modul BeautifulSoup se postara, abychom vytahli ze ziskaneho HTML (dale podporuje i XMLka) strom, skrze ktery je mozne snadno navigovat a vyhledavat.

Nacteme z balicku modul:
```python
from bs4 import BeautifulSoup
```

Pouziti obsahuje aplikaci dvou parametru. Prvnim je objekt, kde se syrove HTML nachazi, druhy je typ parseru:
```python
naparsovane = BeautifulSoup(odpoved_serveru.text, "html.parser")
```

## Aplikujeme v uloze
Doplnime dalsi pomocnou funkci a dopiseme hlavni():
```python
def vytahni_udaje(resp):
    return BeautifulSoup(resp.text, "html.parser")
```
## Musime najit konkretni tag!
Musime se zorientovat v nasem HTML-ku a uvedomit si, ve kterem elementu hledat. V prohlizeci, pomoci rezimu _inspect_ zjistime, o ktery jde.

```html
    <table class="tab_top">
        <tr></tr>
    </table>
```

## Mame vybrano, jak hledat?
Vyhledavat budeme zejmena pomoci typu elementu (_div_,_table_,..) v kombinaci s metodou __.find()__.  Pomocne pro nas mohou byt zejmena attributy (_"tab\_top"_). 

```python
...
naparsovane.find("table", {"class": "tab_top"})
...
```
## Opet aplikujeme
```python
def hledej_tabulku(cont):
    return cont.find("table", {"class": "tab_top"})
```

Timto nase puvodni HTML orezeme a dostaneme pouze obsah <table></table>

## Jak ziskat info o hraci?
Vidime, ze na kazdem radku mame jednoho hrace. Takze se musime probrat k jednotlivym radkum. Takze musime prochazet promennou, kam jsme ulozili tabulku a znovu projit. Muzeme si vsimnout, ze radku je tu hodne a proto nam klasicke __.find()__ nepomuze. To, totiz vrati pouze prvni nalezenou hodnotu.

```python
radky = tabulka.find("tr")  # nelze pouzit, pokud je vice radku
```

Pouzijeme __.find\_all()__, ktera nam vrati vsechny elementy v zadanem objektu.

```python
radky = tabulka.find_all("tr")
radky[0]; radky[1]  # muzeme vytahovat pomoci indexu
```
## Aplikujeme...
Opatrne na zahlavi v _HTML_. To muze komplikovat situaci:
```python
def hledej_radky(tabl) -> list:
    return tabl.find_all("tr")[1:]
```

## Ziskejme konkretni bunku!
Podobne jako u radku v tabulce musime premyslet o bunce v radku. Opet je pro ni typicky konkretni element a na nej se musim zamerit.

```python
hrac_1 = radky.find_all("td")[1]
```

Nami vyfiltrovane HTML nyni obsahuje udaje, patrici prvnimu hraci tabulky. Jak se ale dostaneme ke konkretnimu textovemu udaji?

## Jake bunky tabulky?
V tabulce je porad spousta udaju. Potrebujeme nas vyber jeste malicko zuzit. Rekneme, ze mame zajem pouze o poradi, nickname, body a uspesnost.

## Vrat hodnotu elementu
Pomuze nam metoda __.text__, ktera vraci pouze hodnotu elementu.

```python
hrac_1 = radky.find_all("td")[0]  # poradi
hrac_1 = radky.find_all("td")[2]  # nickname
hrac_1 = radky.find_all("td")[3]  # body
hrac_1 = radky.find_all("td")[7]  # uspesnost
```

## Doplnime...
Doplnujici funkce. Opet musime doplnit i funkci hlavni:
```python
def hraci_info(tr) -> dict:
    try:
        poradi = tr.find_all("td")[0].text
        ...

    except AttributeError:
        print("Indexy u jednotlivych bunek v radku nejsou v poradku")
```
## Ukladani do souboru
Vytvorime si doplnujici funkce. S pomoci modulu __csv__:
```python
def uloz_csv(data: List[dict]):
    with open("players.csv", "a", newline="") as csv_f:
        zahlavi = ["PORADI", "UZIVATEL", "BODY", "USPESNOST"]
        writer = csv.DictWriter(csv_f, fieldnames=zahlavi)
        writer.writeheader()

        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "PORADI": data[index]["poradi"],
                    "UZIVATEL": data[index]["hrac"],
                    "BODY": data[index]["body"],
                    "USPESNOST": data[index]["uspesnost"],
                }
            )
```

## Generator nebo seznam?
Na zacatku, ve funkce _hlavni()_ se nabizi otazka. Je lepsi pouzit seznamovou komprehenci nebo generator?
```python
konecne_udaje = (hraci_info(row) for row in radky)  # generator
konecne_udaje = [hraci_info(row) for row in radky]  # seznam
```
## Dulezite na zaver!
1. Nez se doopravdy pustite do scrapovani udaju, prectete si sekci _pravidla&podminky_, abyste vedeli jak legalne data pouzivat. Ve vetsine pripadu je zakazano pouzivat udaje pro komercni ucely.
2. Ujistete se, ze udaje nestahujete ve velkem meritku(dlouho a velke mnozstvi). To muze mit za nasledek pad serveru a prinejmensim Vase zablokovani.

