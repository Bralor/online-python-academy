![](../images/engeto.png)
# Python academy, lesson 11

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/2dUFX2MjRFu60Wb2LO59_g/importovani/uvod-do-kurzu)

# Dnesni ukol
Cilem dnesni lekce je naucit se pracovat pomoci importovani modulu. Po celou dobu jsme pracovali v prostredi jednoho souboru. Ale dnes se budeme snazit pouzit na praci i vice spolupracujicich souboru. Dale si ukazeme dalsi uzitecne moduly (os, sys), pripadne jak si vytvorit vlastni.

# Vytvareni souboru
Budeme v situaci, kdy dostaneme jako vstupni udaj textovy soubor. V tomto souboru jsou jmena a jejich pripony. Za pomoci tohoto souboru budeme chtit vytvorit skutecne soubory (staci prazdne) do uzivatelem zadaneho adresare.

# Nas cil
Vystupy pro ruzne scenare budou vypadat nasledovne (nebo podobne).

Uspech:
```
...
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/outlook_2016.pptx
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/icon_53456.jpg
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/summary_2019.pptx

...
```
Neuspech:
```
$ python3.8 hlavni.py "/home/mholinka/projects/python_academy/lesson11/pokus" "/home/mholinka/projects/python_academy/lesson11/filenames.txt"
ADRESAR JIZ EXISTUJE! (/home/mholinka/projects/python_academy/lesson11/pokus)
SOUBORY NELZE VYTVORIT! VRACENA HODNOTA --> False
```

# Prerequisites
- python 3.6+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)


# Postup
Do pracovniho adresare si nakopirujeme vstupni textovy soubor, se kterym budeme chtit pracovat. Dale si otevreme novy soubor, ktery pojmenujeme *hlavni.py* a dalsi soubor *pomocne_funkce.py*.

Hlavni soubor:
```
#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - hlavni funkce"""
```
Pomocne funkce:
```
#!/usr/local/bin/python3.8
"""Lekce #11 - Uvod do programovani, importovani - pomocne funkce"""
```

# Cheetsheat s priklady
## Modul
## Importovani, jeste jednou
## Modul os
## Modul sys
## if __name__ == "__main__"
