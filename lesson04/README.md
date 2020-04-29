# Python academy, lesson 04

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links

- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/m6kdssUZTVCpXcA6W3zkBQ/rozsireni-sekvenci-smycka-while/profik-pres-sekvence/opakovani-sekvenci)
- [Walrus operator](https://realpython.com/lessons/assignment-expressions/)

# Dnesni ukol
V ramciho dnesni lekce se pokusime nasi praci v Pythonu lehce automatizovat. Probereme prvni typ cyklu v Pythonu pomoci *while ...* a povime si jak jej prakticky pouzivat.

# Nakupni kosik
Budeme chtit vytvorit virtualni kosik, do ktereho budeme moci vkladat zbozi z nabidky (ze slovniku). Nas kosik bude umet vypisovat celkovou hodnotu zbozi v kosiku a soucasne ukazovat, co je jeho obsahem.

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
{'banan': 30,
 'chleb': 20,
 'jablko': 10,
 'jogurt': 10,
 'maso': 100,
 'mleko': 30,
 'pomeranc': 15}
========================================
VYBERTE ZBOZI: chleb
VYBERTE ZBOZI: pomeranc
VYBERTE ZBOZI: maso
VYBERTE ZBOZI: exit
========================================
{'chleb': 20, 'pomeranc': 15, 'maso': 100}
========================================
CENA CELKEM: 135 CZK
```
# Prerequisites
- python 3.8!
- text. editor
- [podminky](https://github.com/Bralor/python_academy/tree/master/lesson02#podminkovy-zapis)
- [slovnik](https://github.com/Bralor/python_academy/tree/master/lesson03#slovnik)
```
KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": 30,
    "maso": 100,
    "banan": 30,
    "jogurt": 10,
    "chleb": 20,
    "jablko": 10,
    "pomeranc": 15,
}

```
# Postup
Opet si otevreme novy soubor *.py* a nakopirujeme sablonu nize:
```
#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
from pprint import pprint as pp

# I. KROK
# Vytvorime promenne, se kterymi budeme pracovat
# Nabidku potravin, *POTRAVINY*
# Prazdny slovnik, *KOSIK*
# Oddelovac, *ODDELOVAC*


# II. KROK
# Vypiseme nabidku potravin a oddelime


# III. KROK
# Vlozit 3 potraviny z vyberu do kosiku
# Pomoci input() + metod spojenymi se slovniky


# IV. KROK
# Zakomentuj predchozi kod!
# Celou ulohu predelame pomoci smycky *while*
# Plnime kosik, dokud v nem nejsou 3 predmety


# V. KROK
# Vytvorim *else* vetev
# Doplnime sumu veskereho zbozi v kosiku


# VI. KROK
# Zakomentuj predchozi kod!
# Aplikujeme nekonecnou smycku
# Koncept *break/continue* statement

# VII. KROK
# Zakomentuj predchozi kod!
# pouziti prirazovaciho operatoru *walrus operator* --> Python 3.8+

```

# Cheatsheet s priklady
# While cyklus
Je to jeden z [cyklu](https://engeto.com/cs/kurz/online-python-akademie/studium/y1BTUUW1Q12bjKt1MGVJRw/rozsireni-sekvenci-smycka-while/smycka-while/princip-while) v Pythonu, ktery umoznuje opakovat libovolnou cast naseho kodu. Opet je slovo *while* nejaky rezervovany pojem, ktery Pythonu rozezna.
```
while <podminka>:
    # provadej toto pokud je podminka pravdiva (TRUE)
# pokracuj dal, pokud smycka skoncila
```
Priklad:
```
x = 0

>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
...     x = x + 1
... 
x=0; 0<10, v poradku!
x=1; 1<10, v poradku!
x=2; 2<10, v poradku!
x=3; 3<10, v poradku!
x=4; 4<10, v poradku!
x=5; 5<10, v poradku!
x=6; 6<10, v poradku!
x=7; 7<10, v poradku!
x=8; 8<10, v poradku!
x=9; 9<10, v poradku!

