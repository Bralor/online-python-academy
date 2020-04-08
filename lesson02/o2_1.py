""" Lekce #2 - Uvod do programovani, 2/2 Destinatio """
# I. KROK:
# Definujeme promenne, se kterymi chceme pracovat
# Debatovat nad optimalnim datovym typem pro nase data
SEZNAM_MEST = ('Praha', 'Viden','Brno', 'Svitavy', 'Zlin', 'Ostrava')
SEZNAM_CEN = (1000, 1100, 2000, 1500, 2300, 3400)
SEZNAM_SLEV = ('Svitavy', 'Ostrava')
ODDELOVAC = '=' * 35

# II. KROK:
# Pozdravime uzivatele a doplnime oddelovace '='
# Zobrazit uzivateli nasi nabidkou - lokalita | cena
print(ODDELOVAC)
print('Vitejte u nasi aplikace Destinatio!')
print(ODDELOVAC)
print('Prosim mrknete na nasi nabidku')
print(ODDELOVAC)
print('''
1 - Praha| 1000
2 - Viden   | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')
print(ODDELOVAC)

# III. KROK:
# Vyzadame si od uzivatele jednotlive vstup pro vybranou hodnotu (lokalita)
vyber = int(input('Vyberte cislo lokality: '))

# IV. KROK:
# Potrebujeme definovat podminku validniho vyberu.
# Platny vyber --> pocitam cenu, neplatny --> varovani
if not 0 < vyber <= len(SEZNAM_MEST):
	print('Bohuzel, takove cislo neni v nasi nabidce.')

else:
	# Pokud bude hodnota pro vyber valid --> chceme ulozit destinaci a cenu
	destinace = SEZNAM_MEST[vyber - 1]
	cena = SEZNAM_CEN[vyber - 1]

	# Vyresim slevu. Pokud "destinace" v "SEZNAM_SLEV" --> chci novou cenu
	if destinace in SEZNAM_SLEV:
		cena = 0.75 * cena
	else:
		cena = cena

# V. KROK:
# Potrebujeme detaily k rezervovanemu listku
# Jmeno, prijmeni, vek, email, heslo
print('Dekujeme za Vas nakup. Listek do: ' +  destinace) 
print('Vami koupeny listek  posleme hned, jak vyplnite kontaktni udaje.')
print(ODDELOVAC)

jmeno = input('JMENO: ')
prijmeni = input('PRIJMENI: ')
rok = int(input('ROK NAROZENI: '))
email = input('EMAIL: ')
heslo = input('HESLO: ')

# VI. KROK:
# Vyresime PODMINKU pro vek uzivatele
# Pokud je vek < 15 --> True a vypsat zpravu
if (2019 - rok) < 15:
	print('Omlouvame se, ale nenabizime nase sluzby mladistvim')

# Vyresime PODMINKU pro email uzivatele
# Prom. "email" musi obsahovat symbol "@"
elif '@' not in email:
	print('Vlozeny email neobsahuje symbol *@*')

# Vyresime PODMINKY pro heslo uzivatele
# I. Delka
# II. Musi obsahovat jak cislice, tak pismena
# III. Prvni a posledni index nesmi byt numericky vyraz
elif (
	len(heslo) < 8 or \
	heslo.isnumeric() or \
	heslo.isalpha() or \
	heslo[0].isnumeric() or \
	heslo[-1].isnumeric()
	):
	print('''
		Tvoje heslo je spatne zadane:
		1. Musi obsahovat pismena a cislice,
		2. Alespon 8 znaku dlouhe,
		3. Nesmi koncit a zacinat s cislem
		'''
		)

# VII. KROK:
# Pokud vsechny dosavadni podminku v posouzeni prihlaseni nejsou True
# --> musim skoncit v bloku ELSE, ktery obsahuji vypis udaju
else:
	print(ODDELOVAC)
	print('Dekuji ' + jmeno)
	print('Vybrali jste si destinaci: ' + destinace)
	print('Cena za dopravu do *' + destinace + '* je ' + str(cena))
	print('Listek zasleme na Vas email (' + email + ').')

