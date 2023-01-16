# 1. Napisati funkciju koja generise sub-liste iz prosledjene liste
# Primer:
# Lista = [10,20,30,40]
# Sublist =  [[],[10],[20],[30],[40].[10,20],[10,30]...[10,20,30,40] ]

from itertools import combinations

def sublist(lista):
    sublista=[]
    for i in range(len(lista)+1):
        tekuca_lista = combinations(lista,i)
        for j in tekuca_lista:
            t=list(j)
            sublista.append(t)
    print(sublista)
    return sublista
lista_primer = [10,20,30,40]
sublist(lista_primer)