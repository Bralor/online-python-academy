# Python academy, lesson 01

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links

- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/lekce)

# Our first project
We will create simple script named "Destinatio". This program will communicate with the user (note: input/ouput)

#### CZ
Vytvorime jednoduchy skript pojmenovany "Destinatio". Tento program bude komunikovat s uzivatelem (pozn:vstup/vystup)

# Requirements:
After running the script, the communication should look like this.

#### CZ
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

# Procedure
Open your working directory and then create new python file (destinatio1.py). Then copy the text below and follow the individual steps in the text.

#### CZ
Otevrete vas pracovni adresar a vytvorte novy soubor (destinatio1.py) a zkopirujeme nasledujici text a postupujeme podle jednotlivych kroku v textu.
```
#!/usr/bin/env python3
""" Lekce #1 - Uvod do programovani, 1/2 Destinatio """

# I. KROK: 
# Zadame promenne, se kterymi chceme pracovat

# II. KROK:
# Pozdravime uzivatele, oddelime text
# Zobrazit uzivateli nasi nabidkou - <cislo> - <lokalita> | <cena>

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstupy
# cislo destinace, jmeno, prijmeni, vek, email, heslo

# IV. KROK:
# Modifikujeme tyto hodnoty

# VI. KROK:
# Vystupni sekce, vypisujeme konkretni udaje
# Jmeno, destinaci, cenu, email
```

