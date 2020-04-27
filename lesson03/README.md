# Python academy, lesson 03

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links

- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/studium/O6aWKNU3QmWpnO5PKd1orw/slovniky-a-mnoziny/co-te-ceka-v-teto-lekci)
- [The Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_1)
- [The Godfather](https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1)
- [The Dark Knight](https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1)

# Dnesni ukoly
Vypracovani dvou kratkych ukolu, kde si vysvetlime zaklady pro praci s novymi datovymi typy. Prvni ukol "movie_db.py" je zamereny na seznameni se se slovniky (dictionaries) a druhy ukol "hogw_subj.py" nas seznami s mnozinami (sety).

# Filmova databaze
Vytvorime kratky skript, kam budeme ukladat informace o filmech. Soucasne budeme chtit vyuzivat nektere metody pro slovniky a naucit se neco malo o jejich funkcionalite.

# Nas I. cil
Nas zaverecny vystup pro prvni ulohu:
```
=======================================
Vitejte v nasi skromne filmove databazi
=======================================
Mame v nabidce tyto snimky:
['Shawshank Redemption', 'The Godfather']

=======================================
Vyberte film: The Godfather
=======================================
{'HODNOCENI': 92,
 'HRAJI': ['Al Pacino', 'Marlon Brando'],
 'JMENO': 'The Godfather',
 'REZISER': 'Francis Ford Coppola',
 'ROK': 1972,
 'STOPAZ': '175 min'}
```

# Prerequisites
Zkopirujeme zadane slovniky do noveho souboru:
```
film1 = {
'JMENO': 'Shawshank Redemption',
'HODNOCENI': 93,
'ROK': 1994,
'REZISER': 'Frank Darabont',
'HRAJI': ['Tim Robbins', 'Morgan Freeman'],
'STOPAZ': "144 min"
}

film2 = {
'JMENO': 'The Godfather',
'HODNOCENI': 92,
'ROK': 1972,
'REZISER': 'Francis Ford Coppola',
'HRAJI': ['Al Pacino', 'Marlon Brando'],
'STOPAZ': "175 min"
}

film3 = {
'JMENO': 'The Dark Knight',
'HODNOCENI': 90,
'ROK': 2008,
'REZISER': 'Christopher Nolan',
'HRAJI': ['Christian Bale', 'Heath Ledger'],
'STOPAZ': "152 min"
}
```

# Postup I.
Vytvorime si novy soubor, pojmenujeme jej "movie_db.py" a zkopirujeme nasledujici sablonu:
```
#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Movie dictionary """
# ~~~~~~~~~~~~~~~~~~~ZADANI ULOHA I~~~~~~~~~~~~~~~~~~~
...
# ~~~~~~~~~~~~~~~~~~~~KONEC ZADANI~~~~~~~~~~~~~~~~~~~~

# I. KROK
# Vytvorim novy (prazdny) slovnik + oddelovac


# II. KROK
# Vlozime klice (opet zatim prazdne)


# III. KROK
# Doplnime hodnoty klicu
# Primo + update() metodou
# Kombinace s input()


# IV. KROK
# Vytvorime dalsi dva klice s hodnotami
# Klic *STOPAZ* odstranime pomoci metody *pop*
# Z klice *HRAJI* odstranime pomoci funkce *del*


# V. KROK
# Vytvorime novy slovnik *filmova_db*
# Nestujeme dva zbyvajici slovniky ze zadani


# VI. KROK
# Vytvorime pomyslneho interpreta nasi db
# Ten predstavi nase filmy


# VII. KROK
# Vyzkousime metodu slovniku .get()


# VIII. KROK
# Vyzkousime metodu slovniku .setdefault()
# pp(filmova_db.get(film, filmova_db.setdefault(film, )))

```

# Cheatsheet s priklady
## Slovnik
Slovnik je specialni datovy typ, ktery je tvoreny dvojicemi *klic: hodnota*. Jsou postavene tak, abychom pri hledani urciteho klice ziskali nazpet jeho hodnotu.

## Vytvoreni slovniku
Zpusobu pro vytvoreni slovniku je vice. Dva nejjednodussi priklady:
```
novy_slovnik = dict()
novy_slovnik2 = { 'Jmeno' : 'Marek', 'Prijmeni' : 'Janek' }
```

## Vkladani klicu
Klice (jmeno klice) musi byt unikatni. Prvni metoda vytvoreni klice pomoci hranate zavorky:
```
slovnik = dict()
slovnik["Jmeno"] = "Matous"
```
Pomoci metody .update()
```
slovnik = dict()
slovnik.update({"Jmeno": "Matous"})
```

## Mazani klicu
1. zpusob jak mazat klic
```
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
del slovnik["Jmeno"]
```
2. Zpusob vraci hodnotu spojenou s klicem jako vystup a odebere par ze slovniku
```
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
slovnik.pop("PRIJMENI")
```
3. Zpusob .popitem() vrati naposledy pridanou polozku (par) do slovniku a odebere jej:
```
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
slovnik["EMAIL"] = "matous@matous.cz"
slovnik.popitem()

```

