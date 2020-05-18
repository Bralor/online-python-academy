![](../images/engeto.png)
# Python academy, lesson 10

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/JPMWQwarTtuOMOKnEQo-CA/debugovani/debugging)
- [Vice o pdb](https://docs.python.org/3/library/pdb.html)

# Dnesni ukol
Budeme pokracovat v nasi cesta za porozumeni chybam, vyjimkam a debugovani.

# Debugujeme udaje
Predstavme si situaci. Nas vedouci nam zada ukol, zpracovat textovy soubor s udaji. Chceme jej cely projit a naformatovat vystup jako _Udaj1, Udaj2_ (pocatecni pismeno velke, zbytek malym pismem a oba udaje oddelene carkou). Udaju je hromada a rekne, ze chce zpracovat jen cast, proto byl do nasich dat predem umisteny retezec *quit*, ktery ukonci cast dat pro upraveni.

# Nas cil
Vystup by na konci lekce mohl vypadat nasledovne:
```
...
United Kingdom*,London
United States,Washington
Uruguay,Montevideo
Uzbekistan,Tashkent
Vanuatu,Port Vila
Vatican City,Vatican City
Venezuela,Caracas
Vietnam,Hanoi
Yemen,Sana'A
Zambia,Lusaka
Zimbabwe,Harare
```

# Prerequisites
- python 3.6.9+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)


# Postup
Opet si otevreme novy soubor *check_type.py* a nakopirujeme sablonu nize:
```
#!usr/bin/env python3

```

# Teorie s priklady
## Debugovani, na uvod
Nejlepsim zpusobem jak overit, jestli nas kod funguje jak ma, je spustit jej. Cim vice ruznych variant spusteni vyzkousim, tim mene chyb objevime pozdeji. Presto se muze stat, ze vsechny moznosti dostatecne neosetrime.

## Jak debugovat
Nejjednodusi zpusobem, kterym zacit je vypisovat konkretni vystupy pomoci funkce _print()_. Dalsi moznosti je zabudovana funkce _vars()_, ktera extrahuje hodnoty nasich lokalnich promennych.

Priklad:
```
def funkce(*args):
     print(vars())

# volani vzor 
funkce(1, 2, 3)
funkce(["a", "b", "ce", "de"])
```

## pdb
Debugovat pomoci zabudovanych funkci muze byt napomocne, ale casto potrebujeme [*silnejsi kalibr*](https://engeto.com/cs/kurz/online-python-akademie/studium/u1Q4X1ZbRnq4JVVAan2Wkw/debugovani/python-debugger/zapiname-pdb). Vetsina textovych editoru ma vlastni debugger. My si ale povime neco o standartnim debuggeru pojmenovanem _pdb_.

Priklad#01:
```
python cities_debug.py
Afghanistan,Kabul
Albania,Tirana
Algeria,Algiers
Andorra,Andorra La Vella
...
```

## Status?
Vsechno vypada na prvni pohled skvele! Pockat... To nejsou vsechna mesta. Vratilo se nam pouze XY dvojic.

## Jak to vyresit?
Muzeme samozrejme kazdy podezrely radek debugovat pomoci _print()_. Nicmene my si vyzkousime jestli by nam lepe nedovedl poslouzit debugger *pdb*.

Priklad spousteni pdb:
```
$ python -m pdb cities_debug.py
> /home/mholinka/projects/python_academy/lesson10/cities_debug.py(2)<module>()
-> """Lekce #10 - Uvod do programovani, debugging"""
(Pdb)
```

## Dalsi krok
Pokud napiseme _c_ (continue), program probehne cely az do mista s problemem.

Ukazka:
```
Dominican Republic,Santo Domingo
The program finished and will be restarted
> /home/mholinka/projects/python_academy/lesson10/cities_debug.py(2)<module>()
-> """Lekce #10 - Uvod do programovani, debugging"""
(Pdb)
```
Vidime, ze zadna vetsi zmena nenastala. Program probehl podobne jako u spusteni bez _pdb_. Vsimneme si, ze nevyskocila zadna chyba. Pravdepodobne bude problem nejaka zapeklita logicka chyba.

## Krok za krokem
Musime malicko zuzit moznosti, kde se nase chyba vyskytuje. Proto pouzijeme _s_(step), pomoci ktereho se budeme presouvat krok za krokem skrz scenar naseho souboru.

Ukazka:
```
(Pdb) s
> /home/mholinka/projects/python_academy/lesson10/cities_debug.py(15)<module>()
-> def zpracuj_udaje(jmeno_souboru) -> None:
(Pdb) s
> /home/mholinka/projects/python_academy/lesson10/cities_debug.py(27)<module>()
-> zpracuj_udaje("cities.txt")
(Pdb) 
```

## Trochu zvysime tempo
Pokud chceme zobrazit seznam vice radku, pouzijeme prepinac _l_(list). Vsimneme si, ze aktualni radek je oznaceny sipkou _->_.

Vzorova ukazka:
```
 ...	
 15 ->	def zpracuj_udaje(jmeno_souboru) -> None:
 16  	    with open(jmeno_souboru, "rt") as soubor:
 17  	        for radek in soubor:
 18  	            radek = radek.strip()
 19  	            if "quit" in radek.lower():
 20  	                return
 21  	            zeme, mesto = radek.split(",")
 22  	            mesto = mesto.strip()
(Pdb) 
```
## Breakpoint
Musime pouzit trochu dedukce a uvazit, na kterem radku muze byt problem. Jakmile vydedukujeme problemove misto, pouzijeme tzv. _breakpoint_. V prikladu nize nastavime breakpoint na radek 20 a zkusime spustit znovu nas program.

Priklad:
```
(Pdb) b 20
```
Pokud chcete zobrazit vsehcny vase breakpointy, staci napsat pouze _b_.

## Ze by?
Sledujme, ze posledni vypsany radek:
```
Dominican Republic,Santo Domingo
> /home/mholinka/projects/python_academy/lesson10/cities_debug.py(20)zpracuj_udaje()
-> return
```
Nas breakpoint se ukazal vhodny a naznacil, ze po meste _Santo Domingo_ se kod dostal do vetve obsahujici *return* a skoncil.
Zkontrolujeme, jaka hodnota je ulozena ve smycce v promenne _radek_.
```
(Pdb) l
(Pdb) p radek
'ECUADOR, QUITO'
(Pdb) 
```
To ale nevypada, ze by tu bylo... *QUIT*O

## Zaverecne opravy
Cim vice chyb odchytime pri psani, tim mene jich nas bude trapit pozdeji.

Priklad:
```
if "quit" == radek.lower():
    return
```

## Pycharm a debugovani
