import random

laka_pitanja = [
    {"pitanje": "Pitanje1",
     "odgovori": [{"tekst": "Tekst_odgovora_1", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje2",
     "odgovori": [{"tekst": "Tekst_odgovora_1", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje3",
     "odgovori": [{"tekst": "Tekst_odgovora_1", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje4",
     "odgovori": [{"tekst": "Tekst_odgovora_1", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje5",
     "odgovori": [{"tekst": "Tekst_odgovora_1", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
    {"pitanje": "Pitanje6",
     "odgovori": [{"tekst": "Tekst_odgovora_1,", "tacan": True}, {"tekst": "Tekst_odgovora_2,", "tacan": False},
                  {"tekst": "Tekst_odgovora_3,", "tacan": False}, {"tekst": "Tekst_odgovora_4,", "tacan": False}]},
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
    "2": {"v": 1000, "zagarantovano": False},
    "3": {"v": 1000, "zagarantovano": False},
    "4": {"v": 1000, "zagarantovano": False},
    "5": {"v": 1000, "zagarantovano": True},
    "6": {"v": 1000, "zagarantovano": False},
    "7": {"v": 1000, "zagarantovano": False},
    "8": {"v": 1000, "zagarantovano": False},
    "9": {"v": 1000, "zagarantovano": False},
    "10": {"v": 1000, "zagarantovano": True},
    "11": {"v": 1000, "zagarantovano": False},
    "12": {"v": 1000, "zagarantovano": False},
    "13": {"v": 1000, "zagarantovano": False},
    "14": {"v": 1000, "zagarantovano": False},
    "15": {"v": 1000, "zagarantovano": False}
}


def unos_igraca(players):  # A)Napisati funkciju za unos podataka igraca
    players["ime"] = input("Unesite ime igraca:")
    players["prezime"] = input("Unesite ime igraca:")


def izvuci_pitanje(data: dict, tezina: str = "laka"):
    lista = ["a", "b", "c", "d"]
    random.shuffle(data.get(tezina))
    pitanje = data.get(tezina).pop()
    random.shuffle(pitanje.get("odgovori"))
    for index, item in enumerate(pitanje.get("odgovori")):
        item["pozicija"] = lista[index]
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
                if not item["tacan"]:
                    question["odgovori"].remove(item)
                    brojac += 1
    else:
        print("Iskoristili ste pomoc.")

    data_user["pola-pola"] = True

    print(tekst_pitanja)
    for item in odabrano_pitanje:
        print(item["pozicija"], ".", item["tekst"])


def zameni_pitanje(data_user, pozicija, postavljeno_pitanje):
    if not data_user["zamena_pitanja"]:
        print(postavljeno_pitanje)
    data_user["zamena_pitanja"] = True


def pomoc_publike(data_user, pitanja, postavljeno_pitanje):
    if not data_user["pitaj_publiku"]:


def daj_opciju(postavljeno_pitanje, data_user:dict):
    opcija = input("Unesite a, b, c, d ili odustajem")
    for item in postavljeno_pitanje["odgovori"]:
        if opcija == item["pozicija"]:
            if item["tacan"]:
                print("Tacan odgovor")
                data_user["trenutno_pitanje"] += 1
                data_user["osvojeni_novac"] += vrednost_pitanja[data_user["trenutno_pitanje"]-1]
                if data_user["trenutno_pitanje"] // 5:
                    data_user["zagarantovana_suma"] = vrednost_pitanja[data_user["trenutno_pitanje"]]
            else:
                print("Pogrijesili ste.")




    return



print(pomozi_pola_pola(takmicar, pitanja, 3))