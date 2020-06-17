![](../images/engeto.png)
# Python academy, lesson 12

# Important links
- [Python Academy, lekce 12](https://engeto.com/cs/kurz/online-python-akademie/studium/n9fgfnBHTk63vJN6caNang/formaty-souboru/csv)
- [Minula lekce, repo](https://github.com/Bralor/python_academy/tree/master/lesson11)
- [Textove soubory, repo](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)
- [JSON, obecne](https://www.json.org/json-en.html)
- [CSV, obecne](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Mockaroo, generator dat](https://www.mockaroo.com)

# Dnesni ukol
V dnesnim, uz 12. webinari si budeme povidat o dalsich typech [textovych souboru](#important-links), se kterymi muzeme v ramci Pythonu pracovat. Povime si neco o formatu, jehoz hlavnim ucelem je snadny prenos dat (tedy [JSON](#important-links)) a tabulkovem formatu (tedy [CSV](#important-links)).


# Prevodnik JSON -> CSV -> JSON
Ukolem pro dnesni webinar je napsat program, ktery bude umet prevadet JSON na CSV a obracene (definovano uzivatelem pri spousteni). Na uvod dostaneme JSON fiktivni udaje zamestnancu, ktere budeme chtit ukladat do CSV (pro nasledne potencialni pouziti v MOffice/LOffice). Logicky chceme usporadat strukturu programu nasledovne:
```
hlavni.py           # spousti cely kod
csv_funkce.py       # obsahuje funkce s csv
json_funkce.py      # obsahuje funkce s json
spolecne_funkce.py  # obsahuje funkce spolecne
```

# Nas cil
Vystupy pro ruzne scenare budou vypadat nasledovne (nebo podobne).

Spousteni:
```
python <hlavni_soubor.py> <CSV/JSON_udaje> <2json/2csv>
python hlavni.py zamestnanci.csv 2json
python hlavni.py zamestnanci.json 2csv
```

Uspech:
```
$ python hlavni.py zamestnanci.csv 2json
-rw-r--r-- 1 matous matous xxxx MMM DD HH:MM zamestnanci.json

$ python hlavni.py zamestnanci.json 2csv
-rw-r--r-- 1 matous matous xxxx MMM DD HH:MM zamestnanci.csv
```
Neuspech:
```
$ python hlavni.py zamestnanci.csv 2json
SOUBOR NELZE ZAPSAT JAKO .JSON
```

# Prerequisites
- python 3.6+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)

# Postup
Do pracovniho adresare si nakopirujeme vstupni JSON soubor, se kterym budeme chtit pracovat. Dale si otevreme novy soubor, ktery pojmenujeme __hlavni.py__ a dalsi soubory (__csv\_funkce.py__, __json\_funkce.py__, __spolecne\_funkce.py__).

Hlavni soubor:
```
#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - hlavni funkce"""

# I. KROK
# Hlavni ridici funkce se dvema scenari
```

JSON:
```
#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - json funkce"""
import json
```

CSV:
```
#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - csv funkce"""
import csv
```

SPOLECNE:
```
#!/usr/local/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - spolecne funkce"""
```

# Cheatsheet s priklady
## JSON
1. "lightweight" format urceny pro prenos dat (zkratka JavaScript Object Notation). Snadno citelny, lehce formatovatelny.
2. Kolece paru __nazev__ + __hodnota__
3. V Pythonu vypada jako slovnik
4. Muzeme zapisovat (*.dump()*) & nacitat (*.load()*)

## CSV
1. Comma-separated values ruzneho dialektu (delimiter, header, newline)
2. Bunky rozdelene oddelovacem (delimiter, volitelny), radky newliny
3. Muzeme zapisovat (pomoci *writer/DictWriter* objektu), cist (pomoci *reader/DictReader* objektu)
