[VRATIT NA UVOD](https://github.com/Bralor/python-academy/blob/master/README.md)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 01
## Dulezite odkazy
- [Python Academy, lekce](https://engeto.com/cs/kurz/online-python-akademie/lekce)
- [Python Academy, cviceni](https://engeto.com/cs/kurz/online-python-akademie/praxe)
- [Python Academy, Git](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/lekce)
- [Python Academy, zaciname!](https://engeto.com/cs/kurz/python-academy/studium/SpmtH-mVRY6zPL9alhruMQ/home-set-up/basics-of-command-line)
- [Repl.it](https://repl.it/)

## Co nas dnes ceka?
Vytvorime jednoduchy skript pojmenovany "Destinatio". Tento program bude komunikovat s uzivatelem. Komunikaci rozumejme nejake predavani vstupu a vystupu s nasim programem. Jelikoz jde o nasi prvni spolecnou hodinu, vsechno se budeme snazit resit pomoci vzdaleneho online [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)(integrated development enviroment). Prejdeme tedy na [repl.it](#-dulezite-odkazy)!

## Co bude vysledkem?
Po spusteni by mela komunikace vypadat nasledovne:
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
JMENO: Matous
PRIJMENI: Holinka
VEK: 28
EMAIL: matous@nic.cz
HESLO: panpes738
===================================
UZIVATEL: Matous
DESTINACE: Olomouc
CENA(cil:Olomouc): 120
Jizdenku posleme na Vasi emailovou adresu: matous@nic.cz
```

## Jak zacit?
Pojdme vsichni na tuto __adresu__:
```
https://repl.it/
```
Muzeme se prihlasit pomoci _Google uctu_ a otevreme si _novy projekt_:
```
python
```

Pripadne moznost vpravo nahore primo pouzit tlacitko a ihned psat kod:
```
<> start coding
```

## Upozorneni!
S kodem, ktery dneska zapiseme pomoci [repl.it](#-dulezite-odkazy) budeme opet pracovat ve druhe hodine. Vysledek si proto muzete bud ulozit, nebo stahnout potom ode me.

## Nas prvni kod
Zadame promenne, se kterymi chceme pracovat. Ale jake?

<p align="center">
  <img src="https://media.giphy.com/media/64aBc1uYI7asXZH28O/source.gif" width="300" height="300">
</p>

## Prvne cisla
### Cela cisla, integers
Hodnoty zapisujeme pomoci [celych cisel](https://engeto.com/cs/kurz/python-academy/studium/91lewpELSZaQ6CI_vGz9ng/1-intro-to-programming/basics/data-types-overview).
```bash
# zapis pomoci Python interpretru
>>> type(1100)
<class 'int'>  # -> zkratka pro integer
>>> 1100 + 100
1200
>>> 5 - 2
3
```

### Desetinna cisla, floats
Hodnoty zapisujeme jako desetinna cisla. Oddelovac je __tecka__! Carka slouzi k jinym ucelum.
```bash
>>> type(3.1415926536)
>>> 10/3; type(10/3)
3.3333333333333335
<class 'float'>
```

### Co jeste muzeme s cisly provadet?
## Zakladni operatory
V Pythonu pouzivame [zakladni matematicke operace](https://engeto.com/cs/kurz/python-academy/studium/3mDYjEkEQJi0yNIwGTyMBw/1-intro-to-programming/numeric-data-types/arithmetic-operations). Tedy scitani, odcitani, nasobeni a deleni. Dale mame tri dalsi operace: celociselne deleni, zbytek po deleni, negace a umocnovani.

Zkousime jednotlive __operatory__:
```bash
>>> 10 + 5          # 15
>>> 10 - 5          # 5
>>> 10 * 5          # 50
>>> 10 / 5          # 2.0 (?)
>>> 10 // 3         # celociselne deleni
>>> 10 % 3          # ziskani zbytku po deleni
>>> -10             # negace
>>> 10 ** 3         # umocnovani
```

## Je libo i text? Retezce, strings!
Jde o ruzne dlouhe uskupeni [znaku](https://engeto.com/cs/kurz/python-academy/studium/p1_xjnimSui6cpwn2nISBQ/1-intro-to-programming/sequence-data-types/strings) (cisla, pismena, specialni symboly,..), ohranicenych uvozovkami.
```bash
>>> "Matous Holinka"; type("Matous Holinka")
'Matous Holinka'
<class 'str'>
>>> '1234566789'; type('1234566789')
'1234566789'
<class 'str'>
>>> "!@#$%%^&*"; type("!@#$%%^&*")
'!@#$%%^&*'
<class 'str'>
```

## Jak tedy hodnotu uchovat a vyhledat? Promenne...
[Promenne](https://engeto.com/cs/kurz/python-academy/studium/0ujrbVm0T_uX6LlvMP1D1g/1-intro-to-programming/data/variable) v Pythonu jsou je symbolickymi odkazy, ktere odkazuji na objekt v pameti.

__Predpis/syntaxe__ vypada nasledovne:
```python
<jmeno_promenne> = <hodnota> (retezec, cele_cislo, desetinne_cislo, aj.)
```

__Priklad__:
```python
MESTO = 'Praha'     # retezec, konstanta
MNOZSTVI = 2        # cele_cislo, konstanta
CENA = 1000.5       # desetinne_cislo, konstanta
```

## Promenne obsahujici vice udaju
### Seznam, list
List neboli seznam je zmenitelna posloupnost prvku. Tzn. jednotlive prvku muzeme menit, muzeme pracovat s libovolnou casti seznamu, muzeme jej rozsirovat nebo promazavat.

__Obecne__:
```python
<jmeno_seznamu> = <[>"udaj_1"<,> "udaj_2"<,> "udaj_3"<,> "udaj_4"<]>
```
__Priklad__:
```python
JMENA = ["Matous", "Marek", "Lukas", "Jan"]; type(JMENA)  # seznam s retezci
```

## N-tice, tuple
Tuple neboli n-tice je naopak nezmenitelna posloupnost prvku. Muzeme sice pouzivat jednotlive data, ale nemuzeme je menit.

__Obecne__:
```python
<jmeno_ntice> = <(>"udaj_1"<,> "udaj_2"<,> "udaj_3"<,> "udaj_4"<)>
```

__Priklad__:
```python
CISLICE = ("Biscuit", "in", "the", "basket"); type(numbers)  # n-tice s retezci
```

## Uz doopravdy muzeme zacit...
<p align="center">
  <img src="https://media.giphy.com/media/7XZEvQlmM3DJm/giphy.gif" width="300" height="300">
</p>

## Promenne na uvod
Zadame promenne, se kterymi chceme pracovat. Musime nekde uchovat jmena mest, cen a vizualni oddelovac.
```python
"""Lekce #1 - Uvod do programovani, 1/2 Destinatio"""
MESTA = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = '==================================='
```

## Nas prvni vypis z programu
Chceme oficialne uvitat uzivatele, oznamit mu nase umysly a ukazat aktualni nabidku. Jak to provedeme?

### Funce print()
Je to [vestavena funkce](https://engeto.com/cs/kurz/python-academy/studium/GzlxQFyiSSuTLjE_B99htw/1-intro-to-programming/basics/input-output-data) Pythonu (s Pythonem nainstalovana, neni nutne ji tvorit). Ucelem teto funkce je vypsat informace, ktere ji vlozime do kulatych zavorek.

__Obecne__:
```python
<jmeno_funce><(><hodnota_na_vypsani><)>
```

__Priklad__:
```python
print("Jimmy H.")
JMENO = 'James Marshall "Jimi" Hendrix'; print(JMENO)  # kombinace uvozovek!
```
Dopiseme pozdrav a info:
```python
print(ODDELOVAC)
print("Vitejte u nasi aplikace Destinatio!")
print(ODDELOVAC)
print(
"""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)
print(ODDELOVAC)
```

## Vkladame hodnoty pomoci input()
Jde opet o vestavenou funkci v Pythonu. Tato funkce ocekava od uzivatele nejakou vstupni informaci. Cokoliv do ni vlozime tato vestavena funkce standartne premeni na retezec!

__Priklad__:
```python
email = input("Your email address: "); print(email)  # matous@nic.cz
```
Od uzivatele chceme tyto vyplnene udaje:
1. Cislo mesta
2. Jmeno
3. Prijmeni
4. Rok narozeni
5. E-mail
6. Heslo

Dopsany kod:
```python
por_cislo = int(input("Vyberte cislo lokality: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)
```

## Cisla sedi?
Nas program vyzkousime a vybereme libovolnou hodnotu pro mesto, ktere pozadujeme:
```bash
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
Vyberte cislo lokality: 1
...
```
Jake mesto ale dostaneme?

## Jak vse zachranit?
### Pomoci _indexovani_
Jde o [cislo](https://engeto.com/cs/kurz/python-academy/studium/ahOxRKnuRB2NB2HCqIqRKA/1-intro-to-programming/sequence-data-types/indexing) v hranatych zavorkach zapsane ihned za jmenem promenne. Vraci objekt na urcene pozici. Zapamatujte si, ze index pozice prvni polozky je 0 (posledni -1).

__Obecne__:
```python
<jmeno_promenne_kde_mohu_indexovat><[><index><]>
```

__Priklad__:
```python
CISLICE = ("Biscuit", "in", "the", "basket")  # chci ziskat prvni, posledni udaj v ntici
CISLICE[0]; CISLICE[-1]
```
Nyni muzeme udaj opravit. Uzivatel ma totiz k dispozici pouze nas vypis. O indexovani nema ani potuchy. Proto je potreba provest zmeny na pozadi.

Doplnime zmeny s indexovanim:
```python
destinace = MESTA[por_cislo - 1]  # --> destiance[0] pokud bude por_cislo = 1
cena = CENY[por_cislo - 1]
```

## Nyni vratime, vypiseme uzivatelem vyplnene hodnoty
K tomu budeme opet potrebovat funkci _print()_ a nejen ji. Ve vzorovem vystupu vypisuji nejen predepsany text, ale obsah konkretnich promennych. Toho docilime z pravidla tremi postupy:

1. [Konkatenace](#-konkatenace-spojovani)
2. [Oddelovacem](#-oddelovac)
3. [f-string formatovani](#f-string-formatovani)

### Konkatenace, spojovani
Je to [proces](https://engeto.com/cs/kurz/python-academy/studium/1YyeD7QBTIuqU_BMzkcT_w/1-intro-to-programming/sequence-data-types/concatenation), ktery funguje jen u nekterych datovych typu (retezec, seznam, n-tice). Spoji dve ruzne promenne do jedne (pomoci "+" operatoru).

__Priklad__:
```python
print("DESTINACE: " + destinace)
```

## Oddelovac
Spojeni ruznych datovych typu na vystupu pomoci carky.

__Priklad__:
```python
DESTINACE = "Brno"
CENA = 80
print("Cestuji do", DESTINACE, "za pouhych", CENA, ",- .")
```

## F-string formatovani
Vysvetlime si podrobneji v dalsich lekcich. Zatim staci videt, jak jej pouzivat.

__Priklad__:
```python
JMENO = "Matous"
EMAIL = "matous@matous.cz"
print(f"{JMENO}, jizdenku posleme na Vasi emailovou adresu *{email}*")
```

Doplnime chybejici informace:
```python
print("UZIVATEL: " + jmeno)
print("DESTINACE: " + destinace)
print("CENA(cil:" + destinace + "): " + str(cena))
print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
```

## Malickost zaverem
Zpusob zapsani oddelovace je malicko nesikovna. Muzeme cely proces vylepsit [opakovanim](https://engeto.com/cs/kurz/python-academy/studium/QnEydRFvSu2qmTCPIVEW0Q/1-intro-to-programming/sequence-data-types/repetition). Tento proces se sklada ze sekvence, kterou budeme opakovat, operatoru pro opakovani "*" a za nim cele cislo, ktere specifikuje pocet opakovani.

__Obecne__:
```python
<uvozovky><co_opakovat><uvozovky> <operand> <kolikrat>
```

__Priklad__:
```python
"Matous" * 10
```

Nahradime hodnotu promenne __ODDELOVAC__:
```python
ODDELOVAC = "=" * 35
```

[POKRACOVAT NA LEKCI#02](https://github.com/Bralor/python-academy/blob/master/README.md)
