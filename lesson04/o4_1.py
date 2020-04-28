"""
Lekce c.4 - Databaze potravin
"""
# Importuji pomocnou knihovnu, vysvetlime si na dalsich lekcich
from pprint import pprint as pp

# P1
# Bez cyklu
CART = {}
total = 0
SWI = True
SEP = '-' * 50

# item1 = input('ZADEJTE POTRAVINU: ')
# item2 = input('ZADEJTE POTRAVINU: ')
# item3 = input('ZADEJTE POTRAVINU: ')
# item4 = input('ZADEJTE POTRAVINU: ')

# CART[item1] = None
# CART[item2] = None
# CART[item3] = None
# CART[item4] = None

# pp(CART)

# P2
# Uvod do cyklu s *while*
# while len(CART) != 4:
#     item = input('ZADEJTE POTRAVINU: ')
#     CART[item] = None

# pp(CART)

# P3
# Vytvorime slovnik s udaji
# GROCERY_DB = {
#     'mleko': 30,
#     'maso': 100,
#     'banan': 30,
#     'jogurt': 10,
#     'chleb': 20
# }

# P4
# Vypiseme sortiment v obchode
# pp(GROCERY_DB.items())

# P5
# Vybereme 3 polozky z db --> CART
# Plnime kos hodnotami ze slovniku s potravinami + chceme celkovy soucet
# while len(CART) < 3:
#     req = input(f'VYBERTE POLOZKU DO CARTU (AKT.POLOZEK: {len(CART)}): ')
#     CART[req] = GROCERY_DB[req]
#     total = sum(CART.values())

# print(SEP, CART, SEP,sep='\n')
# print(f'Cena CELKEM: {total} CZK')

# P6
# Chceme nekonecnou smycku
# while SWI:
#     req = input(f'VYBERTE POLOZKU DO CARTU (AKT.POLOZEK: {len(CART)}): ')
#     CART[req] = GROCERY_DB[req]
#     total = sum(CART.values())

#     check = input('POKRACOVAT? (y/n): ')
#     if check.lower() == 'n':
#         SWI = False 

# print(SEP, CART, SEP,sep='\n')
# print(f'Cena CELKEM: {total} CZK')

# P7
# EAN neboli carkovy kod
# 5-901234-123457 vzorova hodnota EAN13
GROCERY_DB = {
        'P1': {'produkt': 'mleko', 'cena': 30, 'Pocet': 100},
        'P2': {'produkt': 'kur.maso', 'cena': 100, 'Pocet': 100},
        'P3': {'produkt': 'banan', 'cena': 30, 'Pocet': 100},
        'P4': {'produkt': 'jogurt', 'cena': 10, 'Pocet': 100},
        'P5': {'produkt': 'chleb', 'cena': 20, 'Pocet': 100},
        }

# P8
# Vypisovani podle *P4* nebezi, potrebujeme aktualizovat
tab = []
temp_val = 0

while temp_val != len(GROCERY_DB):
    temp_ref = 'P'
    temp_val += 1
    id_link = temp_ref + str(temp_val)
    
    print('PRODUKT: ',GROCERY_DB[id_link]['produkt'], '\tCENA: ', 
        GROCERY_DB[id_link]['cena'])
    tab.append([GROCERY_DB[id_link]['produkt'], GROCERY_DB[id_link]['cena']])
print(SEP)

# P9
# Po aplikace nove db, potrebujeme upravit vyber potravin do CARTu
while SWI:
    n = 0
    item = input('VYBER ZBOZI: ')
    count = int(input('POCET KUSU: '))

    while tab:
        if item in tab[n]:
            transition = 'P' + str(n + 1)
            
            if GROCERY_DB[transition]['Pocet'] >= count:
                GROCERY_DB[transition]['Pocet'] -= count            
                CART[item] = [GROCERY_DB[transition]['cena'], count]
                total += GROCERY_DB[transition]['cena'] * count
            
            else:
                print('ZBOZI NENI SKLADEM!')

            break

        else:
            n += 1

    check = input('POKRACOVAT? (y/n): ')
    print(SEP)
    if check.lower() == 'n':
        SWI = False

# P10
# Celkova cena nakupu
print(f'TOTAL: {total} CZK')
print()
pp(GROCERY_DB)

# P11
# Odecitame polozky vlozene do CARTu z db
# if GROCERY_DB[transition]['Pocet'] >= count:
#     GROCERY_DB[transition]['Pocet'] -= count            
# else:
#     print('ZBOZI NENI SKLADEM!')