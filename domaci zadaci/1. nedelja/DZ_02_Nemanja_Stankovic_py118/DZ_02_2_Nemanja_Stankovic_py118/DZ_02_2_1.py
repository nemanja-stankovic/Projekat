#Napisati program koji za svaki uneti celi broj određuje da li uneti broj sadrži
#više parnih ili neparnih cifara. Unos prekinuti nakon što korisnik unese broj
#čije su sve cifre parne ili sve cifre neparne. Napomena: Ne koristiti operacije
#nad stringovima, već brojevima
parni=0
neparni=0
prekid=0
while prekid!=1:
    uneti_broj=float(input("Unesite celi broj: "))   # Dozvoljavamo unos realnih brojeva ali korisniku ispisujemo poruku da unese celi broj
    if uneti_broj == 0:
        print("Broj ima vise parnih nego neparnih cifara")
        prekid = 1
    if uneti_broj<0:                                 # ako je korisnik uneo negativan broj pretvaramo ga u pozitvan
        uneti_broj=uneti_broj*(-1)                   # da bi naredni deo koda radio
    if ((uneti_broj*10)%10) != 0:                    # provera da li je broj ceo
        print("Niste uneli celi broj")
    else:
        while uneti_broj> 0:                        # brojanje parnih i neparnih cifara
            cifra =uneti_broj%10
            if (cifra%2 ==0 ):
                parni+=1
            else:
                neparni+=1
            uneti_broj=(uneti_broj-uneti_broj%10)/10
        if parni>neparni:                                                   #
            print("Broj ima vise parnih nego neparnih cifara")
        else:
            if parni<neparni:
                print("Broj ima vise neparnih cifara")
            else:
                if parni==neparni!=0:                                  # razlicito od nule jer smo na pocetku za nulu stavili poseban uslov
                    print("Broj parnih cifara jednak je broju neparnih cifara")
    if (parni==0 and neparni!=0) or (parni!=0 and neparni==0) or (parni==0 and neparni==0):    # uslov da samo broj parnih ili samo broj neparnih bude 0 ili ako su oba istovremeno 0
        prekid=1
        print("Prekid programa")
    else:
        prekid=0
        parni=0
        neparni=0