## Nestovani
Tento princip muzeme chapat jako vkladani slovniku do slovniku (plati i pro jine datove typy). Pomoci tohoto principu muzeme vytvaret strukturovanejsi promenne.

```
nadrazeny_slovnik = dict()
potomek1 = {"Jmeno": "Matous"}
potomek2 = {"Jmeno": "Lukas"}
potomek3 = {"Jmeno": "Jan"}
nadrazeny_slovnik["1_slovnik"] = potomek1
nadrazeny_slovnik["2_slovnik"] = potomek2
nadrazeny_slovnik["3_slovnik"] = potomek3
```

## Pohledy
- .items()
- .keys()
- .values()

## Metody slovniku
- .get() Najdu klic a vratim jeho hodnotu. Pokud neni muze vracet preddefinovanou zpravu
.setdefault() Nastavi novy klic, pokud jej nenajde uvnitr slovniku, kam promennou ukladam. Defaultni hodnota "None".

# Subjects in Hogwarts
# Nas II. cil
Nas zaverecny vystup pro druhy ukol:

```
PRED PRIDANIM CLENA: 
['Adam', 'Chelsea', 'Marcus', ... ]
PO PRIDANI CLENA: 
{'Alex', 'Marcus', 'Ann', ... ] <class 'set'>

Kdo se ucastni vsech predmetu: 
{'Hermiona'}

ODPOVED PODMNOZINY --> False
ODPOVED ODLISTNOST --> True
```

# Prerequisites
```
# Promenne
PREDMETY = (
    'Premenovani',
    'Astronomie',
    'Obrana_proti_cerne_magii',
    'Bylinkarstvi',
    'Lektvary'
)

SKUP_PREMENOVANI = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann', 'Ron', 'Hermiona]
SKUP_ASTRONOMIE = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_OBRANA = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_BYLINKARSTVI = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_LEKTVARY = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']
```

# Postup II.
Vytvorime si druhy soubor, pojmenujeme jej "hogw_subj.py" a zkopirujeme nasledujici sablonu:
```
#!/usr/bin/env python3
""" Lekce #3 - Uvod do programovani, Hogwards subjects """
# ~~~~~~~~~~~~~~~~~~~ZADANI ULOHA II~~~~~~~~~~~~~~~~~~~
...
# ~~~~~~~~~~~~~~~~~~~~KONEC ZADANI~~~~~~~~~~~~~~~~~~~~
# I. KROK
# Vytvorim prazdny slovnik "rozvrh"


# II. KROK
# Klice slovniku budou stringy z promenne PREDMETY
# Hodnoty klicu jsou seznamy skupin


# III. KROK
# Vytvorime sety studentu v jednotlivych klicich


# IV. KROK
# Do *set_premenovani* studenta se jmenem *Harry*
# Ze setu *set_astronomie* odebereme *Samuel*


# V. KROK
# Vypiseme zmeny po pridani/odebrani


# VI. KROK
# Zjistime, kdo navstevuje vsechny predmety


# VII. KROK
# bool test na podmnoziny (S.issubset())
# Je vsichni studenti z hodin obrany v hodine premenovani


# VIII. KROK
# S.isdisjoint()
# Jsou studenti v prom. *NOVI_STUDENTI* uplne odlisne hodnoty 
```

# Cheatsheet s priklady
## Mnozina
Mnozinou tedy oznacujeme neusporadanou kolekci unikatnich hodnot. Nema tedy poradi a zarucuje, ze kazda promenna je v nem je jedenkrat. Do mnoziny muzeme hodnoty pridavat/odebirat. 

## Vytvoreni
Vytvoreni pomoci dvou zpusobu:
```
novy_set = set(); type(novy_set)
```
... nebo ...
```
novy_set2 = {"Matous", "Marek", "Lukas", "Jan"}; type(novy_set2)
```

## Manipulace
Udaje muzeme pridavat a odebirat:
```
novy_set = set()
novy_set.add("Matous")
novy_set.add("Marek")
print(novy_set)
novy_set.discard("Matous")
print(novy_set)
```

## Operace
[Seznam](https://engeto.com/cs/kurz/online-python-akademie/studium/6xiZIR4FS5iG2I27YUny2A/slovniky-a-mnoziny/mnoziny/sjednoceni-union) vsech operaci, ktere s mnozinami muzete provadet.

## Podmnozina
Jde o vracenou boolean hodnotu, ktera popisuje jestli se vsechny prvky z jednoho setu nachazeji v setu druhem.
```
>>> set1 = {"a", "b", "c", "d", "e"}
>>> set2 = {"a", "b", "c"}
>>> set3 = {1, 2, 3, "a", "b"}
>>> set2.issubset(set1)
True
>>> set3.issubset(set1)
False
>>> set3.issubset(set1)

```

## Disjunkce
Opet vracena hodnota je boolean hodnota. True znamena odpoved PRAVDA, pokud dva sety (a jejich hodnoty) nemaji zadnou spolecnou hodnotu.

```
>>> set5 = {"a", "b", "c", "d", "e"}
>>> set6 = {"f", "g", "h"}
>>> set7 = {"h", "i", "j", "k"}
>>> set5.isdisjoint(set6)
True
>>> set6.isdisjoint(set7)
False

```