![](../images/engeto.png)
# Python academy, lesson 11

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/2dUFX2MjRFu60Wb2LO59_g/importovani/uvod-do-kurzu)
- [Soubor \_\_init\_\_.py](https://pythontips.com/2013/07/28/what-is-__init__-py/)
- [Hledani modulu](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
- [Instalator balicku pip](https://pypi.org/project/pip/)
- [Pycharm importing](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
- [Name == '__main__'](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)


# Dnesni ukol
Cilem dnesni lekce je povedet si vic o modulech. Rozlisovat mezi moduly a baliky. Umet nacist nejenom moduly standartni ale i moduly tretich stran a s tim problematika souvisejici. Dale se budeme snazit rozdelit nasi praci do nekolika souboru. Po celou dobu jsme pracovali v prostredi jednoho souboru. Ale dnes se budeme snazit pouzit na praci i vice spolupracujicich souboru.

# Vytvareni souboru
Budeme v situaci, kdy dostaneme jako vstupni udaj textovy soubor. V tomto souboru jsou jmena a jejich pripony. Za pomoci tohoto souboru budeme chtit vytvorit skutecne soubory (staci prazdne) do uzivatelem zadaneho adresare.

# Nas cil
Vystupy pro ruzne scenare budou vypadat nasledovne (nebo podobne).

Spousteni:
```
$ python <jmeno_souboru> "<prazdna_slozka>" "<txt_s_jmeny>"  # obecne
$ python hlavni.py "/home/mholinka/projects/python_academy/lesson11/pokus" "/home/mholinka/projects/python_academy/lesson11/jmena_souboru.txt"
```

Uspech:
```
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/outlook_2016.pptx
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/icon_53456.jpg
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/summary_2019.pptx
...
```
Neuspech:
```
$ python hlavni.py "/home/mholinka/projects/python_academy/lesson11/pokus" "/home/mholinka/projects/python_academy/lesson11/jmena_souboru.txt"
ADRESAR JIZ EXISTUJE! (/home/mholinka/projects/python_academy/lesson11/pokus)
SOUBORY NELZE VYTVORIT! VRACENA HODNOTA --> False
```

# Prerequisites
- python 3.6+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)


# Postup
Do pracovniho adresare si nakopirujeme vstupni textovy soubor, se kterym budeme chtit pracovat. Dale si otevreme novy soubor, ktery pojmenujeme __hlavni.py__ a dalsi soubor __pomocne\_funkce.py__.

Hlavni soubor:
```
#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - hlavni funkce"""

# I. KROK
# Vytvorime hlavni funkci

# II. KROK
# Volame funkci *hlavni()*
# __name__ == "__main__"
```
Pomocne funkce:
```
#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - pomocne funkce"""

# ad. III. KROK
# Funkce zkontroluje jestli je cesta validni

# ad. III. KROK
# Funkce vytvori prazdny adresar

# ad IV. KROK
# Funkce najde soubor, otevre jej a precte jeho obsah

# ad V. KROK
# Funkce se pokus vytvorit jednotlive soubory
```

# Teorie s priklady
## Nazvoslovi
1. __Modul__ (module) - v jednoduchosti jde o [soubor](https://engeto.com/cs/kurz/online-python-akademie/studium/TV769pARQ8GJsa-X_ykhug/importovani/importujeme-moduly/co-je-to-modul) s priponou ".py". Obsahuje promenne, funkce, aj.

Priklad:
```
import <muj_modul>      # obecne
import os               # konkretni priklad
```

2. __Balik__ (package) - je cela sbirka modulu (tedy *.py* souboru) umistena ve spolecnem adresari, ktery ma navic jistou hierarchii. Uvnitr adresare najdeme soubor [__\_\_init\_\_.py__](#important-links) (oznacuji adresare na disku, ktere Python pouziva jako baliky). Dale obsahuji soubor __\_\_pycache\_\_.py__. To je soubor, ktery vznika kdyz spoustime koda interpret jej zkompiluje na __bytecode__ a schova je do toho adresare. Ucel je spustit program, co mozna nejrychleji (za predpokladu, ze jej neupravime).

Priklad:
```
from <package> import <modul>   # obecne
from collections import List    # konkr. priklad
```

## Ucel
- nemusim jej psat, ale aplikovat
- muzu jej opakovane pouzivat v ruznych souborech
- kod je prehlednejsi

## Importovani, obecne
Pokud chci modul [pouzit](https://engeto.com/cs/kurz/online-python-akademie/studium/XTUm-WCsSbW1AxOucXXwWA/importovani/importujeme-moduly/jednoduchy-import), musim jej nahrat (*importovat*):
1. Python kontroluje jestli neni modul jiz nacteny
2. Pokud neni, [hleda](#important-links) jej:
3. V built-in modulech
4. V aktualnim adresari
5. Pomoci sys.path
6. ModulNotFoundError -> soubor jsme nenasli vyse
7. Kompilace + spusteni -> soubor nalezen

Priklad:
```
import sys
sys.modules         # slovnik s zabudovanymi moduly
sys.path            # adresare, kde algorytmus hleda
```

## Moduly tretich stran
Pro praci s moduly tretich stran muzeme pracovat v __terminalu__ nebo primo v __editoru__:

### Terminal
1. Vytvorim si virtualni pracovni prostredi
```
python3.8 -m venv <jmeno_prostredi>     # obecne
python3.8 -m venv python_academy        # priklad
```

2. Aktivuji moje pracovni virtualni prostredi
```
source <jmeno_prostredi>/bin/activate       # obecne
source python_academy/bin/activate          # v nasem pripade
```

Priklad s ukoncenim:
```
(python_academy) matous@matous:~/$ deactivate   # ukoncim virt. prostredi
matous@matous:~/projects/python_academy$        # -> jmena prostredi nevidim
```

3. Najdu modul, ktery se mi hodi
4. Stahuji + instaluji (pomoci [pip](#important-links) -> package installer)
```
pip install requests-html       # instalace
pip uninstall requests-html     # odstraneni
```

5. Zkontroluji, ktere moduly mam pro svuj aktualni projekt dostupne a zapisu je do .txt souboru
```
pip freeze > requirements.txt
```

### Pycharm
- [Spustime](#important-links) Pycharm a otevreme projekt
- -> Settings
- -> Project: <jmeno_projektu>
- -> Project interpreter
- Vedle tabulky nahore + vpravo je symbol *+*
- Vyhledame modul/balik

## if __name__ == "__main__"
[Konstrukce](https://engeto.com/cs/kurz/online-python-akademie/studium/V1BsukdUSrS2lSP5T2-1wg/importovani/moduly-do-podrobna/co-je-to-__name__-), ktera nam umozni bezkonfliktne [importovat](#important-links) soubory i jejich obsah a pritom nedojde ke spusteni celeho souboru. Pri spusteni .py souboru ulozim do promenne __\_\_name\_\_.py__ hodnotu __\_\_main\_\_.py__.

Priklad:
```
def hlavni():
    print("Volani prvni funkce...")
    funkce_1()
    print("Volani druhe funkce...")
    funkce_2()
    print("Volani treti funkce...")
    funkce_3()


def funkce_1():
    print("Spousteni prvni funkce...")


def funkce_2():
    print("Spousteni druhe funkce...")


def funkce_3():
    print("Spousteni treti funkce...")
```

Pokud soubor importuji (.py!) nastavi hodnotu __\_\_name\_\_.py__ jako jmeno souboru.

Reseni:
```
if __name__ == "__main__":
    print("Spousteni pres importovani")
    hlavni()
else:
    print("Naimportovano!")
```

