# 3. Potreban nam je program pomoću kojeg ćemo pratiti uspeh studenata na ispitima. Za
# svakog studenta pamtimo ime, prezime, broj indeksa, šifru smera i sve predmete koje
# treba da položi ili je položio sa ocenom od 6 do 10. Za svaki predmet koji je dodeljen
# studentu znamo naziv i jedinstvenu šifru predmeta.
# Na osnovu unetih podataka, potrebno je da program omogući prikaz (ima sledeće
# funkcionalnosti):
# a. svih položenih ispita određenog studenta
# b. srednje ocene određenog studenta
# c. podataka studenta/studenata sa navećom prosečnom ocenom

# d. podataka studenta/studenata sa najmanje položenih ispita
# e. svih studenta koji su položili sve ispite na predmetima koji su im dodeljeni

# f. raspodele studenata po smerovima, u procentima
# g. sve studente na odabranom smeru

# h. najboljeg studenta na odabranom smeru
# i. sve predmete koji nije položio niti jedan student

# j. predmeta sa najvećom prosečnom ocenom
# Kada se program pokrene, prikazati korisniku glavni meni sa opcijama a - j (koje može
# da unese sa tastature). Nakon odabira opcije, ukoliko je potrebno, od korisnika
# zahtevati unos podataka i prikazati željene rezultate. Potom, ponovo prikazati glavni
# meni.
# Korisnik prekida program odabirom opcije “Kraj programa”
# (Bonus) Dodati opcije za unos ocene studentu nakon položenog ispita
# (Bonus) Dodati opciju za dodavanje novog studenta
# (Bonus) Dodati opciju za dodeljivanje novog predmeta postojećem studentu
# (Bonus) Dodati opciju za uklanjenje predmeta postojećem studentu, pod uslovom da
# nije položen
# (Bonus) Dodati opciju za brisanje studenta, pod uslovom da nije položio niti jedan ispit

