
with open("inputfile.txt","r") as f:                # otvaramo fajl i upisujemo ga u listu
    data = f.read()
lista = data.split("\n")
kasiri=[]
sume_racuna = []
for i in range(len(lista)):
    suma_racuna = 0
    if i%2==0:                                      # izdvajamo podatke za kasire iz parnih redova
        kasir=lista[i].split(":")
        kasiri.append(kasir[1].strip())
    if i%2==1:                                       # izdvajamo podatke za racune iz neparnih redova
        racuni_red=lista[i].split(":")
        racuni=racuni_red[1].split(",")
        for racun in racuni:                        # za svakog kasira obracunamo ukupnu sumu
            suma_racuna+=float(racun.strip())
        sume_racuna.append(suma_racuna)             # posle svega ovoga imacemo dve liste: kasiri i sume_racuna
for i in range(len(sume_racuna)):
    for j in range(len(kasiri)):                    # u ovom delu
        if sume_racuna[j]>sume_racuna[i] and j>i:   # obe liste
            pom=sume_racuna[i]                      # sortiramo
            sume_racuna[i]=sume_racuna[j]
            sume_racuna[j]=pom
            pom2 = kasiri[i]
            kasiri[i] = kasiri[j]
            kasiri[j] = pom2
for i in range(len(kasiri)):                         # i na kraju iz nasih listi formiramo txt fajlove
    naziv_fajla=kasiri[i]+"_"+str(i+1)+".txt"
    f=open(naziv_fajla,"w")
    data=kasiri[i]+": "+str(sume_racuna[i])
    f.write(data)
    f.close()