```
# While + else
While cyklus ma spoustu ze sve podstaty spolecne s podminkovym zapisem. Mimo struktury zapisu napr. *else*. Pokud se podminka v zahlavi vyhodnoti jako NEPRAVDIVA, potom se nevykonava kod v odsazenem bloku po zahlavi, ale v prave *else*.
```
>>> x = 0
>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
...     x = x + 1
... else:
...     print(f"x=10; 10==10, cyklus konci!")
... 
x=0; 0<10, v poradku!
x=1; 1<10, v poradku!
x=2; 2<10, v poradku!
x=3; 3<10, v poradku!
x=4; 4<10, v poradku!
x=5; 5<10, v poradku!
x=6; 6<10, v poradku!
x=7; 7<10, v poradku!
x=8; 8<10, v poradku!
x=9; 9<10, v poradku!
x=10; 10==10, cyklus konci!
```

# Nekonecny cyklus
Jednou z moznosti, kterou *while* smycka nabizi je zapsani [nekonecne](https://engeto.com/cs/kurz/online-python-akademie/studium/jSauyS9oTWW2PX_0PL9PZw/rozsireni-sekvenci-smycka-while/smycka-while/preruseni-while-break) smycky.
Jak by smycka vypadat nemela:
```
>>> x = 0
>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
...
<ctrl+C --> ukonci>
```
Jak vytvorit nekonecnou smycku, ktera ma ucel:
```
>>> cislo = 2
>>> prepinac = True
>>> while prepinac:
...     cislo = cislo ** cislo
...     kontrola = input("PRO UKONCENI NAPIS 'q': ")
...     if kontrola == "q":
...             prepinac = False
...     else:
...             print(cislo)
... 
PRO UKONCENI NAPIS 'q': 
4
PRO UKONCENI NAPIS 'q': 
256

```
# Break + continue
V ramci pouziti smycek muzeme vyuzivat dvou ohlasenich uvnitr smycky.
1. [break](https://engeto.com/cs/kurz/online-python-akademie/studium/jSauyS9oTWW2PX_0PL9PZw/rozsireni-sekvenci-smycka-while/smycka-while/preruseni-while-break) - pri cteni odsazeneho bloku narazim na toto ohlaseni a smycku ukoncim
2. continue - ... vracim se opet do zahlavi a zacinam dalsi cyklus
Priklad BREAK:
```
>>> while cislo < 100:
...     cislo = cislo + 2
...     if cislo == 14:
...             break
...     else:
...             print(cislo)
... 
2
4
6
8
10
12
```
Priklad CONTINUE:
```
>>> cislo = 0
>>> while cislo < 100:
...     cislo = cislo + 3
...     if cislo % 15 == 0:
...             print(f"NASOBEK 15ti! Cislo --> {cislo}")
...             continue
...     else:
...             print(cislo)
... 
3
6
9
12
NASOBEK 15ti! Cislo --> 15
18
21
24
27
NASOBEK 15ti! Cislo --> 30
33
36
39
42
NASOBEK 15ti! Cislo --> 45
48
51
54
57
NASOBEK 15ti! Cislo --> 60
63
66
69
72
NASOBEK 15ti! Cislo --> 75
78
81
84
87
NASOBEK 15ti! Cislo --> 90
93
96
99
102

```

# Walrus (prirazovaci) operator
Prirazovaci operator, nebo prirazovaci vyraz je v Pythonu pomerne nova zalezitost. Jeho jmeno je odvozene od symbolu jejichz kombinace pripomina mroze. Jeho ucel spociva ve zkraceni definice promenne a jejiho pouziti do jedne konstrukce (formy zapisu).
```
>>> while ((dotaz:=input("VLOZ CISLO: ")).isnumeric()):
...     print(dotaz)
... 
VLOZ CISLO: 1
1
VLOZ CISLO: 2
2
VLOZ CISLO: 3
3
VLOZ CISLO: 4
4
VLOZ CISLO: a
>>>

```