studenti = {

"2008/205" :    {
        "ime": "Nemanja",
        "prezime": "Stankovic",
        "indeks": "2008/205",
        "smer": "OG",
            "predmeti":
            {
                "MAT3" :   {"naziv":"matematika 3", "ocena": 5, "sifra" : "MAT3"},
                "EE":      {"naziv":"elementi elektronike", "ocena": 5,"sifra": "EE" },
                "AM":      {"naziv":"asinhrone masine ", "ocena": 5,"sifra": "AM" },
                "SM" :     {"naziv":"sinhrone masine", "ocena": 10,"sifra": "SM" },
                "MAE":     {"naziv":"materijali u elektrotehnici", "ocena": 10,"sifra": "MAE" },
                "EES1":    {"naziv":"analiza elektroenergetskih sistema 1","ocena" : 10,"sifra": "EES1" },
                "EES2":    {"naziv":"analiza elektroenergetskih sistema 2", "ocena":6,"sifra": "EES2"},
                "ENG3":    {"naziv":"engleski 3", "ocena": 7,"sifra": "ENG3" },
                "INST1":    {"naziv":"instalacije 1", "ocena": 10,"sifra": "INST1" },
                "OGPPK":    {"naziv":"praktikum iz koriscenja racunara", "ocena": 8,"sifra": "OGPPK" }
            }
                }
, "2009/008":  {
        "ime": "Marija",
        "prezime": "Markovic",
        "indeks": "2009/008",
        "smer": "TK",
        "predmeti":
                    {
                        "MAT3": {"naziv": "matematika 3", "ocena": 5, "sifra": "MAT3"},
                        "EE": {"naziv": "elementi elektronike", "ocena": 5, "sifra": "EE"},
                        "AM": {"naziv": "asinhrone masine ", "ocena": 10, "sifra": "AM"},
                        "SM": {"naziv": "sinhrone masine", "ocena": 10, "sifra": "SM"},
                        "MAE": {"naziv": "materijali u elektrotehnici", "ocena": 10, "sifra": "MAE"},
                        "EES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 10, "sifra": "EES1"},
                        "EES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 10, "sifra": "EES2"},
                        "ENG3": {"naziv": "engleski 3", "ocena": 10, "sifra": "ENG3"},
                        "INST1": {"naziv": "instalacije 1", "ocena": 10, "sifra": "INST1"},
                        "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 8, "sifra": "OGPPK"}
                        }
    }
,

"2010/100": {
        "ime": "Milos",
        "prezime": "Milosevic",
        "indeks": "2010/100",
        "smer": "OG",
         "predmeti":
                    {
                        "MAT3": {"naziv": "matematika 3", "ocena": 5, "sifra": "MAT3"},
                        "EE": {"naziv": "elementi elektronike", "ocena": 5, "sifra": "EE"},
                        "AM": {"naziv": "asinhrone masine ", "ocena": 10, "sifra": "AM"},
                        "SM": {"naziv": "sinhrone masine", "ocena": 10, "sifra": "SM"},
                        "MAE": {"naziv": "materijali u elektrotehnici", "ocena": 8, "sifra": "MAE"},
                        "EES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 10, "sifra": "EES1"},
                        "EES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 10, "sifra": "EES2"},
                        "ENG3": {"naziv": "engleski 3", "ocena": 10, "sifra": "ENG3"},
                        "INST1": {"naziv": "instalacije 1", "ocena": 10, "sifra": "INST1"},
                        "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 8, "sifra": "OGPPK"}
                    }
         }
,"2008/105": {
        "ime": "Marko",
        "prezime": "Petrovic",
        "indeks": "2008/105",
        "smer": "OG",
            "predmeti":
                    {
                        "MAT3": {"naziv": "matematika 3", "ocena": 5, "sifra": "MAT3"},
                        "EE": {"naziv": "elementi elektronike", "ocena": 10, "sifra": "EE"},
                        "AM": {"naziv": "asinhrone masine ", "ocena": 10, "sifra": "AM"},
                        "SM": {"naziv": "sinhrone masine", "ocena": 7, "sifra": "SM"},
                        "MAE": {"naziv": "materijali u elektrotehnici", "ocena": 10, "sifra": "MAE"},
                        "EES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 10, "sifra": "EES1"},
                        "EES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 6, "sifra": "EES2"},
                        "ENG3": {"naziv": "engleski 3", "ocena": 10, "sifra": "ENG3"},
                        "INST1": {"naziv": "instalacije 1", "ocena": 10, "sifra": "INST1"},
                        "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 5, "sifra": "OGPPK"}
                    }
        }
,"2008/300":   {
        "ime": "Pera",
        "prezime": "Peric",
        "indeks": "2008/300",
        "smer": "EE",

        "predmeti":
                        {
                            "MAT3": {"naziv": "matematika 3", "ocena": 5, "sifra": "MAT3"},
                            "EE": {"naziv": "elementi elektronike", "ocena": 10, "sifra": "EE"},
                            "AM": {"naziv": "asinhrone masine ", "ocena": 10, "sifra": "AM"},
                            "SM": {"naziv": "sinhrone masine", "ocena": 7, "sifra": "SM"},
                            "MAE": {"naziv": "materijali u elektrotehnici", "ocena": 8, "sifra": "MAE"},
                            "EES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 10, "sifra": "EES1"},
                            "EES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 6, "sifra": "EES2"},
                            "ENG3": {"naziv": "engleski 3", "ocena": 10, "sifra": "ENG3"},
                            "INST1": {"naziv": "instalacije 1", "ocena": 10, "sifra": "INST1"},
                            "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 5, "sifra": "OGPPK"}
                        }
                }

}

