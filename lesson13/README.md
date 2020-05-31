![](../images/engeto.png)
# Python academy, lesson 13

    Matous Holinka <bralor92@email.cz>
    +420 776 857 619

# Important links
- [Python Academy, lekce 13](https://engeto.com/cs/kurz/python-5/studium/Fefwhy-AQ3WsXPnmjsUH5A/iteracni-protokol-comprehensions/iteracni-protokol/co-je-to-protokol)
- [Minula lekce, repo](https://engeto.com/cs/kurz/online-python-akademie/studium/ELexreXFQqOfbmaZJIJpUQ/formaty-souboru/kviz/json)
- [JSON, obecne](https://www.json.org/json-en.html)
- [CSV, obecne](https://en.wikipedia.org/wiki/Comma-separated_values)

# Dnesni ukol
1. Komprehence
2. Lambda
3. map()
4. filter()
5. reduce()
6. functools(?)

# <Nejspis_nebude>
Nase ukoly:
```
hlavni.py           # spousti cely kod
csv_funkce.py       # obsahuje funkce s csv
...
```

# <nejspis_nebude>

```
XXX
```

```
XXX
```

```
XXX
```

# Prerequisites
- python 3.6+
- text. editor
- [handlovani chyb](https://github.com/Bralor/python_academy/tree/master/lesson09#zachazeni-s-chybami)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/master/lesson08#prace-se-soubory-pomoci-pythonu)
- [importovani](https://github.com/Bralor/python_academy/tree/master/lesson11#importovani-obecne)


# Cheatsheet s priklady
## Komprehence
### Uvodem
Teorie:
```python
# Klasicka smycka *for*
<promenna> = []

for <lib_vyraz> in <kolekce_udaju>:
    <promenna>.append(<lib_vyraz>)

# Seznamova komprehence
<promenna> = [<lib_vyraz> for <lib_vyraz> in <kolekce_udaju>]   # obecny zapis
dvakrat = [cislo * 2 for cislo in range(101)]                   # konkretni priklad
```

### Podminkou..
Teorie:
```python
# Klasicka smycka *for*
<promenna> = []

for <lib_vyraz> in <kolekce_udaju>:
    if <podminka>:
        <promenna>.append(<lib_vyraz>)

# Seznamova komprehence
<promenna> = [<lib_vyraz> for <lib_vyraz> in <kolekce_udaju> <podminka>]   # obecny zapis
dvakrat = [cislo * 2 for cislo in range(101) if cislo % 2 == 0]            # konkretni priklad
```

### Slozitejsi podminky
Teorie:
```python
<promenna> = [<lib_vyraz> if <podminka> else <lib_vyraz_2> for <lib_vyraz> in <kolekce_udaju>]      # obecny zapis
suda_licha = ["Suda" if cislo % 2 == 0 else "Licha" for cislo in range(1, 21)]                      # konkretni priklad
```

## Pro srovnani


## Lambda
1. Comma-separated values ruzneho dialektu (delimiter, header, newline)
2. Bunky rozdelene oddelovacem (delimiter, volitelny), radky newliny
3. Muzeme zapisovat (pomoci *writer/DictWriter* objektu), cist (pomoci *reader/DictReader* objektu)
