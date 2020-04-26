# Python academy, lesson 03

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links

- [Python Academy](https://engeto.com/cs/kurz/online-python-akademie/lekce)
- [The Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_1)
- [The Godfather](https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1)
- [The Dark Knight](https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1)
# Movie_dictionary


## Dnesni ukoly
Vypracovani dvou kratkych ukolu, kde si vysvetlime zaklady pro praci s novymi datovymi typy. Prvni ukol "movie_db.py" je zamereny na seznameni se se slovniky (dictionaries) a druhy ukol "hogw_subj.py" nas seznami s mnozinami (sety).

# Nase cile
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

Druha uloha:
```

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
## Vytvoreni slovniku


## Vkladani klicu

## Mazani klicu

## Nestovani

## Metody slovniku
