# Napisati program za igranje kviza “Želite li da postanete milioner?
# a. Napisati funkciju za unos podataka igraca
# b. Napisati funkciju koja ce na osnovu broja pitanja iz liste pitanja (postoji jedinstvena lista za
# pitanja od 1-5 (laksa), 6-10(srednja) i 11-15(teska)) random postaviti pitanje i odgovore igracu.
# Nije dozvoljeno jednom igracu postaviti ista pitanja.
# c. Napisati funkciju za pomoc pola pola
# d. Napisati funkciju za pomoc zamena pitanja (nije dozvoljeno postaviti isto pitanje)
# e. Napisati funkciju za pomoc pitaj publiku (Sto je teze pitanje, manja je sansa da publika da
# tacan odgovor, svaki odgovor ima procentualno koliko je publike glasalo da je to tacan
# odgovor)
# f. Napisati funkciju za davanje odgovora (a, b, c, d, ODUSTAJEM)
# g. Napisati funkciju koja ce na osnovu datog odgovora odrediti da li se igracu postavlja sledece
# pitanje, ili se vraca na zagarantovanu sumu (5. pitanje, 10. pitanje)
# h. Napisati funkciju koja ce na kraju igre prikazati koliko je novca osvojio takmicar
import random

laka_pitanja = [ {
        "pitanje": "Bacanjem pljosnatih kamencica u vodu pravimo...?",
        "odgovori":[
            {"tekst":"babice", "tacan": False},
            {"tekst":"buku", "tacan": False},
            {"tekst":"tarabice", "tacan": False},
            {"tekst":"zabice", "tacan": True}
                    ]
                },
                {
        "pitanje": "Ko rano rani...?",
        "odgovori":[
            {"tekst":"ceo dan zeva", "tacan": False},
            {"tekst":"dve srece grabi", "tacan": True},
            {"tekst":"ima da radi domaci", "tacan": False},
            {"tekst":"naspavao se na vreme", "tacan": False}
                    ]
},
    {
        "pitanje": "Ko je rekao Ipak se okrece?",
        "odgovori":[
            {"tekst":"Galileo Galilej", "tacan": True},
            {"tekst":"Aca Lukas", "tacan": False},
            {"tekst":"prase na raznju", "tacan": False},
            {"tekst":"niko", "tacan": False}
    ]
    }
        ]


srednja_pitanja = [
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},

]

teska_pitanja = [
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},

]

pitanja = {"laka": laka_pitanja, "srednja": srednja_pitanja, "teska": teska_pitanja}

takmicar = {
    "ime": "",
    "prezime": "",
    "trenutno_pitanje": 1,
    "osvojeni_novac": 0,
    "Zagarantovana_suma": 0,
    "pola_pola": False,
    "zamena_pitanja": False,
    "pitaj_publiku": False,
}

vrednost_pitanja = {
    "1": {"v": 1000, "zagarantovano": False},
    "2": {"v": 2000, "zagarantovano": False},
    "3": {"v": 3000, "zagarantovano": False},
    "4": {"v": 4000, "zagarantovano": False},
    "5": {"v": 5000, "zagarantovano": True},
    "6": {"v": 10000, "zagarantovano": False},
    "7": {"v": 20000, "zagarantovano": False},
    "8": {"v": 40000, "zagarantovano": False},
    "9": {"v": 80000, "zagarantovano": False},
    "10": {"v":160000, "zagarantovano": True},
    "11": {"v":320000, "zagarantovano": False},
    "12": {"v":640000, "zagarantovano": False},
    "13": {"v":1250000, "zagarantovano": False},
    "14": {"v":2500000, "zagarantovano": False},
    "15": {"v":5000000, "zagarantovano": False}
}


def unos_igraca():  # A)Napisati funkciju za unos podataka igraca
    takmicar["ime"] = input("Unesite ime igraca:")
    takmicar["prezime"] = input("Unesite prezime igraca:")

# b. Napisati funkciju koja ce na osnovu broja pitanja iz liste pitanja (postoji jedinstvena lista za
# pitanja od 1-5 (laksa), 6-10(srednja) i 11-15(teska)) random postaviti pitanje i odgovore igracu.

