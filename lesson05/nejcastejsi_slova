#!/usr/bin/python3
""" Lekce #5 - Uvod do programovani, hledac slov """

# I. KROK
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

ODDELOVAC = "=" * 35

# II. KROK
# rozdeleni TEXT
jednotliva_slova = TEXT.split()

# III. KROK
# ziskam ocistena slova
vycistena_slova = [slovo.strip(",.") for slovo in jednotliva_slova]
vyskyt_slov = {}

# IV. KROK
# Zjistim jejich vyskyt
for ciste_slovo in vycistena_slova:
    vyskyt_slov[ciste_slovo] = vyskyt_slov.setdefault(ciste_slovo, 0) + 1

# V. KROK
# Potrebuji 5 nejcastejsich
nejcastejsich_pet = sorted(vyskyt_slov, key=vyskyt_slov.get, reverse=True)[:6]

# VI. KROK
# Zaverecny vystup
for index, vysledek in enumerate(nejcastejsich_pet):
    if index == 0:
        print(
            "VITEJTE U NASEHO POCITADLA!".center(35, " "),
            end=f"\n{ODDELOVAC}\n")
    else:
        print(
            f"{index}. NEJCASTEJSI SLOVO: {vysledek}, VYSKYT: {vyskyt_slov[vysledek]}",
            end=f"\n{ODDELOVAC}\n"
        )


