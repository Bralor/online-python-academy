<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 16
## Dulezite odkazy
- [Python Academy, lekce 16](https://engeto.com/cs/kurz/zaklady-api-s-pythonem/lekce)
- [Minula lekce, repozitar](https://github.com/Bralor/python_academy/tree/master/lesson15)
- [Oficialni podpora](https://developers.google.com/sheets/api/quickstart/python)
- [Jiny postup](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

## Co nas ceka?
V nasem poslednim, 16em webinari se budeme bavit o _API_ (application programming interface). Rekneme si opet o co jde, kde se s nim muzeme setkat a ukazeme si i praktickou ulohu, kde vsechno aplikujeme.

## Kindle clippings - poznamky
Ukol, ktery nas ceka dnes je prevest udaje ulozene v poznamkach ctecky. Cilem bude tyto udaje posbirat, roztridit a ulozit na Google drive prave pomoci API.

## Prerequisites
- python 3.6+
- text. editor
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)
- [filter()](https://github.com/Bralor/python_academy/tree/master/lesson13#funkce-filter)
- [generatory](https://github.com/Bralor/python_academy/tree/master/lesson14#generatorova-funkce)

# Teoreticke materialy & ukol
## Nejprve musime soubor najit
Pomoci prohlizece souboru nejprve nas soubor s poznamkami najdeme. Nasledovne jej presuneme do pracovniho naseho dnesniho adresare.

## Nase prvni funkce
Nase prvni funkce se pokusi otevrit preddefinovany soubor.
```python
"""Lekce #16 - Uvod do programovani, API intro"""

import sys
from typing import List

def hlavni(soubor) -> None:
    pass

def ziskej_poznamky(soubor) -> List[str]:
    pass
```

## Prohledneme data
Jakmile je soubor nacteny, musime zkontrolovat jak vypada. Z ceho je slozeny a jak se v nem orientovat.

```bash
$ python <nas_soubor.py> <poznamky.txt>
Gray---Muži-jsou-z-Marsu,-ženy-z-Venuše (Unknown)
- Your Bookmark on page 3 | location 32 | Added on Tuesday, 24 April 2018 10:13:28

==========
...
```

## Jak je usporadat?
V nasem vystupu je videt jednotlive poznamky. Ale jak je rozdelit? Bude potreba smycky, ktera nam cely seznam rozseka podle definovaneho oddelovace.

```python
def parsuj_poznamky(pozn: List[str]) -> List[str]:
    ...
```
Takze po dopsani a spusteni teto casti dostaneme:
```bash
$ python <nas_soubor.py> <poznamky.txt>
['\ufeffGray---Muži-jsou-z-Marsu,-ženy-z-Venuše (Unknown)\n- Your Bookmark on page 3 | location 32 | Added on Tuesday, 24 April 2018 10:13:28', ....
```

## Jak dal?
V tento moment jsme si cely soubor se vsemi poznamkami rozdelili na jednotlive poznamky. Pomoci indexu jsme schopni je oznacovat a vracet. Vsimneme si, ze kazda jednotliva poznamka ma vlastni typickou strukturu. Zkusme ji opet specifikovat.

```python
def rozdel_poznamku(note: str) -> str:
    ...
```

Pokud na rozdelenou poznamku koukneme, muzeme rict, ze je slozena ze tri casti:
```bash
$ python <nas_soubor.py> <poznamky.txt>
[
    'Kindle Paperwhite User’s Guide, 8th Edition (Amazon)',  # Kniha
    '- Your Highlight at location 44-46 | Added on Wednesday, 30 May 2018 16:45:15',  # Popis
    'Device. If you have enabled ...'  # Samotna poznamka
]
```

## Parsujeme vsechny poznamky
Jakmile uvidime onen vzorec rozdeleni pro jednotlive poznamky, muzeme jej zkusit aplikovat i u ostatnich. Pojdme napsat generator, ktery se o to postara.

```python
def generator_poznamek(poznamky: str) -> Generator[tuple, None, None]:  # Generator[yield_type, send_type, return_type]
    for <var> in poznamky:
        try:
            ...

        except ValueError as ve:
            print(f"{ve.__class__.__name__}: Nema 3 casti! > {zpr_poznamka}")
```

## Proc generator a ne cyklus?
Otazka do pranice...

## Prvni cast -> hotovo!
Prvni cast naseho programu je hotova a dela nasledujici: 
1. Nacte textovy soubor,
2. Zpracuje jej,
3. Vystupem bude podany tuple. 

Podle vzoru nize:
```python
# 1. cyklus
("kniha1", "popis1", "poznamka1")
# 2. cyklus
("kniha1", "popis2", "poznamka2")
# 3. cyklus
("kniha1", "popis3", "poznamka3")
...
```

## Odesilani udaju?
Nyni si budeme muset neco povedet o API, abychom mohli ulohu dotahnout na konce.

## API
Jde o nejake [rozhrani](https://www.mulesoft.com/resources/api/what-is-an-api), ktere umoznuje dvema aplikacim (kazda na jednom konci) spolecne komunikovat.

### Priklad API
Analogii pro tuto situaci muze byt Vase navsteva v restauraci. Na jednom konci vy, jako klient, na druhem konci kuchyne, jako nejaka cast systemu. Ta bude mit na starost vyridit Vasi objednavku. Ted uz chybi jenom kriticke spojeni mezi Vami a kuchyni. Tim bude cisnik/cisnice, ktera objednavku interpretuje v kuchyni a za moment dorazi s jidlem. V nasem prikladu je tedy cisnik, prip. cisnice pomyslnym API.

## Nas cil
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/Logo_of_Google_Drive.svg" width="200" height="200">
  <img src="https://lh3.googleusercontent.com/RYEyviCFtwVsRHolYDHbnuDf6s9FEttJmPT-6W0ZY0xYwcmEQsG5glDV-h2afrNIFnB_" width="200" height="200">
</p>

Nas cil je jasny, nahrat nami ziskane udaje na Google Drive ve forme Drive tabulky. Pojdme proto nastavit nase API rozhrani na jejich web.

## Nastaveni googlu
Nazhavte svoje prohlizece a prejdete na [tento odkaz](https://console.cloud.google.com). V uvodnim navigacnim poli hledame __Vyber projektu__ a vytvorime __novy projekt__ (pojmenujte jej treba _api uvod_). Nakonec potvrdime tlacitkem __CREATE__.

## Navigujeme pomoci noveho projektu
1. Klikneme na nas nove vytvoreny projekt a budeme presmerovani na __dashboard__.
2. V hlavnim menu se prepneme do sekce __API&Services__
3. Potom do sekce __Library__
4. Najdeme API __Google drive__ -> klikneme na __ENABLE__ a povolime jej uvnitr naseho projektu
5. Musime nastavit prihlasovaci udaje k nasemu API -> klikneme na __CREATE CREDENTIALS__
Vyplnime nasledujici pole:
```
Which API are you using? -> Google Drive API
Where will you be calling the API from? -> Web server
What data will you be accessing? -> Application data
Are you planning to use this API with App engine...? -> No,...
# Klikneme na "What credentials do I need? #
```
Dalsi tabulka:
```
Create a service account -> matous
Role -> editor
Key type -> JSON
# Klikneme na "Continue" #
```
6. Stahneme prihlasovaci udaje v souboru __JSON__
7. Prejdeme zpet do knihovny a povolime dalsi API -> Google sheet API -> klikneme na __ENABLE__
8. V tuto chvili mame povolene obe API a nachystane prihlasovaci/poverovaci udaje v souboru
9. Skocime na google Drive a vytvorime si novy prazdny Google sheet soubor.
10. Hotovo & smitec!

## ...opet lokalne
Udaje, ktere jsme stahly si prejmenujeme na __credentials.json__ a presuneme je do naseho pracovniho adresare. Tento soubor otevreme a zkopirujeme hodnotu klice __"client_email"__. Prepneme do naseho Google Drive -> do naseho souboru. Chceme sdilet novou tabulku excelu s hodnotou klice __"client_email"__. 

```python
  "private_key": "XXXXXX"
  "client_email": "matous@notesXXXXXX.iam.gserviceaccount.com",  # tuto hodnotu
  "client_id": "XXXXX",
```
Tim si udelime pristup z naseho API.

## Vytvorime novy soubor
Dalsim krokem bude vytvoreni .py souboru __sheet\_writter.py__. Ten bude mit za ukol vlastni zapisovani udaju.

## Nainstalujeme potrebne knihovny
Aktivujeme nase virtualni prostredi a nainstalujeme nasledujici dva baliky:
1. gspread - zarizuje interakce s Pythonem a Googlovskymi spreadsheety
2. oauth2client - udeluje autorizaci pro Google Drive API
```bash
pip install gspread oauth2client
```
## Zaciname psat
Po instalaci muzeme knihovny nahrat. U _oauth2client_ neni nutne importovat celou knihovnu, staci jeden modul:
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
```
Dale musime vlozit potrebna prostredi:
```python
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
```

Jakmile mame vsechna potrebna prostredi, nacteme nas prihlasovaci soubor:
```python
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name("creds.json", SCOPE)
CLIENT = gspread.authorize(CREDENTIALS)
```

Mame nactene potrebne prihlasovaci udaje. Dale dojde k autorizaci pro prostredi definovana vyse a pro samotny projekt.

Nakonec inicializujeme samotne otevreni naseho vzdaleneho souboru na Drive a otevrene prvni list:
```python
CLIENT.open("<jmeno_souboru_na_Drive>").sheet1
```

## Vytvorime radne funkce
Jednu hlavni, kterou budeme chtit nahrat do prvniho souboru a vedlejsi, ktera otevre prislusny Drive sheet.

```python
def zapisovac(index: int, data: tuple) -> None:
    pass

def otevri_drive_sheet():
    pass
```

## Vkladani udaju
Pro vkladani udaju je potreba pouzit prislusnou metodu __.insert\_row()__. Pouziti ve funkci:
```python
def vloz_data_na_radek(gsheet, data, row):
    return gsheet.insert_row(data, row)
```
Pouziti je obdobne jako metoda pro seznamy __.append()__

## Doplnim zahlavi tabulky
Momentalne ukladame na Drive samotna data ale chybi nam radne zahlavi. Pomoci built-in __enumerate()__:
```python
for index, poznamka in enumerate(<generator>, <start_index>):
        if index == 1:
            zahlavi = ("Kniha", "Popis", "Poznamka")
            sheet_writter.zapisovac(1, zahlavi)
        else:
            sheet_writter.zapisovac(index, poznamka)
```

# Slovo utechy zaverem
Takze nase Google API komunikuje skvele! Ulohu je mozne radikalne zdokonalit a automatizovat. Ale konkretni reseni by zabralo samozrejme vice casu. Pomoci API muzete sepsat kod mnohem uzitecnejsi, vsestrannejsi. Navic spousta spolecnosti se jejich API-ckem primo chlubi (Google, Spotify, youtube, aj.). Casto najdete velmi podrobne dokumentace a s kazdym je potreba se nejprve seznamit.