def izvuci_pitanje(data: dict, tezina: str = "laka"):
    lista = ["a", "b", "c", "d"]
    random.shuffle(data.get(tezina))
    pitanje = data.get(tezina).pop()
    random.shuffle(pitanje.get("odgovori"))
    for index, item in enumerate(pitanje.get("odgovori")):
        item["pozicija"] = lista[index]
    print(pitanje.get("pitanje"))
    odgovori=pitanje.get("odgovori")
    for odgovor in odgovori:
        print(odgovor.get("pozicija"),".",odgovor.get("tekst"))
    return pitanje


def postavi_pitanje(pitanja: dict, n_pitanja):
    if 0 < n_pitanja < 6:
        question = izvuci_pitanje(pitanja, "laka")
    elif 5 < n_pitanja < 11:
        question = izvuci_pitanje(pitanja, "srednja")
    else:
        question = izvuci_pitanje(pitanja, "teska")
    return question


def pomozi_pola_pola(data_user: dict, pitanja: dict, question:dict):
    tekst_pitanja = question["pitanje"]
    if not data_user["pola_pola"]:
        brojac = 0
        while brojac < 3:
            for item in question["odgovori"]:
                if not item["tacno"]:
                    question["odgovori"].remove(item)
                    brojac += 1
    else:
        print("Iskoristili ste pomoc.")
    data_user["pola-pola"] = True
    print(tekst_pitanja)
    for item in question:
        item=question.get("odgovori")
        for odgovori in item:
            print(odgovori["pozicija"], ".", odgovori["tekst"])


# d. Napisati funkciju za pomoc zamena pitanja (nije dozvoljeno postaviti isto pitanje)
def zameni_pitanje(data_user, pozicija, postavljeno_pitanje):
    if not data_user["zamena_pitanja"]:
        print(postavi_pitanje(pitanja,3))
    data_user["zamena_pitanja"] = True


# def pomoc_publike(data_user, pitanja, postavljeno_pitanje):
#     if not data_user["pitaj_publiku"]:




# f. Napisati funkciju za davanje odgovora (a, b, c, d, ODUSTAJEM)
def daj_opciju(postavljeno_pitanje, data_user:dict):
    opcija = input("Unesite a, b, c, d ili odustajem")

    odgovori=postavljeno_pitanje.get("odgovori")
    for odgovor in odgovori:
        pozicija=odgovor.get("pozicija")
        if opcija == pozicija:
            if odgovor["tacan"]:
                data_user["trenutno_pitanje"] += 1
                trenutno_pitanje=int(data_user["trenutno_pitanje"])
                suma=vrednost_pitanja.get(str(trenutno_pitanje))
                data_user["osvojeni_novac"] += suma.get("v")
                if data_user["trenutno_pitanje"] > 5 and data_user["trenutno_pitanje"]<10:
                    data_user["zagarantovana_suma"] = 5000
                elif data_user["trenutno_pitanje"] > 10 and data_user["trenutno_pitanje"] < 15:
                     data_user["zagarantovana_suma"] = 160000
                # osvojeni_novac =(vrednost_pitanja.get(str(trenutno_pitanje))).get("v"))
                # print("Os")
            else:
                print("Pogrijesili ste.")
                print("Osvojili ste", takmicar.get("zagarantovana_suma"))

    return

# g. Napisati funkciju koja ce na osnovu datog odgovora odrediti da li se igracu postavlja sledece
# pitanje, ili se vraca na zagarantovanu sumu (5. pitanje, 10. pitanje)
def dalje_ide():
    unos=input(print("Trenutno osvojena suma", takmicar.get("osvojeni_novac"), "Da li zelite da nastavite ili odustajete ? ( za nastavak bilo koji taster, za odustajanje 0)"))
    if unos!=0:
        n=takmicar.get("trenutno_pitanje")//5
        postavljeno_pitanje=postavi_pitanje(pitanja,n)
        daj_opciju(postavljeno_pitanje,pitanja)
    else:
        print("Osvojili ste",takmicar.get("zagarantovana_suma"))

dalje_ide()