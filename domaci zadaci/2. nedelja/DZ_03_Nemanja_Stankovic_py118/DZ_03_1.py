def da_li_je_broj_prost(broj):                 # definisemo funkciju koja proverava da li je broj prost
    s=0                                        # kao izlaz vraca True ako je broj prost
    for j in range(2, broj, 1):
        if broj % j == 0:
            s += 1
    if s == 0:
        return True
uneti_broj=1
while uneti_broj!=0:
    uneti_broj=int(input("Unesite broj:\n"))
    for i in range(2,uneti_broj,1):                     # u for petlji nalazimo sve delioce unetog broja
        if (uneti_broj % i == 0):                       # kada pronadjemo delilac preko gore definisane funkcije
            if da_li_je_broj_prost(i):                  # proveravamo da li je broj prost i zatim ispisujemo rezultat
                print(i)

