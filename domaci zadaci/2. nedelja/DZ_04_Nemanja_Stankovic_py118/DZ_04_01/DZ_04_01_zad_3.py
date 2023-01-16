# 3. Napisati fuknciju koja pronalazi unikatne vrednosti
# u datoj listi tuplova, i ispisati ih na standardnom izlazu.
# [(“h”, “g”, “l”, “k”), (“a”, “b”, “d”, “e”, “c”), (“j”, “i”, “y”), (“n”, “b”, “v”, “c”), (“x”, “z”)]
lista=[("h", "g", "l", "k"), ("a", "b", "d", "e", "c"), ("j", "i", "y"), ("n", "b", "v", "c"), ("x", "z")]

def nadji_unikate_iz_liste_tuplova(lista):
    originali=[]
    duplikati=[]
    for tuple in lista:
        for element in tuple:
            originali.append(element)                   # formiramo jednu listu originali
    for i in range(len(originali)):
        for j in range(len(originali)):                # u listi originali nalazimo duplikate i
            if originali[j]==originali[i] and j!=i:    # i smestamo u listu duplikati
                while originali[j] not in duplikati:
                    duplikati.append(originali[i])
    for duplikat in duplikati:                           # a onda te duplikate izbacujemo
         while duplikat in originali:
            originali.pop(originali.index(duplikat))
    return originali
print(nadji_unikate_iz_liste_tuplova(lista))
