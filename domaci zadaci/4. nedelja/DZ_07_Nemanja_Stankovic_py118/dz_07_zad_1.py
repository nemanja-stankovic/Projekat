# 1.Ucitati knjigu “20000 leagues-under-Jules-Verne.txt” iz fajla.
# Knjiga se sastoji od CHAPTER-a.
# Za svaki CHAPTER napraviti posleban folder CHAPTER_broj_chaptera.
# U svakom folderu CHAPTER_broj_chaptera dodati fajl koji ce sadrzati text iz samo tog CHAPTERA. Fajl nazvati po prvoj recenici nakon CHAPTER reda.
# Dodatno uz taj fajl napraviti i fajl Analytics_CHAPTER_broj_chaptera.txt unutar foldera.
# Analytics file treba da sadrzi u sebi upisan dictionary koji ce sadrzati frekvenciju pojavljivanja svake reci u tom CHAPTERU (frekvencija je broj pojavljivanja te reci/ukupan broj reci).
# Program podeliti u funkcije. Za svaku funkciju pisati obradu izuzetaka koji mogu da se jave.
# Na kraju u posebnom folderu koji ce se zvati all_analytics napraviti fajl all_analytics.txt koji ce sadrzati po opadajucem redosledu broju reci koji sadrzi CHAPTER. Upisati u svaki red samo CHAPTER_broj_chaptera : Broj_reci.
# Dodatni zadatak - Bonus:
# Naci sve prefix duzine (duzina prefixa), i to upisati u dodatni fajl u svakom CHAPTERU pod prefix_CHAPTER_broj_chaptera.
#
# Primer:
# 	Doktor
# 	Dok
#
# {“Dok”:(“Dok”,”Doktor”)}
import os

def make_chapters(data: str) -> list:                   # funkcija od datog teksta pravi listu tekstova,
    try:                                                # gde je svaki tekst posebno poglavlje
        if "CHAPTER" in data:
            poglavlja=data.split("CHAPTER")
            poglavlja_s=[]
            for element in poglavlja:
                element_1 = "CHAPTER" + element
                if element!="":
                    poglavlja_s.append(element_1)
            return poglavlja_s
        else:
            return []
    except AttributeError:
        print("Greska prilikom pozivanja funkcije make_chapters, argument mora biti tipa string")
    except TypeError:
        print("Greska prilikom pozivanja funkcije make_chapters, argument mora biti tipa string")
    except Exception as e:
        print(e)

def make_chapter_titles(chapter: list) -> list:         # funkcija od date liste tekstova izdvaja
    try:                                                 # listu naslovnih recenica
        naslovne_recenice=[]
        for element in chapter:
            brojac=0
            pocetak=0
            kraj=0
            for i in range(len(element)):
                if element[i]=="." and brojac<3:
                    brojac+=1
                    if brojac==1:
                        pocetak=i+1
                    else:
                        if brojac==2:
                            kraj=i+1
            recenica=element[pocetak:kraj]
            recenica=recenica.lstrip()
            naslovne_recenice.append(recenica)
        return naslovne_recenice
    except TypeError:
        print("Greska prilikom pozivanja funkcije make_chapter_titles, argument mora biti lista stringova")
    except Exception as e:
        print(e)

def list_of_words(data: str) -> list:                   # funkcija od datog teksta vraca listu reci
    try:
        lista_reci = data.split()
        lista_reci_clear = []
        for i in range(len(lista_reci)):
            rec = ""
            for j in range(len(lista_reci[i])):
                if lista_reci[i][j].isalpha() or lista_reci[i][j].isnumeric() or lista_reci[i][j] == "-":
                    rec = rec + lista_reci[i][j].lower()
            lista_reci_clear.append(rec)
        return lista_reci_clear
    except TypeError:
        print("Greska prilikom pozivanja funkcije make_chapter_titles, argument mora biti string")
    except Exception as e:
        print(e)

def frequency_words(lista_reci: list) -> dict:          # funkcija od date liste reci pravi dictionary
    try:                                                # gde je kljuc rec, a vrednost ucestalost pojavljivanja
        dict = {}                                       # te reci u tekstu
        for i in range(len(lista_reci)):
            brojac=0
            for j in range(len(lista_reci)):
                if lista_reci[i]==lista_reci[j]:
                    brojac+=1
            dict[lista_reci[i]]=brojac/len(lista_reci)
        return dict
    except TypeError:
        print("Greska prilikom pozivanja funkcije frequency_words, argument mora biti lista stringova")
    except Exception as e:
        print(e)

def sortiraj_dve_liste_prema_prvoj(brojevi_reci: list, brojevi_chaptera: list) -> tuple:      # funkcija od dve prosledjene liste sortira prvu
    try:
        for i in range(len(brojevi_reci)):                                          # prema opadajucem redosledu a zatim drugu prema prvoj
            for j in range(len(brojevi_reci)):                                      # na kraju vraca tuple dve sortirane liste
                if brojevi_reci[j] > brojevi_reci[i] and j > i:
                    pom = brojevi_reci[i]
                    brojevi_reci[i] = brojevi_reci[j]
                    brojevi_reci[j] = pom
                    pom2 = brojevi_chaptera[i]
                    brojevi_chaptera[i] = brojevi_chaptera[j]
                    brojevi_chaptera[j] = pom2
        izlaz= (brojevi_reci, brojevi_chaptera)
        return izlaz
    except TypeError:
        print("Greska prilikom pozivanja funkcije sortiraj_dve_liste_prema_prvoj, argumenti moraju biti dve liste brojeva")
    except Exception as e:
        print(e)