#a) svi polozeni ispiti odredjenog studenta
def polozeni_ispiti_studenta(student_dict: dict = None, indeks: str = None):
    if indeks is not None:
        student = student_dict.get(indeks)
        predmeti = student.get("predmeti")
        # for key in predmeti:
        #     polozeni_ispiti.append(predmeti.get(key) if predmeti.get(key).get("ocena") > 5)
        # print(predmeti.get(key)) if predmeti.get(key).get("ocena") > 5 else ""
        polozeni_ispiti = [value for (key, value) in predmeti.items() if predmeti.get(key).get("ocena") > 5]
        return polozeni_ispiti
    else:
        #
        for key in student_dict:
            polozeni_ispiti = polozeni_ispiti_studenta(student_dict=student_dict, indeks=key)
            student_dict.get(key).update({"polozeni": polozeni_ispiti})

        return student_dict

# b) srednja ocena odredjenog studenta
def prosecna_ocena_studenta(student_dict: dict = None, indeks: str = None):
    polozeni = polozeni_ispiti_studenta(student_dict=student_dict, indeks=indeks)
    student = student_dict.get(indeks)
    sum = 0
    for el in polozeni:
        sum += el["ocena"]
    if len(polozeni) > 0:
        prosecna_ocena=round(sum / len(polozeni), 2)
    else:
        prosecna_ocena=0
        print("Nema polozenih")
    return prosecna_ocena


#c. podatke studenta/studenata sa navećom prosečnom ocenom

def ko_ima_najveci_prosek(studenti):
    najveca_prosecna_ocena=0
    najbolji_studenti=[]
    for key in studenti:
        prosecna_ocena=prosecna_ocena_studenta(studenti,key)
        if prosecna_ocena>=najveca_prosecna_ocena:
            najveca_prosecna_ocena=prosecna_ocena
            indeks_najboljeg_studenta=key
            najbolji_studenti.append(indeks_najboljeg_studenta)
    najbolji_studenti = []
    for key in studenti:
        prosecna_ocena=prosecna_ocena_studenta(studenti,key)
        if prosecna_ocena>=najveca_prosecna_ocena:
            najveca_prosecna_ocena=prosecna_ocena
            indeks_najboljeg_studenta=key
            najbolji_studenti.append(indeks_najboljeg_studenta)
    studenti_sa_najboljim_prosekom={}
    studenti_sa_najboljim_prosekom.update({prosecna_ocena:najbolji_studenti})
    return studenti_sa_najboljim_prosekom

#d) podatke studenta/studenata sa najmanje položenih ispita
def najmanje_polozenih_ispita(studenti):
    indeksi_polozenih=[]
    najmanje_polozenih=[]
    min=100000
    najmanje_polozenih_ispita={}
    for key in studenti:
        broj_polozenih=len(polozeni_ispiti_studenta(studenti,key))
        najmanje_polozenih.append(broj_polozenih)
        indeksi_polozenih.append(key)
    for i in range(len(indeksi_polozenih)):
        if najmanje_polozenih[i]<=min:
            min=najmanje_polozenih[i]
    for i in range(len(indeksi_polozenih)):
        if najmanje_polozenih[i]==min:
            najmanje_polozenih_ispita.update({indeksi_polozenih[i]:min})
    return najmanje_polozenih_ispita

# e)sve studente koji su položili sve ispite na predmetima koji su im dodeljeni
def svi_studenti_koji_su_ocistili_godinu(stud_dict):
    novi_stud_dict = polozeni_ispiti_studenta(student_dict=stud_dict)
    s=0
    for key in novi_stud_dict:
        if len(novi_stud_dict.get(key)["predmeti"]) == len(novi_stud_dict.get(key)["polozeni"]):
            print("student ", novi_stud_dict.get(key)["ime"], "je polozio sve predmete!")
        else:
            s+=1
    if s==len(studenti):
        print("nema niceg")

