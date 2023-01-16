# 1. Napisati funkciju koja će prikazati sve podskupove unetog seta
# Primer
# Ulaz: {1, 2, 3}
# Izlaz: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
from itertools import combinations

def podskupovi(skup):
    lista = list(skup)
    sublista=[]
    for i in range(len(skup)+1):
        tekuci_skup = combinations(lista,i)
        for el in tekuci_skup:
            t=set(el)
            sublista.append(t)
    print(sublista)
skup_primer= (1, 2, 3)
podskupovi(skup_primer)