with open("20000 leagues-under-Jules-Verne-[ebooksread.com].txt","r") as f:
    data=f.read()
lista_reci=list_of_words(data)
poglavlja_s=make_chapters(data)
naslovne_recenice=make_chapter_titles(poglavlja_s)

try:
    parent_path=os.getcwd()                                                          # pravljenje foldera deo I
    path=os.path.join(parent_path,"DEO I")
    if os.path.exists(path)==False:
        os.mkdir(path)
except Exception as e:
    print(f"Greska prilikom kreiranja foldera DEO I{e}")
try:
    parent_path_deo_1 = path
    for i in range(23):
        CHAPTER="CHAPTER_"+str(i+1)                                                 # pravljenje 23 foldera CHAPTER
        path=os.path.join(parent_path_deo_1,CHAPTER)
        if os.path.exists(path) == False:
            os.mkdir(path)
except Exception as e:
    print(f"Greska prilikom kreiranja 23 CHAPTER foldera DEO I {e}")

try:
    naslov=naslovne_recenice[i]+"txt"                                              # pravljenje 23 text fajla u deo I
    parent_path=path
    path=os.path.join(parent_path,naslov)
    naslov_analytics="analytics_"+str(i+1)+".txt"
    path_analytics=os.path.join(parent_path,naslov_analytics)
    with open(path, "w") as f:
        data=poglavlja_s[i]
        f.write(data)
    with open(path_analytics, "w") as f:
        data=poglavlja_s[i]
        lista_reci=list_of_words(data)
        data_analytics=frequency_words(lista_reci)
        f.write(str(data_analytics))
except Exception as e:
    print(f"Greska prilikom kreiranja 23 text fajla deo I {e}")

try:
    parent_path=os.getcwd()                                                         # pravljenje foldera deo II
    path=os.path.join(parent_path,"DEO II")
    if os.path.exists(path) == False:
        os.mkdir(path)
    parent_path_deo_2 = path
except Exception as e:
    print(f"Greska prilikom kreiranja 23 CHAPTER foldera DEO II {e}")

try:
    for i in range(23):
        CHAPTER="CHAPTER_"+str(i+1)                                                # pravljenje 23 foldera CHAPTER u deo II
        path=os.path.join(parent_path_deo_2,CHAPTER)
        if os.path.exists(path) == False:
            os.mkdir(path)
        naslov=naslovne_recenice[i+23]+"txt"
except Exception as e:
    print(f"Greska prilikom kreiranja 23 CHAPTER foldera DEO II {e}")

try:
    parent_path=path                                                           # pravljenje 23 text fajla u deo II
    path=os.path.join(parent_path,naslov)
    naslov_analytics="analytics_"+str(i+1)+".txt"
    path_analytics=os.path.join(parent_path,naslov_analytics)
    with open(path, "w") as f:
        data=poglavlja_s[i+23]
        f.write(data)
    with open(path_analytics, "w") as f:
        data = poglavlja_s[i]
        lista_reci=list_of_words(data)
        data_analytics=frequency_words(lista_reci)
        f.write(str(data_analytics))
except Exception as e:
    print(f"Greska prilikom kreiranja 23 text fajla deo II {e}")
try:
    parent_path=os.getcwd()                                                          # pravljenje all analytics foldera
    path=os.path.join(parent_path,"ALL ANALYTICS")
    if os.path.exists(path) == False:
        os.mkdir(path)
    parent_path=path
    path=os.path.join(parent_path,"all analytics.txt")
    str_all_analytics=""
    brojevi_reci_deo_1 = []
    brojevi_chaptera_deo_1 = []
    brojevi_reci_deo_2 = []
    brojevi_chaptera_deo_2 = []
    for i in range(23):
        data = poglavlja_s[i]
        broj_reci = len(list_of_words(data))
        broj_chaptera=i+1
        brojevi_reci_deo_1.append(broj_reci)
        brojevi_chaptera_deo_1.append(broj_chaptera)
    for i in range(23,46):
        data = poglavlja_s[i]
        broj_reci = len(list_of_words(data))
        broj_chaptera=i-22
        brojevi_reci_deo_2.append(broj_reci)
        brojevi_chaptera_deo_2.append(broj_chaptera)
except Exception as e:
    print(f"Greska prilikom kreiranja allanalytics foldera {e}")
try:                                                                    # pravljenje all analytics text fajla
    brojevi_chaptera=[]
    brojevi_reci=[]
    for i in range(len(brojevi_chaptera_deo_1)):
        broj_chaptera_deo_1="DEO_1_CHAPTER_"+str(brojevi_chaptera_deo_1[i])
        brojevi_chaptera.append(broj_chaptera_deo_1)
        brojevi_reci.append(brojevi_reci_deo_1[i])
    for i in range(len(brojevi_chaptera_deo_2)):
        broj_chaptera_deo_2="DEO_2_CHAPTER_"+str(brojevi_chaptera_deo_2[i])
        brojevi_chaptera.append(broj_chaptera_deo_2)
        brojevi_reci.append(brojevi_reci_deo_2[i])

    brojevi_reci_i_brojevi_chaptera=sortiraj_dve_liste_prema_prvoj(brojevi_reci,brojevi_chaptera)

    for i in range(len(brojevi_chaptera)):
        str_red=brojevi_chaptera[i]+": "+str(brojevi_reci[i])+"\n"
        str_all_analytics=str_all_analytics+str_red

    with open(path, "w") as f:
        data = str_all_analytics
        f.write(data)
except Exception as e:
    print(f"Greska prilikom kreiranja allanalytics text fajla {e}")



