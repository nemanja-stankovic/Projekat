from options import *


def main_option():
    unos = ""
    while unos != "Z":
        unos = input("Pristup ustanovi\n"
                     "1 - dom zdravlja\n"
                     "2 - poliklinika\n"
                     "3 - dodatne funkcije\n").upper()
        if unos == "1":
            option_1()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u == "0":
                main_option()
            else:
                unos = "Z"
        elif unos == "2":
            option_2()
            u = input("Pritisnite bilo koji taster za povratak u prethodni meni ili Z za kraj\n").upper()
            if u == "0":
                main_option()
            else:
                unos = "Z"
        elif unos == "3":
            option_3()
            u = input("Pritisnite bilo koji taster za povratak u prethodni meni ili Z za kraj\n").upper()
            if u == "0":
                main_option()
            else:
                unos = "Z"
def option_1():
    unos = ""
    while unos != "Z":
        unos = input("Izaberite opciju\n"
                     "1 - Zakazivanje pregleda kod lekara opste prakse\n"
                     "2 - Pregled kod lekara opste prakse\n"
                     "0 - Povratak u prethodni meni\n"
                     "Z - prekid programa\n ").upper()

        if unos == "1":
            option_1_1()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"


        elif unos == "2":
            option_1_2()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"

        elif unos == "0":
            main_option()
        else:
            unos = "Z"

def option_2():
    unos = ""
    while unos != "Z":
        unos = input("Izaberite opciju\n"
                     "1 - Zakazivanje pregleda kod lekara specijaliste\n"
                     "2 - Pregled kod lekara specijaliste\n"
                     "0 - Povratak u prethodni meni\n"
                     "Z - prekid programa\n ").upper()

        if unos == "1":
            option_2_1()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"

        elif unos == "2":
            option_2_2()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"

        elif unos == "0":
            main_option()
        else:
            unos = "Z"

def option_3():
    unos = ""
    while unos != "Z":
        unos = input("Izaberite opciju\n"
                     "1 - Za polikliniku u kojoj ima najviše zaposlenih lekara\n"
                        " specijalista prikazati imena svih pacijenta kao i datume pregleda.\n"
                        " Ukoliko ima više klinika sa istim, najvećim brojem lekara specijalista\n"
                        " – prikazati podatke imena svih pacijenata i datume pregleda za svaku od tih klinika. \n"
                     
                     "2 - Prikaz lekara koji su izdali vise od 10 recepata\n"
                     "0 - Povratak u prethodni meni\n"
                     "Z - prekid programa\n ").upper()

        if unos == "1":
            option_3_1()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"

        elif unos == "2":
            option_3_2()
            u = input("Pritisnite nulu za povratak u prethodni meni ili Z za kraj\n").upper()
            if u != "Z":
                main_option()
            else:
                unos = "Z"

        elif unos == "0":
            main_option()
        else:
            unos = "Z"