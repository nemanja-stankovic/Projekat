# 2. Napisati program za enkripciju i dekripciju poruka. Na samom početku korisnik unosi
# poruku i ključ (celobrojnu referentnu vrednost u opsegu od 1 do 5 koja se koristi u
# procesu). Potom korisnik bira operaciju unošenjem reči “encrypt” ili “decrypt”. Program
# na izlazu prikazuje obrađenu poruku.
# ● Enkripcija se vrši tako što se za svaki karakter vrši pomeranje unapred vrednosti
# u Unicode tabeli za određeni broj vrednosti u zavisnosti od unešenog ključa.
# ● Dekripcija je inverzna operacija enkripciji - vrši se pomeranje unazad
# Isprobati program sa različitim unosima. Testirati da li su operacije inverzne.
# Hint: koristiti built-in funkcije za prevođenje karaktera u Unicode i obratno

poruka = input("Unesite poruku:\n")
kljuc = int(input("Unesite kljuc (od 1 do 5): \n"))

def encrypt(poruka, kljuc):                                                # definisemo funkciju koja za argumente uzima poruku i kljuc
    enkriptovana_poruka = ""                                               # i kao izlaz vraca enkriptovanu poruku
    for s in range(len(poruka)):
        enkriptovana_poruka = enkriptovana_poruka+chr(ord(poruka[s])+kljuc)
    return enkriptovana_poruka

def decrypt(poruka, kljuc):                                                # definisemo funkciju koja za argumente uzima poruku i kljuc
    dekriptovana_poruka = ""                                               # i kao izlaz vraca dekriptovanu poruku
    for s in range(len(poruka)):
        dekriptovana_poruka = dekriptovana_poruka+chr(ord(poruka[s])-kljuc)
    return dekriptovana_poruka

zeljena_operacija = input("Unesite encrypt ili decrypt\n")                 # korisnik unosi zeljenu operaciju
dekripcija = 0
enkripcija = 0
if zeljena_operacija == "encrypt":                                         # ako je uneo encrypt
    enkripcija = encrypt(poruka, kljuc)                                    # ispisujemo enkriptovanu poruku
    print(enkripcija)
    n = input("Da li zelite da dekriptujete poruku?\n").lower()            # a zatim ga pitamo da li zeli tu poruku da dekriptuje
    if n == "da":                                                          # ovo je opcioni deo koda koji koristimo kao proveru da li su navedene operacije inverzne
        dekripcija = decrypt(enkripcija, kljuc)                            # ako su inverzne trebalo bi da dobijemo originalnu poruku
        print(dekripcija)
else:
    if zeljena_operacija == "decrypt":                                     # a zatim ga pitamo da li zeli tu poruku da enkriptuje
        dekripcija = decrypt(poruka, kljuc)                                # ovo je takodje opcioni deo koda koji koristimo kao proveru da li su navedene operacije inverzne
        print(dekripcija)                                                  # ako su inverzne trebalo bi da dobijemo originalnu poruku
        n = input("Da li zelite da enkriptujete poruku?\n").lower()
        if n == "da":
            enkripcija = encrypt(dekripcija, kljuc)
            print(enkripcija)
    else:
        print("Pogresan unos")
