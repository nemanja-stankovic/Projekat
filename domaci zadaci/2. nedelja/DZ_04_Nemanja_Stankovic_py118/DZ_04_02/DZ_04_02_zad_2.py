# 2. Napisati funkciju koja će, na osnovu prosleđenog teksta, odrediti procenat učestalosti
# pojavljivanja svakog jedinstvenog karaktera u tom tekstu
# Primer
# Ulaz: “say hello to my little friend”
# Izlaz: {“a”: 3.45, “d”: 3.45, “e”: 10.35, “f”: 3.45, “h”: 3.45, “i”: 6.9, “l”:13.8, …, “ “: 17.24}
def nadji_ucestalost_pojavljivanja_karaktera(tekst):
    recnik={}
    for s1 in tekst:
        t=100 * tekst.count(s1) / (len(tekst))
        recnik[s1] = round(t, 2)
    print("Ucsestalost pojavljivanja karaktera u vasem tekstu je sledeca:\n",recnik)
ulazni_tekst=input("Unesite neki tekst:\n")
nadji_ucestalost_pojavljivanja_karaktera(ulazni_tekst)