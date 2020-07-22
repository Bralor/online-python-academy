Minula [lekce#04](https://github.com/Bralor/online-python-academy/tree/master/lesson04)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

![](../images/engeto.png)
# Online Python academy, lesson 05
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- Funkce [Sorted()](https://docs.python.org/3/library/functions.html#sorted)
- Seznamova [komprehence](http://howto.py.cz/cap08.htm#10)

## Co nas dneska ceka
V ramci dnesni lekce budeme chtit dokoncit teorii o smyckach v Pythonu.  V 
predchozi lekci jsme si povidali o __while__ cyklu. Dnes budeme mluvit o 
_for cyklech_. Rekneme si obecne o jejich pouziti, doplnujici zpusob prace
s nimi. Na zaver bychom si povedeli neco o rozdilu mezi temito dvema typy. 

## Hledani nejcastejsich slov
Soucasne s dnesni tematikou si zadame opet spolecnou ulohu. V poznamkach nize
si zkopirujeme nahodny text nekam do sveho lokalniho pracovniho souboru.
Cilem bude zjistit pet nejcastejsich slov, ktere se v textu vyskytuji.

## Ukazka na uvod
Spustime skript v tomto adresari:
```
$ ./nejcastejsi_slova
```
Vystup by na konci lekce mohl vypadat nasledovne:
```
    VITEJTE U NASEHO POCITADLA!    
===================================
1. NEJCASTEJSI SLOVO: in, VYSKYT: 5
===================================
2. NEJCASTEJSI SLOVO: up, VYSKYT: 4
===================================
3. NEJCASTEJSI SLOVO: of, VYSKYT: 3
===================================
4. NEJCASTEJSI SLOVO: ye, VYSKYT: 3
===================================
5. NEJCASTEJSI SLOVO: an, VYSKYT: 3
===================================
```

## Co budeme potrebovat?
- python 3.6+
- text. editor
- pomocny text:
```python
TEXT = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual. 
"""
```

## Jdeme na to!

<p align="center">
  <img src="https://media.giphy.com/media/nbMyAHO0PAVxJ5uJmG/source.gif"  width="300" height="300">
</p>

Preskocime na okamzik do naseho noveho souboru. Vlozime
[pomocny text](#co-budeme-potrebovat) a zkusime napsat prvni cyklus.

Nejprve nase zadani. To bude vypadat nasledovne:
```python
""" Lekce #5 - Uvod do programovani, nejcastejsi slova"""

# I. KROK
# Zadani nasi ulohy
TEXT = ...
```
Tak a ted je ta chvile, kdy si vysvetlime __for__ cyklus a jeho syntaxi.
Jde o dalsi zpusob, kterym v Pythonu muzu opakovat casti kodu. Zatim co
__while__ se opakoval, pokud byla explicitne zadana podminka vyhodnocena jako
__True__, __for__ cyklus bezi, dokud neprojde celou zadanou sadu udaju.
Pripadne, pokud jej jinak neukoncime.

__Teorie__:
```python
for libovolny_jmeno in sada_udaju:
    <telo_smycky>
```

__Priklad__:
```python
JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]

for jmeno in JMENA:
    print(jmeno)  # Helmut, Helga, Harold, Hammet, Hetfield
```
Jakmile dojde k poslednimu udaji v nasem zadanem seznamu __JMENA__, uz nema
do smycky co podavat. Takze proste ukonci celou proces opakovani a pokracuje
kodem pod odsazenym telem smycky.

### Doplnime I. cast
```python
for slovo in TEXT:
    print(slovo)
```
Pojdme se podivat na vystup!

## Takze mame cyklus
A nyni prochazime nas text slovo za slov... a nebo taky ne!
__Opatrne na vstupni udaj cyklu__ Bohuzel nam smycka nevraci jedno slovo za
druhym, jak jsme puvodne cekali. Duvod je prosty. Zadany udaj totiz neni
seznam, jak byl v nasem vzoru ale retezec. S tim si ale umime poradit!

Metoda __split()__:
Tato metoda vraci seznam ze zadane promenne. Tuto zadanou promennou rozdeli
podle preddefinovaneho oddelovace.

__Priklad__:
```python
VETA1 = "Dneska mame ale otresne pocasi. Jeste, ze muzeme kodit v Pythonu!"
print(VETA1.split())     # rozdelime po slovech i radcich
print(VETA1.split("."))  # rozdelime po vetach
print(VETA1.split(".", maxsplit=1))  # rozdelime po vetach, 1x
```

Doplnime cast naseho kodu:
```python
# I. KROK
jednotliva_slova = TEXT.split()  # opatrne na symbol rozdelovani

for slovo in jednotliva_slova:
    ...
```
## Slova mame! Mame?!
Dale bychom se chteli zbavit carek a tecek! Pro odstraneni libovolnych vyrazu
se musime seznamit s dalsi metodou rezecu _strip()_.

Metoda __strip()__:
Tato metoda vraci kopii zadaneho retezce (promenne), kdy z puvodniho udaje
odstrani explicitne definovane symboly na zacatku/konci promenne.

__Priklad__:
```python
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov,\
        která však postrádají myšlenku a znalost.   "
VETA3 = "Není trapnější hloupost,..."
print(VETA2.strip())        # odstranime uvodni a zaverecne mezery
print(VETA3.strip(".,"))    # odstranime uvodni a zaverecne carky/tecky
```

### Dopsana II. cast
```python
vycistena_slova = []

for slovo in jednotliva_slova:
    ciste_slovo = slovo.strip(".,")
    vycistena_slova.append(ciste_slovo)
```

## Pocitame vyskyt
Jakmile muzeme prochazet slova vycistena od carek, tecek atd., prichazi moment,
kdy je zacneme pocitat. Nejprve musime vymyslet jaky datovy typ se nam pro
evidenci slov a jejich vyskytu vubec hodi.
```python
vyskyt_slov = {}
```

## Jak zapisu vyskyt?
Pokud pouzijeme k danemu ucelu slovnik, muzeme si vypomoct jednou z jeho metod.
Pomoci _setdefault()_ muzu kazdy vyraz, ktery potkam zapsat do naseho slovniku
__vyskyt_slov__.

__Ukazka__:
```python
muj_slovnik = {}

muj_slovnik.setdefault("Matous", 1)
muj_slovnik.setdefault("Marek", 2)
```
Jak zmenim hodnotu, pri pristim vyskytu konkretniho klice? Jednoduse upravime
zapis hodnot klicu.
```python
...
muj_slovnik.setdefault("Matous", 0) + 1
```
Tim zajistim, ze pocatecni hodnota klice bude nula a hned v tom samem kroku,
prictu hodnotu + 1. Takze po prvnim vyskytu dostanu hodnotu 1. Cyklus ale 
bezi dal, takze pokazde, kdyz se objevi stejny klic, prictu k hodnote +1.

### Dopsana III. cast
```python
...
for ciste_slovo in vycistena_slova:
    vyskyt_slov[ciste_slovo] = vyskyt_slov.setdefault(ciste_slovo, 0) + 1
    ...
```

## Jak vypiseme nejvetsi klice?
Ted uz mame vsechny udaje ohodnocene a potrebujeme je patricne vypsat.
Pomoci zabudovane funkce *sorted()* muzeme docilit serazeni definovane promenne.

__Ukazka__:
```python
HODNOTY = (1, 3, 4365, 23, 12, 90, 34, 7)
print(sorted(HODNOTY))

VYSKYT = {"A": 3, "B": 6, "C": 1, "D": 10}
print(sorted(VYSKYT, key=VYSKYT.get, reversed=True)
```
Nakonec nam tato vestavena funkce vraci novy seznam s hodnotami. Takze jak
mohu ziskat udaje na prvnich peti indexech?

### Dopsana IV. cast
```python
nejcastejsich_pet = sorted(vyskyt_slov, key=vyskyt_slov.get, reverse=True)[:5]
```
## Vracime vystup
Nyni potrebujeme akorat ziskat upraveny vystup nasich vysledku. Pred prvnim
vystupem chceme vypsat strucny uvod. Jak ale upravit jen nektery krok cyklu?

__enumerate__ je opet opet zabudovana funkce, kterou Python podporuje. Ukazme
si jak funguje primo na prikladu.

__Priklad__:
```python
JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]
ocislovane = enumerate(JMENA, 1)
print(list(ocislovane))

for cislo, jmeno in enumerate(JMENA, 1):
    print(f"{cislo}.: {jmeno}")
```
### Dopiseme V. cast
```python
...
for index, vysledek in enumerate(nejcastejsich_pet):
    if index == 0:
        print("VITEJTE U NASEHO POCITADLA!".center(35, " "), end=f"\n{ODDELOVAC}\n")
    else:
        print(
            f"{index}. NEJCASTEJSI SLOVO: {vysledek}, VYSKYT: {vyskyt_slov[vysledek]}",
            end=f"\n{ODDELOVAC}\n"
        )
```
Vyuzijeme funkcionalitu __enumerate__, abychom vypsali uvodni text a potom
ocislovali nejcastejsi vystupy.

## Muzeme zapis vylepsit?
V nasem kodu mame nekolikrat zapsanou smycku typu __for__. V techto smyckach
dost casto jen ukladame upravena data do nejakeho datoveho typu. V mnoha
pripadech muzeme smycku sikovne zkratit pomoci _seznamove komprehence_ neboli
zkraceneho zapisu smycky __for__.

__Priklad__:
```python
VETA2 = "   Není trapnější hloupost, než dutý zvuk krásných a vznešených slov, která však postrádají myšlenku a znalost.   "
vycisteny_seznam = [slovo.strip(",.") for slovo in VETA2.split()]
print(vycisteny_seznam)
```
### Doplnime VI. cast
```python
vycistena_slova = [slovo.strip(",.") for slovo in jednotliva_slova]
```
## Intervaly v Pythonu
Je v podstate [nezmenitelny datovy typ](https://engeto.com/cs/kurz/online-python-akademie/studium/PHnlRhS8RQK7xyKhRoEGlA/range-a-smycka-for/datovy-typ-range/range-vytvareni-a-princip),
podobne jako string nebo tuple. Jde o interval hodnot, ktery se velice casto
pouziva prave u for cyklu.

__Priklad__:
```python
# 1. zpusob
print(list(range(10)))

# 2. zpusob
print(list(range(1, 10)))

# 3. zpusob
print(list(range(1, 10, 2)))
```

## Nestovane smycky
Princip [nestovani](https://engeto.com/cs/kurz/online-python-akademie/studium/HX7RYlaNSk2AjSbGAM_kXw/range-a-smycka-for/smycka-for/vnorene-smycky),
zanorovani je v podstate vkladani jedne smycky (vnitrni) do nejake jine
(vnejsi).

__Priklad__:
```python
for number in range(0, 5):
    print("=" * 14)
    print(f"Radej cislo {number}")
    print("=" * 14)

    for cislo_bunky in range(1, 5):
        print(f"Bunka cislo {cislo_bunky}")
```

Pokracovat na [Lekci#06](https://github.com/Bralor/online-python-academy/tree/master/lesson06)