def raspodela_studenata_po_smerovima(studenti):
    a=[]
    b=[]
    raspodela={}
    for key in studenti:
        student=studenti.get(key)
        a.append(student.get("smer"))
        b.append(student.get("indeks"))
        for i in range(len(a)):
            s=0
            for j in range(len(a)):
                if a[j]==a[i]:
                    s+=1
            procenat=100 * s / len(a)
            str_procenat=str(procenat)
            raspodela.update({"Na smeru "+a[i]+" ima":str_procenat+"%"})
    return raspodela

def raspodela_po_smerovima(studenti):
    svi_smerovi={}
    raspodela_po_smerovima={}
    for key in studenti:
        student = studenti.get(key)
        for smer in student:
            smer=student.get("smer")
            svi_smerovi.update({smer:None})
    for smerovi in svi_smerovi:
        studenti_na_istom_smeru = []
        for key in studenti:
            student = studenti.get(key)
            smer=student.get("smer")
            if smer==smerovi:
                studenti_na_istom_smeru.append(student)
                raspodela_po_smerovima.update({smer:studenti_na_istom_smeru})
    return raspodela_po_smerovima
#f) raspodelu studenata po smerovima, u procentima
def raspodela_po_smerovima_procenti(studenti):
    raspodela_po_smerovima_procenti = {}
    raspodela_po_smerovima_1=raspodela_po_smerovima(studenti)
    for key in raspodela_po_smerovima_1:
        procenat = str(100 * len(raspodela_po_smerovima_1.get(key)) / len(studenti))
        raspodela_po_smerovima_procenti.update({key: procenat + "%"})
    return raspodela_po_smerovima_procenti
#g) sve studente na odabranom smeru
def svi_studenti_na_odabranom_smeru(studenti,odabrani_smer):
    s=0
    raspodela_po_smerovima_1=raspodela_po_smerovima(studenti)
    for smer in raspodela_po_smerovima_1:
        if odabrani_smer==smer:
            svi_studenti_na_odabranom_smeru=raspodela_po_smerovima_1.get(smer)
        else:
            s+=1
    if s==len(raspodela_po_smerovima_1):
        print("Nema studenata na odabranom smeru")
        svi_studenti_na_odabranom_smeru={}
    return svi_studenti_na_odabranom_smeru

#h) najboljeg studenta na odabranom smeru
def ko_je_najbolji_na_smeru(studenti,odabrani_smer):
    indeksi=[]
    prosecne_ocene=[]
    for indeks in studenti:
        student=studenti.get(indeks)
        smer=student.get("smer")
        prosecna_ocena=prosecna_ocena_studenta(studenti,indeks)
        if smer==odabrani_smer:
            prosecne_ocene.append(prosecna_ocena)
            indeksi.append(indeks)
    najveca_prosecna_ocena=0
    for i in range(len(prosecne_ocene)+1):
       if prosecne_ocene[i]>najveca_prosecna_ocena:
           najveca_prosecna_ocena=prosecne_ocene[i]
           broj_indeksa_najboljeg_studenta=indeksi[i]

    for key in studenti:
        student=studenti.get(key)
        if key==broj_indeksa_najboljeg_studenta:
            print("Student ",student.get("ime"),student.get("prezime"),"sa prosecnom ocenom", najveca_prosecna_ocena)
    return broj_indeksa_najboljeg_studenta

def predmeti_i_prosecne_ocene(studenti):
    lista_predmeta=[]
    lista_ocena=[]
    for indeks in studenti:
        student=studenti.get(indeks)
        for predmeti in student:
            predmeti=student.get("predmeti")
            for predmet in predmeti:
                predmet=predmeti.get(predmet)
                naziv_predmeta=predmet.get("naziv")
                ocena_predmeta=predmet.get("ocena")
                lista_predmeta.append(naziv_predmeta)
                lista_ocena.append(ocena_predmeta)
    recnik_ocena={}
    for i in range(len(lista_predmeta)):
        recnik_ocena.update({lista_predmeta[i]:None})
    for key in recnik_ocena:
        suma_ocena=0
        broj_ocena=0
        for i in range(len(lista_predmeta)):
            if key==lista_predmeta[i]:
                broj_ocena+=1
                suma_ocena=suma_ocena+lista_ocena[i]
        prosek_ocena=suma_ocena/broj_ocena
        recnik_ocena[key]=prosek_ocena
    return recnik_ocena
