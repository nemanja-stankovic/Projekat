# 2. Napisati funkcije koja kao argumente primaju dve liste,
# a vracaju listu koja predstavlja presek/razliku tih listi.
# Primer razlike:
# Lista1=[10,20,30,40]
# Lista2=[10,30,50,70]
# Izlazna_lista = [20,40,50,70]
# Primer preseka:
# Lista1=[10,20,30,40]
# Lista2=[10,30,50,70]
# Izlazna_lista = [10,30]

Lista1=[10,20,30,40]
Lista2=[10,30,50,70]

def nadji_presek_dve_liste(lista_1,lista_2):
    presek_listi=[]
    for element_1 in lista_1:
        for element_2 in lista_2:
            if element_1==element_2:
                presek_listi.append(element_1)
    return presek_listi

def nadji_razliku_dve_liste(lista_1,lista_2):
    razlika_liste_1 = []
    razlika_liste_2 = []

    for element_1 in lista_1:                  # prvo nalazimo po cemu se prva lista razlikuje od druge liste
        s=0                                    # koristimo brojac koji se povecava svaki put kada su elementi razliciti
        for element_2 in lista_2:
            if element_1!=element_2:
                s+=1
        if s== len(lista_2):                   # ako je brojac dostigao duzinu liste to znaci da su svi elementi
            razlika_liste_1.append(element_1)  # iz druge liste razliciti i dodajemo taj element u listu
    for element_2 in lista_2:                  # na isti nacin dobijamo po cemu se druga lista razlikuje od prve
        s=0
        for element_1 in lista_1:
            if element_2!=element_1:
                s+=1
        if s== len(lista_1):
            razlika_liste_2.append(element_2)
    razlika_listi=razlika_liste_1+razlika_liste_2
    return razlika_listi
print(nadji_presek_dve_liste(Lista1,Lista2))
print(nadji_razliku_dve_liste(Lista1,Lista2))

