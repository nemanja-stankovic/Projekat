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
        {
        "ime": "Marko",
        "prezime": "Petrovic",
        "indeks": "2008/105",
        "smer": "OG",
        "predmeti": {
            "OGMAT3": {"naziv": "matematika 3", "ocena": 10},
            "OGEE": {"naziv": "elementi elektronike", "ocena": 9},
            "OGAM": {"naziv": "asinhrone masine ", "ocena": 8},
            "OGSM": {"naziv": " sinhrone masine", "ocena": 10},
            "OGMAE": {"naziv": "materijali u elektrotehnici", "ocena": 10},
            "OGAEES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 8},
            "OGAEES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 8},
            "OGENG3": {"naziv": "engleski 3", "ocena": 10},
            "OGINST1": {"naziv": "instalacije 1", "ocena": 8},
            "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 10}
                    }
        }

    ,
        {
        "ime": "Nemanja",
        "prezime": "Stankovic",
        "indeks": "2008/205",
        "smer": "OG",
        "predmeti": {
            "OGMAT3": {"naziv": "matematika 3", "ocena": 7},
            "OGEE": {"naziv": "elementi elektronike", "ocena": 5},
            "OGAM": {"naziv": "asinhrone masine ", "ocena": 10},
            "OGSM": {"naziv": " sinhrone masine", "ocena": 8},
            "OGMAE": {"naziv": "materijali u elektrotehnici", "ocena": 10},
            "OGAEES1": {"naziv": "analiza elektroenergetskih sistema 1", "ocena": 7},
            "OGAEES2": {"naziv": "analiza elektroenergetskih sistema 2", "ocena": 5},
            "OGENG3": {"naziv": "engleski 3", "ocena": 10},
            "OGINST1": {"naziv": "instalacije 1", "ocena": 7},
            "OGPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 9}
        }
    },
     {
        "ime": "Marija",
        "prezime": "Markovic",
        "indeks": "2008/205",
        "smer": "EE",
        "predmeti": {
            "EEMAT3": {"naziv": "matematika 3", "ocena": 10},
            "EEOE": {"naziv": "osnove elektronike", "ocena": 10},
            "EETK": {"naziv": "telekomunikacije ", "ocena": 10},
            "EEF1": {"naziv": " fizika1", "ocena": 10},
            "EEMAE": {"naziv": "materijali u elektronici", "ocena": 10},
            "EEAEK1": {"naziv": "analiza elektricnih kola 1", "ocena": 10},
            "EEAEK2": {"naziv": "analiza elektricnih kola 2", "ocena": 10},
            "EEENG3": {"naziv": "engleski 3", "ocena": 10},
            "EEINST1": {"naziv": "instalacije 1", "ocena": 10},
            "EEPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 10}
        }
    },
     {
        "ime": "Petar",
        "prezime": "Petrovic",
        "indeks": "2008/307",
        "smer": "TK",
        "predmeti": {
            "TKMAT3": {"naziv": "matematika 3", "ocena": 6},
            "TKOE": {"naziv": "osnove elektronike", "ocena": 6},
            "TKTK": {"naziv": "telekomunikacije ", "ocena": 7},
            "TKF1": {"naziv": " fizika1", "ocena": 8},
            "TKMAE": {"naziv": "materijali u elektronici", "ocena": 6},
            "TKAEK1": {"naziv": "analiza elektricnih kola 1", "ocena": 6},
            "TKAEK2": {"naziv": "analiza elektricnih kola 2", "ocena": 5},
            "TKENG3": {"naziv": "engleski 3", "ocena": 7},
            "TKINST1": {"naziv": "instalacije 1", "ocena": 6},
            "TKPPK": {"naziv": "praktikum iz koriscenja racunara", "ocena": 8}
        }
    }
}


def polozeni_predmeti_studenta(studenti, student_indeks):
    student = studenti.get(str(student_indeks))
    predmeti = student.get("predmeti").values()
    polozeni = []
    for predmet in predmeti:
        if int(predmet.get("ocena")) > 5:
            polozeni.append(predmet.get("naziv"))
    return polozeni

def srednja_ocena_studenta(studenti, student_indeks):
    student = studenti.get(str(student_indeks))
    predmeti = student.get("predmeti").values()
    polozeni = []
    broj_polozenih = 0
    zbir_ocena = 0
    for predmet in predmeti:
        if int(predmet.get("ocena")) > 5:
            broj_polozenih += 1
            zbir_ocena = zbir_ocena + int(predmet.get("ocena"))
    srednja_ocena = round(zbir_ocena / broj_polozenih, 2)
    return srednja_ocena

def ko_ima_najveci_prosek(studenti):
    brojevi_indeksa = studenti.keys()
    najveca_prosecna_ocena = 0
    for broj_indeksa in brojevi_indeksa:
        if (srednja_ocena_studenta(studenti, broj_indeksa)) > najveca_prosecna_ocena:
            najveca_prosecna_ocena = srednja_ocena_studenta(studenti, broj_indeksa)
            broj_indeksa_najboljeg = broj_indeksa
    student = studenti.get(str(broj_indeksa_najboljeg))
    return student

def ko_je_polozio_najmanje_ispita(studenti):
    student = studenti.get(str(student_indeks))
    predmeti = student.get("predmeti").values()

    broj_najmanje_polozenih = 0
    indeksi_najgorih_studenata = []
    najgori_student = {}

    for student in studenti:
        student_tekuci = studenti.get(str(student_indeks))
        predmeti = student_tekuci.get("predmeti").values()
        polozeni = []
        broj_polozenih = 0
        for predmet in predmeti:
            if int(predmet.get("ocena")) > 5:
                broj_polozenih += 1
        if broj_najmanje_polozenih >= broj_polozenih:
            broj_najmanje_polozenih = broj_polozenih
            najgori_student.update(student)
    return najgori_student

# print(ko_je_polozio_najmanje_ispita(studenti))

ko_ima_najveci_prosek(studenti)
print(polozeni_predmeti_studenta(studenti, "2008/205"))
srednja_ocena_studenta(studenti, "2008/205")

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

while unos!="kraj":
    if unos == "a":
        broj_indeksa = input("Unesite broj indeksa:\n")
        print(polozeni_predmeti_studenta(studenti, broj_indeksa))
    else:
        if unos == "b":
            broj_indeksa = input("Unesite broj indeksa:\n")
            print(srednja_ocena_studenta(studenti, broj_indeksa))
        else:
            if unos == "c":
                print(ko_ima_najveci_prosek(studenti))
            else:
                break