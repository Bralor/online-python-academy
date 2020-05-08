#!/usr/bin/env python3
"""Lekce #7 - Uvod do programovani, kalkulacka"""

# I. KROK
# Zadame pomocne promenne
COM = 'DOSTUPNE OPERACE: '
OPS = '+', '-', '*', '/', 'AVR', 'PWR'
SEP = '-' * 19

# II. KROK
def main():
    """
    Hlavni funkce, ma na starost komunikaci s uzivatelem + predavat data
    dalsim funkcim
    """
    print(COM, SEP, '|'.join(OPS), SEP, sep='\n')
    swi = True

    while swi:
        ops_input = input('OPERACE (\'q\'- konec): ')

        # III. KROK
        # Zakladni aritmeticke operace
        if ops_input in OPS[:4]:
            x1 = int(input('CISLO 1: '))
            x2 = int(input('CISLO 2: '))

            op_result = math_op(ops_input, x1, x2)
            print(SEP, f'{x1} {ops_input} {x2} = {op_result}', SEP, sep='\n')
        
        # IV. KROK
        # Umocnovani cisel
        elif ops_input.upper() == 'PWR':
            x1 = int(input('CISLO: '))
            exp = int(input('EXPONENT: '))
            
            pow_result = power_OP(x1, exp)
            print(SEP, f'{x1}^{exp} = {pow_result}', SEP, sep='\n')

        # V. KROK
        # Prumerna hodnota
        elif ops_input.upper() == 'AVR':
            nums = input('VLOZTE CISLA ODDELENA CARKOU: ')
            conv_nums = [int(num) for num in nums.split(',')]

            avg_result = average_op(conv_nums)
            txt = 'CISLA: {} PRUMER: {}' .format(str(conv_nums)[1:-1], avg_result)  # budeme resit metody formatovani
            print(SEP, txt, SEP, sep='\n')

        # VII. KROK
        # Pokud bude vstup "stop", chceme ukoncit smycku
        elif ops_input == 'q':
            swi = False
            print('Doufam, ze se Vam kalkulacka libila! ^^')

# P9
def math_op(ops, x1, x2):
    """Jednoduche matematicke operace"""
    return {
            '+': x1 + x2,
            '-': x1 - x2,
            '*': x1 * x2,
            '/': x1 / x2
            }.get(ops)


# P10
def average_op(nums):
    """Funkce na pocitani prumerne hodnoty"""
    return round(sum(nums) / len(nums), 2)


# P11
def power_OP(cislo, exp):
	"""Vstupni hodnoty jsou cela cisla. Vraci cislo umocnene hodnotou exp"""
    return cislo ** exp


# P12
main()
