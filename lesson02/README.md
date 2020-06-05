# Python academy, lekce 02
# Important links

- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/lekce)
- [Ukoncovani v Pythonu](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)

# Destinatio, pt. 2
Budeme pokracovat v nasem projektu pro zjednodusene rezerovani jizdenek.

## Nas cil
Za predpokladu, ze nami zadane hodnoty budou mit platny format, by vystup na zaver mohl vypadat nasledovne:
```
===================================
Vitejte u nasi aplikace Destinatio!
===================================

1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180

===================================
Vyberte cislo lokality: 3
DESTINACE: Olomouc
===================================
JMENO: Matous
PRIJMENI: Holinka
JMENO: Matous, PRIJMENI: Holinka
===================================
ROK NAROZENI: 1992
Pokracuji...
===================================
EMAIL: matous@matous.cz
Email v poradku, pokracuji...
===================================
HESLO: panpes738
Heslo v poradku
===================================
UZIVATEL: Matous
DESTINACE: Olomouc
CENA(cil:Olomouc): 90.0
Jizdenku posleme na Vasi emailovou adresu: matous@matous.cz
```

# Prerequisites
- Python 3.6 +
- IDE
- vystup z prvni [lekce](https://github.com/Bralor/python_academy/blob/master/lesson01/destinatio1.py)

# Postup
Otevreme nas pracovni adresar se souborem z minule lekce. Udelame si kopii a pojmenujeme ji "destinatio2.py". Nasledujici postup si vlozime tam, kde jsme minule skoncili.

```
#!/usr/bin/env python3
""" Lekce #2 - Uvod do programovani, 2/2 Destinatio """

# ~~~~~~~~~~~~~~~~~~~ZAPIS Z LEKCE #01~~~~~~~~~~~~~~~~~~~
...
# ~~~~~~~~~~~~~~~~~~~KONEC ZAPISU Z LEKCE #01~~~~~~~~~~~~~~~~~~~
# I. KROK:
# Doplnit zadani

# II. KROK:
# Spravne cislo lokality! Podm. zapis x --> (1, 6)

# III. KROK:
# Vyresime pouziti slevy. Membership testing.

# IV. KROK:
# Jmeno + prijmeni obsahuje jen pismena

# V. KROK:
# Aktualni rok - datum narozeni >= 18

# VI. KROK:
# Spravny email obsahuje "@"

# VII. KROK:
# Heslo obsahuje jak cisla, tak pismena + delka >= 8
# Zaverecny vystup pro uzivatele
```

# Teoreticky cheatsheet s priklady
## Boolean hodnoty
Je to dalsi datovy typ. Spada castecne pod integer (tedy specialne hodnoty 1 a 0). V Pythonu je ale casteji oznacujeme textovym popiskem True(1) a False(0). Jejich ucelem je rozhodovat v testovaci procedure, zda-li je nejaky vyraz [pravdivy](https://engeto.com/cs/kurz/online-python-akademie/studium/9roGO2_ITGaLbq-X-KGT7w/rozhodujeme/datovy-typ-boolean/co-je-to-boolean) nebo ne.

## Logicke operatory
Bool hodnoty souvisi s pouzitim logickych operatoru:
-[and](https://engeto.com/cs/kurz/online-python-akademie/studium/rh38CL2fRmmOBqJt312GOA/rozhodujeme/datovy-typ-boolean/logicke-operace)
-or
-not

## Podminkovy zapis
Pro pouziti [podminkoveho zapisu](https://engeto.com/cs/kurz/online-python-akademie/studium/EBuXiFdpSKK96n6Eds4cgA/rozhodujeme/python-rozhoduje/podminky-if) musime dodrzet nasledujici kroky:
1. Klicove slovo _if_
2. Vytvorit bool() test
3. Radek ukoncit dvojteckou
4. Nasledujici radek psat odsazeny

Priklad I.:
```
A = 10_000
B = 15_000

if A > B:
    print("PRAVDA! A je mensi nez B")  # True
else:
    print("NENI PRAVDA! A neni vetsi nez B")  # False
```

Priklad II.:
```
METRO = False               # bool
POCET_OBYVATEL = 374_734    # integer

if POCET_OBYVATEL < 100_000:
    print("Jde o male mesto")

elif POCET_OBYVATEL < 300_000:
    print("Jde o velke mesto")

elif POCET_OBYVATEL == 374_734 and METRO == False:
    print("Jasne BRNO!")

```

## Ukoncovaci oznameni
Jde o formu ukonceni prubehu naseho souboru. V Pythonu je vic moznosti jak ukonceni vyvolat (quit()/exit()). Vice info v odkazu na uvod.

Priklad:
```
VEK = 19

if VEK > 18:
    print("USPECH! Pokracuji...")
else:
    print("NEUSPECH! Ukoncuji...")
    exit()
```
## Overovani clenstvi
Jde o dotazovaci strukturu, kdy se ptame jestli je nejaky udaj [soucasti](https://engeto.com/cs/kurz/online-python-akademie/studium/tR_PX2qoQw68kXQKe1q1fg/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/pritomnost-prvku-membership-test) sekvence jako je string, list, tuple. Klicovym pojmem v tomto overovani je _in_.

Priklad:
```
>>> "Matous" in ["Matous", "Marek", "Lukas", "Jan"]
True
```

## Nektere metody retezcu
Jde o metody, ktere nam pomahaji/usnadnuji praci s retezci.
1. S.isalpha() --> vraci True, pokud jsou vsechny znaky v S pismena
2. S.isnumeric() --> vraci False, pokud jsou vsechny znaky ciselne

Priklad:
```
>>> "Matous".isalpha()
True
>>> "M@tous".isalpha()
False
>>> "Mat0us".isalpha()
False
>>> "7350".isalpha()
False
>>> "7350".isnumeric()
True

```

## len()
Jde o preddefinovanou funkci, ktera slouzi k [pocitani prvku](https://engeto.com/cs/kurz/online-python-akademie/studium/MCDGtwdxTn2GMv5sfPvXQA/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/zjisteni-delky-lenght) v udaji.

Priklad:
```
>>> len("Matous")
6
>>> len(["zena", "ruze", "pisen", "kost"])
4
```
