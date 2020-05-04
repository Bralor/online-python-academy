#!/usr/bin/env python3
""" Lekce #5 - Uvod do programovani, hledac slov """

# I. KROK
# Zadani nasi ulohy
TEXT = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual. 
"""

# II. KROK
# Prochazime promennou *text*
# for item in TEXT:
#     print(item)

# III. KROK
# Rozdelime promennou *text*, abych prochazeli slova
jednotlive_slova = TEXT.split()

# IV. KROK
# Zakomentuj krok 2.
# Prochazime znovu
# for slovo in jednotlive_slova:
# V. KROK
# Ocistime slova, ktera obsahuji interpunkci
# ciste_slovo = slovo.strip(",.")
# print(ciste_slovo)

# Zkusime napsat pomoci *while* cyklu
# while jednotlive_slova:
#     slovo = jednotlive_slova.pop()
#     print(slovo)


# VI. KROK
# Zakomentujeme krok 4.
# Vyzkousime seznamovou komprehenci
# Utridime slova do slovniku podle vyskytu
vycistena_slova = [slovo.strip(".,") for slovo in jednotlive_slova]

# VII. KROK
# Vytvorim pomocnou promennou *vyskyt_slov*
# Pocitam vyskyt slov
vyskyt_slov = {}

for ciste_slovo in vycistena_slova:
    vyskyt_slov[ciste_slovo] = vyskyt_slov.setdefault(ciste_slovo, 0) + 1

# VIII. KROK
# Vybere 5 nejcastejsich slov
nejcastejsi = sorted(vyskyt_slov, key=vyskyt_slov.get, reverse=True)[:5]

# IX. KROK
# Upravit vystup abych mel hodnoty rozdelene
for cislo in range(len(nejcastejsi), 0, -1):
    print("=" * 23)
    for item in nejcastejsi:
        print(f"SLOVO: *{item}*, VYSKYT: {vyskyt_slov[item]}x")
        nejcastejsi.remove(item)
        break
