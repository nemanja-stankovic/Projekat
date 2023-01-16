import random
cena_dostave = 109
cena_pice = 0
popust=0
dodatna_naknada=0
v=1
while v!= 0:                                         # ako je korisnik zavrsio sa izborom pica unece 0
    vel=input("Unesite velicinu pice (S,M,L): ")
    print("\nUneli ste velicinu ",vel )             # obavestavamo korisnika sta je izabrao
    lose_vreme = False
    verovatnoca = random.randint(1, 100)
    if verovatnoca <= 35:                   # generisemo verovatnocu loseg vremena
        lose_vreme = True
    if lose_vreme == True:
        dodatna_naknada=50                   # ako je vreme lose naknada je 50din
    else:
        dodatna_naknada=0
    if vel=="S" or vel=="s":                 # definisemo cenu na osnovu izbora velicine pice
        cena=500
        print("Cena S velicine je: ",cena)
    else:
        if  vel=="M" or vel=="m":
            cena=650
            print("Cena M velicine je: ", cena)
        else:
            if vel=="L" or vel=="l":
                cena = 770
                print("Cena L velicine je: ", cena)
            else:
                print("Ta velicina ne postoji, pokusajte ponovo")  # ako je unos nevalidan trazimo ponovni unos
                cena=0                                             # cena je 0 u tom slucaju
    v=int(input("Da li zelite da narucite jos jednu picu (unesite 0 za ne, bilo koji broj za da)"))
    cena_pice=cena_pice+cena                                      # oredjujemo ukupnu cenu za sve pice koje korisnik unese
    iznos=cena_pice+cena_dostave
    if iznos>800:
        popust=0.2*iznos
        iznos=0.8*iznos+dodatna_naknada
    else:
        popust=0
print("\nCena pice je ", cena_pice,"din,","cena dostave je",cena_dostave,"din,","popust je",round(popust,2),"din,","dodatna_naknada je",dodatna_naknada,"din,")
print(cena_pice,"din +",cena_dostave,"din -",round(popust,2),"din +",dodatna_naknada,"din =" )
print("Vaš ukupni račun je", round(iznos,2), "din")