# Prerequisites
## Integers
We write [values](https://engeto.com/cs/kurz/python-academy/studium/91lewpELSZaQ6CI_vGz9ng/1-intro-to-programming/basics/data-types-overview) using integers

#### CZ
Hodnoty zapisujeme pomoci celych cisel
```
# zapis pomoci Python interpretru
>>> type(1100)
<class 'int'>
>>> 1100 + 100
1200
```

## Floats
#### EN
We write values as decimal number. The separator is dot! Decimal point is used for other purposes.

#### CZ
Hodnoty zapisujeme jako desetinna cisla. Oddelovac je tecka! Carka slouzi k jinym ucelum.

```
>>> type(3.1415926536)
>>> 10/3; type(10/3)
3.3333333333333335
<class 'float'>
```

## Numerical operations
In Python we use basic [mathematical operations](https://engeto.com/cs/kurz/python-academy/studium/3mDYjEkEQJi0yNIwGTyMBw/1-intro-to-programming/numeric-data-types/arithmetic-operations). That is addition, subtraction, multiplication and division. We also have three other operations: floor division, remainder, negation and power.

#### CZ
V Pythonu pouzivame zakladni matematicke operace. Tedy scitani, odcitani, nasobeni a deleni. Dale mame tri dalsi operace: celociselne deleni, zbytek po deleni, negace a umocnovani.

```
>>> num1 = 5  # prvni promenna
>>> num2 = 4  # druha promenna
>>> num1 + num2
9
>>> num1 - num2
1
>>> num1 * num2
20
>>> num1 / num2
1.25
>>> num1 // num2  # celociselne deleni
1
>>> num1 % num2  # ziskani zbytku po deleni
1
>>> -num1  # negace
-5
>>> num1 ** num2  # umocnovani
625
```

## Strings
These are various long groupings of characters (numbers, letters, special symbols, ..), enclosed in quotation marks.

#### CZ
Jde o ruzne dlouhe uskupeni znaku (cisla, pismena, specialni symboly,..), ohranicenych uvozovkami.

```
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

## Variables
[Variables](https://engeto.com/cs/kurz/python-academy/studium/0ujrbVm0T_uX6LlvMP1D1g/1-intro-to-programming/data/variable) in Python are just symbolic names that are pointers to an object in physical memory.

#### CZ
Promenne v Pythonu jsou je symbolickymi odkazy, ktere odkazuji na objekt v pameti.

<jmeno_promenne> = <hodnota> (retezec, cele_cislo, desetinne_cislo)
```
mesto = 'Praha' # retezec
mnozstvi = 2    # cele_cislo
cena = 1000.5   # desetinne_cislo
```

## List
A list is a mutable element sequence. The individual elements can be changed, we can work with any part of the list, we can extend or delete it.

#### CZ
List neboli seznam je zmenitelna posloupnost prvku. Tzn. jednotlive prvku muzeme menit, muzeme pracovat s libovolnou casti seznamu, muzeme jej rozsirovat nebo promazavat.

## Tuple
A tuple, on the other hand, is an immutable sequence of elements. Although we can use individual data, we cannot change it.

#### CZ
Tuple neboli n-tice je naopak nezmenitelna posloupnost prvku. Muzeme sice pouzivat jednotlive data, ale nemuzeme je menit.

```
>>> names = ["Matous", "Marek", "Lukas", "Jan"]; type(names)  # list of strings
<class 'list'>
numbers = ("11", 11, "eleven"); type(numbers)  # list of strings
<class 'tuple'>
```

## print()
It's a built-in Python [feature](https://engeto.com/cs/kurz/python-academy/studium/GzlxQFyiSSuTLjE_B99htw/1-intro-to-programming/basics/input-output-data) (installed with Python, we don't have to create one). The purpose of this function is to list the information that we put in the round tabs.

#### CZ
Je to vestavena funkce Pythonu (s Pythonem nainstalovana, neni nutne ji tvorit). Ucelem teto funkce je vypsat informace, ktere ji vlozime do kulatych zavorek.

```
>>> print("Matous")
Matous
>>> name = 'Matous'; print(name)
Matous
```
## input()
This is again a built-in function in Python. This function expects some input information from the user.

#### CZ
Jde opet o vestavenou funkci v Pythonu. Tato funkce ocekava od uzivatele nejakou vstupni informaci.

```
>>> email = input("Your email address: "); print(email)  # matous@nic.cz
matous@nic.cz
```

## Indexing
It is just a [number](https://engeto.com/cs/kurz/python-academy/studium/ahOxRKnuRB2NB2HCqIqRKA/1-intro-to-programming/sequence-data-types/indexing) in square brackets written immediately after the variable name. It returns the object at the designed position. Remember the first item position's index is 0 (the last --> -1).

#### CZ
Jde o [cislo](https://engeto.com/cs/kurz/python-academy/studium/ahOxRKnuRB2NB2HCqIqRKA/1-intro-to-programming/sequence-data-types/indexing) v hranatych zavorkach zapsane ihned za jmenem promenne. Vraci objekt na urcene pozici. Zapamatujte si, ze index pozice prvni polozky je 0 (posledni -1).

## Concatenation
Its a [process](https://engeto.com/cs/kurz/python-academy/studium/1YyeD7QBTIuqU_BMzkcT_w/1-intro-to-programming/sequence-data-types/concatenation) that works only on some data types (string, list, tuple). It merges two different variables into one (with "+" operator)

#### CZ
Je to [proces](https://engeto.com/cs/kurz/python-academy/studium/1YyeD7QBTIuqU_BMzkcT_w/1-intro-to-programming/sequence-data-types/concatenation), ktery funguje jen u nekterych datovych typu (retezec, seznam, n-tice). Spoji dve ruzne promenne do jedne (pomoci "+" operatoru)

## Repetition
This [process](https://engeto.com/cs/kurz/python-academy/studium/QnEydRFvSu2qmTCPIVEW0Q/1-intro-to-programming/sequence-data-types/repetition) consists of sequence that will be repeated, the multiplication operator "*" and an integer that specifies the number of repetitions.

#### CZ
Tento [proces](https://engeto.com/cs/kurz/python-academy/studium/QnEydRFvSu2qmTCPIVEW0Q/1-intro-to-programming/sequence-data-types/repetition) se sklada ze sekvence, kterou budeme opakovat, operatoru pro opakovani "*" a za nim cele cislo, ktere specifikuje pocet opakovani.