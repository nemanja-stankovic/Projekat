"""DISCLAIMER - NE KORISTITI PRAVI RAD SA FAJLOVIMA, modelujemo nase imaginarne fajlove.
Modelovati interfejs za primitivan fajl sistem. Fajl sistem cemo modelovati bez direktorijuma,
dakle nas fajl sistem ima samo fajlove, datoteke. Fajlovi mogu biti razlicitog tipa, ali dele skup funkcionalnosti
- svaki fajl ima naziv, tip (ekstenziju), velicinu, opis, trenutak (moze datum i vreme, moze samo datum, moze samo vreme,
moze timestamp, moze samo neki arbitrarni broj - stagod hocete) poslednje modifikacije, i neki sadrzaj (dummy sadrzaj,
sadrzaj svih fajlova moze biti modelovan prostim stringom za potrebe ovog zadatka - NE RADITI SA PRAVIM FAJLOVIMA) .
Svi fajlovi se mogu procitati i u sve fajlove se moze upisati (read, write). Pri citanju iscitava se sadrzaj,
pri upisu sadrzaj se menja, a menja se i trenutak poslednje modifikacije fajla
(i ukoliko je potrebno jos nekih atributa datog fajla, zavisno od tipa).
Od mogucih fajlova imamo:
1. Tekstualne tipa .txt koji pored gorenavedenih atributa imaju jos i broj karaktera u njima;
2. Slike tipa .img koji imaju dimenzije sllike;
3. Video fajlove tipa .mp4 koji imaju dimenziju slike i trajanje.
U mainu napraviti bar po jedan fajl svakog tipa, i pozvati/iskoristiti svaku od njihovih metoda.
Cilj je dakle da imamo jasnu, cistu hijerarhiju klasa, a ne da unosimo kompleksnost radeci sa pravim fajlovima.
Tako da obratite paznju molim vas, ko koga nasledjuje i to ce biti dovoljno da utvrdimo nasledjivanje kao koncept.
Nikakva logicka kompleksnost ne postoji u ovom zadatku."""


from file import File
from txt_file import FileTxt
from img_file import FileImg
from mp4_file import FileMp4

def main():

    file_primer=File("nemanja",12,"opis","nesto","vreme","txt")
    print(file_primer)
    file_primer.write("nesto")
    print(file_primer)
    text=FileTxt("nemanja",2,"opis","neki sadrzaj","date","txt",12)
    print(text.number_of_chars)
    image=FileImg("nemanja",120,"opis","neki sadrzaj","date","img","720x1280")
    print(image)
    video=FileMp4("Avatar_preview", 7560, "film", "sadrzaj","date", "mp4","720x1280","12s")
    print(video)
    video.write(" dodatni sadrzaj")
    print(video)
    print(video.read())

if __name__ == '__main__':
    main()