#i) sve predmete koji nije položio niti jedan student
def predmeti_koje_nije_niko_polozio(studenti):
    predmeti_koje_nije_niko_polozio=[]
    recnik_ocena=predmeti_i_prosecne_ocene(studenti)
    for predmet in recnik_ocena:
        if recnik_ocena.get(predmet)<=5:
            predmeti_koje_nije_niko_polozio.append(predmet)
    print(predmeti_koje_nije_niko_polozio)
#j) predmete sa najvećom prosečnom ocenom
def predmeti_sa_najvecom_prosecnom_ocenom(studenti):
    predmeti_sa_najvecom_prosecnom_ocenom=[]
    najveca_prosecna_ocena=0
    recnik_ocena = predmeti_i_prosecne_ocene(studenti)
    for predmet in recnik_ocena:
        if recnik_ocena.get(predmet)>=najveca_prosecna_ocena:
            najveca_prosecna_ocena=recnik_ocena.get(predmet)
            predmeti_sa_najvecom_prosecnom_ocenom.append(predmet)
    predmeti_sa_najvecom_prosecnom_ocenom=[]
    for predmet in recnik_ocena:
        if recnik_ocena.get(predmet) >= najveca_prosecna_ocena:
            najveca_prosecna_ocena = recnik_ocena.get(predmet)
            predmeti_sa_najvecom_prosecnom_ocenom.append(predmet)
    return predmeti_sa_najvecom_prosecnom_ocenom
unos=""
while unos!="kraj":
    unos = input("Sta zelite da program ispise ?\n"
                 "a. sve položene ispite određenog studenta\n"
                 "b. srednju ocenu određenog studenta\n"
                 "c. podatke studenta/studenata sa navećom prosečnom ocenom\n"
                 "d. podatke studenta/studenata sa najmanje položenih ispita\n"
                 "e. sve studente koji su položili sve ispite na predmetima koji su im dodeljeni\n"
                 "f. raspodelu studenata po smerovima, u procentima\n"
                 "g. sve studente na odabranom smeru\n"
                 "h. najboljeg studenta na odabranom smeru\n"
                 "i. sve predmete koji nije položio niti jedan student\n"
                 "j. predmete sa najvećom prosečnom ocenom\n")

    if unos == "a":
        broj_indeksa = input("Unesite broj indeksa:\n")
        print(polozeni_ispiti_studenta(studenti, broj_indeksa))

    else:
        if unos == "b":
            broj_indeksa = input("Unesite broj indeksa:\n")
            print(prosecna_ocena_studenta(studenti, broj_indeksa))
        else:
            if unos == "c":
                print(ko_ima_najveci_prosek(studenti))
            else:
                if unos == "d":
                    print(najmanje_polozenih_ispita(studenti))
                else:
                    if unos == "e":
                        print(svi_studenti_koji_su_ocistili_godinu(studenti))
                    else:
                        if unos == "f":
                            print(raspodela_po_smerovima_procenti(studenti))
                        else:
                            if unos == "g":
                                odabrani_smer=input("Unesite smer")
                                print(svi_studenti_na_odabranom_smeru(studenti,odabrani_smer))
                            else:
                                if unos == "h":
                                    odabrani_smer = input("Unesite smer")
                                    print(ko_je_najbolji_na_smeru(studenti,odabrani_smer))
                                else:
                                    if unos == "i":
                                        print(predmeti_koje_nije_niko_polozio(studenti))
                                    else:
                                        if unos == "j":
                                            print(predmeti_sa_najvecom_prosecnom_ocenom(studenti))
                                        else:
                                            if unos!="kraj":
                                                print("Pogresan unos")