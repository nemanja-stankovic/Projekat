# Napisati program koji na ulazu prihvata jedan po jedan broj
# od strane korisnika sve dok korisnik ne unese broj 0.
# Odrediti sumu unetih brojeva koji su deljivi zbirom svojih cifara.
# Napisati funkciju za određivanje da li je
# broj deljiv zbirom svojih cifara i iskoristiti
# je na odgovarajući način za rešavanje zadatka.

def da_li_je_broj_prost(broj):  # definisemo funkciju koja proverava da li je broj prost
    s=0
    for j in range(2,broj,1):
        if broj%j==0:
            s+=1
    if s==0:
        return True
broj=1                          # broj=1 da bismo definisali promenljivu broj pre while petlje, moze biti bilo koji broj
while broj!="0":
    broj=int(input("Unesite broj:"))    # Korisnik unosi broj
    for i in range(2,broj+1,1):           # Pronalazimo sve delioce broja
        if broj%i==0:                   # Kada pronadjemo delilac
            if da_li_je_broj_prost(i):  # Proverimo da li je prost broj
                print(i)                # I tek onda ga ispisemo na izlaz

