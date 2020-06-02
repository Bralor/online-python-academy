#!/home/mholinka/projects/python_academy/env/bin/python
"""Demonstrativni soubor pro ukazku porovnani for loop a generatoru"""

import sys
import time
import random

from typing import List, Generator
import memory_profiler as mem_profile  # pip install memory-profiler


JMENA = ['Martin', 'Marek', 'Adam', 'Tomas', 'Patrik', 'Lukas']
PREDMETY = ['matematika', 'fyzika', 'informatika', 'anglictina', 'nemcina']

print("--------------------------")
print(f'PAMET (start): {round(mem_profile.memory_usage()[0], 5)} MB')

def seznam_lidi(pocet_lidi: int) -> List[dict]:
    vysledek = []
    for i in range(pocet_lidi):
        osoba = {
                    'id': i,
                    'jmeno': random.choice(JMENA),
                    'predmet': random.choice(PREDMETY)
                }
        vysledek.append(osoba)
    return vysledek

def generator_lidi(pocet_lidi: int) -> Generator[dict]:
    for i in range(pocet_lidi):
        osoba = {
                    'id': i,
                    'jmeno': random.choice(JMENA),
                    'predmet': random.choice(PREDMETY)
                }
        yield osoba

if __name__ == "__main__":
    mod = sys.argv[1]
    if mod == "sez":
        t1 = time.process_time()
        lide = seznam_lidi(1000000)
        t2 = time.process_time()
        print(f'PAMET (konec): {round(mem_profile.memory_usage()[0], 5)} MB')
        print(f'DOBA TRVANI: {round(t2-t1, 5)} vterin')
        print("----------CYKLUS----------")
    
    elif mod == "gen":
        t1 = time.process_time()
        lide = generator_lidi(1000000)
        t2 = time.process_time()
        print(f'PAMET (konec): {round(mem_profile.memory_usage()[0], 5)} MB')
        print(f'DOBA TRVANI: {round(t2-t1, 5)} vterin')
        print("---------GENERATOR--------")
