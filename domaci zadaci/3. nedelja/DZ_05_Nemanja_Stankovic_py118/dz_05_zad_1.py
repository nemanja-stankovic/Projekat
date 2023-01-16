# Zadatak 1. Napisati program koji će od ulaznog teksta(stringa) u sledećem obliku:
#
# REG_OZNAKABOJATIP_VOZILA
# NI-543-MMsivaautomobil
# LE-345-KMlavakamion
# BG-345-TTbelaautomobil
# KG-365-KGplavaautomobil
# SU-475-GMbelaautomobil
# KG-845-YBcrnaautobus
# NI-345-XDbelaautomobil
# UE-134-NFcrnaautomobil
# AL-226-DFbelakamion
#
# (Podaci su izlistani u zasebnim redovima, a u svakom redu su odvojeni tabom. Prvi red (REG_OZNAKA    BOJA    TIP_VOZILA) jeste deo input teksta)
#
# Napraviti izlaz u obliku:
#
# {
#     tip_vozila: {
#             "automobil": "66.67%",
#             "kamion": "22.22%",
#             "autobus": "11.11%"
#     },
#     gradovi: ["NI", "LE", "BG", "KG", "UE", "AL", "SU"],
#     boja_po_tipu: {
#         "automobil":{
#             "siva": 1,
#             "bela": 3,
#             # "plava": 1,
#             "crna": 1,
#        },
#         "kamion":{
#             "bela": 1,
#             "plava": 1
#     },
#         "autobus":{
#             "crna": 1
#         }
#     },
# }

# ulazni_string="NI-543-MM\tsiva\tautomobil\n" \
#               "LE-345-KM\tplava\tkamioin\n" \
#               "BG-345-TT\tbela\tautomobil\n" \
#               "KG-365-KG\tplava\tautomobil\n" \
#               "SU-475-GM\tbela\tautomobil\n" \
#               "KG-845-YB\tcrna\ttautobus\n" \
#               "NI-345-XD\tbela\tautomobil\n" \
#               "UE-134-NF\tcrna\ttautomobil\n" \
#               "AL-226-DF\tbela\tkamion"

provera_da_li_radi=[["REG_OZNAKA","BOJA", "TIP_VOZILA"],["NI-543-MM","siva","automobil"], ["LE-345-KM","plava","kamion"], ["BG-345-TT","bela","automobil"], ["KG-365-KG","plava","automobil"],\
  ["SU-475-GM","bela","automobil"], ["KG-845-YB","crna","autobus"], ["BG-345-TT","bela","automobil"], ["UE-134-NF","crna","automobil"], ["AL-226-DF","bela","kamion"]]

def unos_podataka():
    print("Unesite podatke\n")
    ulazni_red="random"
    lista_podataka=[]
    while ulazni_red!="":
        ulazni_red=input()
        if ulazni_red!="":
            lista_podataka.append(ulazni_red.split("\t"))
    return lista_podataka

def tipovi_vozila(lista_podataka: list) -> dict :
    tipovi_vozila={}
    vozila={}
    tip_vozila=lista_podataka[0][2]
    tipovi_vozila[tip_vozila]=vozila
    vozila_lista=[]
    vozila_lista_1=[]
    brojevi_vozila=[]
    for i in range(1,len(lista_podataka)):
        vozila_lista.append(lista_podataka[i][2])
    for i in range(len(vozila_lista)):
        count = 1
        for j in range(len(vozila_lista)):
            if vozila_lista[i]==vozila_lista[j] and i !=j:
                count+=1
        vozila_lista_1.append(vozila_lista[i])
        brojevi_vozila.append(count)
    for i in range(len(vozila_lista_1)):
        brojevi_vozila[i]=round(100*brojevi_vozila[i]/(len(lista_podataka)-1),2)
        vozila.update({vozila_lista_1[i]:str(brojevi_vozila[i])+"%"})
    return tipovi_vozila

def gradovi(lista_podataka: list) -> dict:
    registracije=[]
    for i in range(1,len(lista_podataka)):
            registracija=lista_podataka[i][0].split("-")
            registracije.append(registracija[0])
    jedinstvene_registracije=[]
    for i in range(len(registracije)):
        s=0
        for j in range(len(registracije)):
            if registracije[j]==registracije[i] and j>i:
                s+=1
        if s==0:
            jedinstvene_registracije.append(registracije[i])
    gradovi={"gradovi":jedinstvene_registracije}
    return gradovi
def boja_po_tipu(lista_podataka: list) -> dict:
    automobili=[]
    automobili_po_bojama={}
    po_bojama={}
    boje=[]
    for i in range(1,len(lista_podataka)):
        boje.append(lista_podataka[i][1])
        automobili.append(lista_podataka[i][2])
    boja=[]
    count = 0
    boja = []
    for i in range(len(automobili)):
        boja = []
        for j in range(len(automobili)):
            if automobili[i]==automobili[j]:
                boja.append(boje[j])
            automobili_po_bojama.update({automobili[i]:boja})
    for key in automobili_po_bojama:
        lista_boja=automobili_po_bojama.get(key)
        recnik_boja={}
        for i in range(len(lista_boja)):
            count_boja=0
            for j in range(len(lista_boja)):
                if lista_boja[i]==lista_boja[j]:
                    count_boja+=1
            recnik_boja.update({lista_boja[i]:count_boja})
        automobili_po_bojama.update({key:recnik_boja})
    boja_po_tipu={"boja_po_tipu":automobili_po_bojama}
    return boja_po_tipu
unos=input("Unesite 1 za unos podataka\nUnesite bilo sta drugo ako zelite da program ispise default-ne podatke\n")
if unos=="1":
    lista_podataka=unos_podataka()
else:
    lista_podataka=provera_da_li_radi
tip_vozila=tipovi_vozila(lista_podataka)
gradovi=gradovi(lista_podataka)
boja_po_tipu=boja_po_tipu(lista_podataka)
izlazni_dict={}
izlazni_dict.update(tip_vozila)
izlazni_dict.update(gradovi)
izlazni_dict.update(boja_po_tipu)
print(izlazni_dict)