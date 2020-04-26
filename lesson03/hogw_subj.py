#!/usr/bin/env python3
"""
Lekce c. 3, druhy projekt - Skolni rozvrh
-------------------------------------------------------------------------------
SKUP_1 = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
		  'Ron', 'Hermiona]
SKUP_2 = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_3 = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_4 = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_5 = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']

PREDMETY = ['Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
		'Bylinkarstvi', 'Lektvary']
-------------------------------------------------------------------------------
"""
# Pomocny balicek, vyznam budeme probirat pozdeji
# Zde pouzivam pouze pro lepsi output
from pprint import pprint as pp

# P11
# Vytvorim prazdny slovnik "tridy"
ROZVRH = {}

# P12
# Definujeme predmety
PREDMETY = ('Premenovani', 'Astronomie', 'Obrana_proti_cerne_magii',
			'Bylinkarstvi', 'Lektvary')

# P13
# Propojime jmena predmetu s klici slovniku
ROZVRH[PREDMETY[0]] = None
ROZVRH[PREDMETY[1]] = None
ROZVRH[PREDMETY[2]] = None
ROZVRH[PREDMETY[3]] = None
ROZVRH[PREDMETY[4]] = None

# Doplnime studeny po skupinach k jednotlivymi predmetum
SKUP_1 = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann',
		  'Ron', 'Hermiona']
SKUP_2 = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_3 = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_4 = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_5 = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']

# P14
# Priradime skupiny do jednotlivych predmetu
ROZVRH.update(Premenovani = SKUP_1)
ROZVRH.update(Astronomie = SKUP_2)
ROZVRH.update(Obrana_proti_cerne_magii = SKUP_3)
ROZVRH.update(Bylinkarstvi = SKUP_4)
ROZVRH.update(Lektvary = SKUP_5)


# P15
# Vytvorime dva sety ze predmetu *Premenovani* a *Astronomie*
prem_s = set(ROZVRH['Premenovani'])
astr_s = set(ROZVRH['Astronomie'])

# P16
# Do *set_premenovani* pridame *Harry*
prem_s.add('Harry')

# Ze setu *set_astronomie* odebereme *Samuel*
astr_s.discard('Samuel')

# P17
# Vypiseme zmeny pred a po
print('Predmet *' + PREDMETY[0] + '* ma tyto studenty: ')
print(prem_s, type(prem_s))
print('Predmet *' + PREDMETY[1] + '* ma tyto studenty: ')
print(astr_s, type(astr_s))

# P18
# Zjistime kdo navstevuje vsechny predmety
print('Kdo se ucastni vsech predmetu: ')
pp(
	prem_s &
	astr_s &
	(set(ROZVRH['Obrana_proti_cerne_magii'])) &
	(set(ROZVRH['Bylinkarstvi'])) &
	(set(ROZVRH['Lektvary']))
	)

# P19
# Dotazovani na podmnozinu pomoci input()
print()
dotaz_1 = input(
	'Je mnoz. *OBRANA_PROTI_CERNE_MAGII* podmnozinou setu PREMENOVANI?(y/n):'
	)

if dotaz_1 == 'y':
	print('BOHUZEL NENI PODMNOZINOU?','>>>', \
			set(ROZVRH['Obrana_proti_cerne_magii']).issubset(prem_s))

else:
	print('SPRAVNA ODPOVED!')

print()
dotaz_2 = input(
	'Jsou jmena *Matous* a *Monika* mimo mnoz. *ASTRONOMIE*?(y/n):'
	)

if dotaz_2 == 'y':
	print('SPRAVNA ODPOVED!','>>>', \
			set({'Matous', 'Monika'}).disjoint(astr_s))

else:
	print('BOHUZEL NENI!','>>>', \
			set({'Matous', 'Monika'}).disjoint(astr_s))
