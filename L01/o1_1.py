#!/usr/bin/env python3
""" Lekce #1 - Uvod do programovani, 1/2 Destinatio """

# I. KROK: 
# Definujeme promenne, se kterymi chceme pracovat
# Debatovat nad optimalnim datovym typem pro nase data
SEZNAM_MEST = ('Praha', 'Viden','Brno', 'Svitavy', 'Zlin', 'Ostrava')
SEZNAM_CEN = (1000, 1100, 2000, 1500, 2300, 3400)
ODDELOVAC = '=' * 35

# II. KROK:
# Pozdravime uzivatele a doplnime oddelovace '='
# Zobrazit uzivateli nasi nabidkou - lokalita | cena
print(ODDELOVAC)
print('Vitejte u nasi aplikace Destinatio!')
print(ODDELOVAC)
print(
'''
1 - Praha| 1000
2 - Viden   | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')
print(ODDELOVAC)

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstupy
# cislo destinace, jmeno, prijmeni, vek, email, heslo
vyber = int(input('Vyberte cislo lokality: '))
jmeno = input('JMENO: ')
prijmeni = input('PRIJMENI: ')
vek = int(input('VEK: '))
email = input('EMAIL: ')
heslo = input('HESLO: ')
print(ODDELOVAC)

# IV. KROK:
# Modifikujeme tyto hodnoty,
destinace = SEZNAM_MEST[vyber - 1] # --> destiance[0] pokud bude vyber = 1
cena = SEZNAM_CEN[vyber - 1]

# VI. KROK:
# Vystupni sekce, vypisujeme konkretni udaje
# Jmeno, destinaci, cenu, email
print('Dekuji ' + jmeno)
print('Vybrali jste si destinaci ' + destinace)
print('Cena za dopravu do ' + destinace + ' je ' + str(cena))
print(f'Listek posleme na Vas email ({email})')


