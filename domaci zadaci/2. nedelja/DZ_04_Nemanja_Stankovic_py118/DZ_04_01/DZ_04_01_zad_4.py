# 4. Napisati funkciju koja od datih listi kreira novu listu koja
# sadrzi parne elemente prve i neparne elemente druge liste
# i sortirati ih u opadajucem redosledu.
# [2,1,66,4,3,87] i [4, 4, 6, 99, 34, 3, 7, 10, -2, -10]
prva_lista=[2,1,66,4,3,87]
druga_lista=[4, 4, 6, 99, 34, 3, 7, 10, -2, -10]

def iskombinuj_od_parnih_iz_prve_i_neparnih_iz_druge(prva_lista,druga_lista):
    nova_lista=[]
    for i in range(len(prva_lista)):
        if prva_lista[i]%2==0:                      # trazenje parnih elemenata prve liste
            nova_lista.append(prva_lista[i])
    for i in range(len(druga_lista)):
        if druga_lista[i]%2==1:                     # trazenje neparnih elemenata druge liste
            nova_lista.append(druga_lista[i])
        sortirana_nova_lista=[]
    return (nova_lista)
def sortiraj_u_opadajucem_redosledu(nova_lista):
    for i in range(len(nova_lista)):               # sortiranje nove liste ( a moglo je i preko sort )
       for j in  range(len(nova_lista)):
           if nova_lista[j]>nova_lista[i] and j>i:
               pom=nova_lista[i]
               nova_lista[i]=nova_lista[j]
               nova_lista[j]=pom
    return nova_lista
lista=iskombinuj_od_parnih_iz_prve_i_neparnih_iz_druge(prva_lista,druga_lista)

def sortiraj_u_rastucem_redosledu(nova_lista):
    for i in range(len(nova_lista)):               # sortiranje nove liste ( a moglo je i preko sort )
       for j in  range(len(nova_lista)):
           if nova_lista[j]<nova_lista[i] and j>i:
               pom=nova_lista[i]
               nova_lista[i]=nova_lista[j]
               nova_lista[j]=pom
    return nova_lista

print(sortiraj_u_rastucem_redosledu(lista))