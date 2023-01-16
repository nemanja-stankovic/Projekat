DROP DATABASE IF EXISTS evidencija_proizvoda;
CREATE DATABASE IF NOT EXISTS evidencija_proizvoda;
USE evidencija_proizvoda;

CREATE TABLE IF NOT EXISTS kupac (
JMBG VARCHAR(90),
ime VARCHAR(90),
prezime  VARCHAR(90),
adresa  VARCHAR(150),
tel VARCHAR(20),
naziv_mesta VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS mesto (
naziv_mesta VARCHAR(90),
zip VARCHAR(20),
zemlja VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS materijal (
naziv_materijala VARCHAR(90),
opis VARCHAR(90),
slika BLOB
);

CREATE TABLE IF NOT EXISTS proizvod (
naziv_proizvoda VARCHAR(90),
opis VARCHAR(90),
slika BLOB,
cena FLOAT
);

CREATE TABLE IF NOT EXISTS sastavnica (
naziv_proizvoda VARCHAR(90),
naziv_materijala VARCHAR(90),
kolicina INT
);

CREATE TABLE IF NOT EXISTS kupovina_proizvoda (
naziv_proizvoda VARCHAR(90),
naziv_mesta VARCHAR(90),
ime_kupca VARCHAR(90),
kolicina INT,
ukupna_cena FLOAT,
datum DATETIME
);

ALTER TABLE kupac
ADD PRIMARY KEY (JMBG);

ALTER TABLE mesto
ADD PRIMARY KEY (zip);

ALTER TABLE materijal
ADD PRIMARY KEY (naziv_materijala);

ALTER TABLE proizvod
ADD PRIMARY KEY (naziv_proizvoda);

ALTER TABLE sastavnica
ADD PRIMARY KEY (naziv_proizvoda);

ALTER TABLE kupovina_proizvoda
ADD PRIMARY KEY (naziv_proizvoda);


ALTER TABLE kupac
ADD COLUMN id_kupac INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_kupac) ;


ALTER TABLE mesto
ADD COLUMN id_mesto INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_mesto) ;

ALTER TABLE materijal
ADD COLUMN id_materijal INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_materijal) ;


ALTER TABLE proizvod
ADD COLUMN id_proizvod INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_proizvod) ;

ALTER TABLE sastavnica
ADD COLUMN id_sastavnica INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_sastavnica) ;


ALTER TABLE kupovina_proizvoda
ADD COLUMN id_kupovina_proizvoda INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_kupovina_proizvoda) ;


ALTER TABLE sastavnica
ADD CONSTRAINT fk_proizvod_1 FOREIGN KEY (naziv_proizvoda) REFERENCES proizvod(naziv_proizvoda) ON UPDATE NO ACTION ON DELETE NO ACTION,
ADD CONSTRAINT fk_materijal_1 FOREIGN KEY (naziv_materijala) REFERENCES materijal(naziv_materijala) ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE kupovina_proizvoda
ADD CONSTRAINT fk_proizvod_2 FOREIGN KEY (naziv_proizvoda) REFERENCES proizvod(naziv_proizvoda) ON UPDATE NO ACTION ON DELETE NO ACTION,
ADD CONSTRAINT fk_mesto_1 FOREIGN KEY (naziv_mesta) REFERENCES mesto(naziv_mesta) ON UPDATE NO ACTION ON DELETE NO ACTION,
ADD CONSTRAINT fk_kupac_1 FOREIGN KEY (ime_kupca) REFERENCES kupac(ime_kupca) ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE materijal
DROP COLUMN slika;

ALTER TABLE proizvod
DROP COLUMN slika;

ALTER TABLE kupac
RENAME COLUMN tel TO telefon;

CREATE TABLE IF NOT EXISTS proizvod_na_popustu(
id_proizvoda INT PRIMARY KEY AUTO_INCREMENT,
naziv_proizvoda VARCHAR(90),
cena FLOAT,
naziv_materijala VARCHAR(90),
popust INT,
cena_sa_popustom FLOAT,
CONSTRAINT fk_proizvod_2 FOREIGN KEY (id_proizvoda) REFERENCES proizvod(id_proizvoda) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_proizvod_3 FOREIGN KEY (naziv_proizvoda) REFERENCES proizvod(naziv) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_materijal_2 FOREIGN KEY (naziv_materijala) REFERENCES materijal(naziv_materijala) ON UPDATE NO ACTION ON DELETE NO ACTION
);

INSERT INTO kupac (JMBG,ime,prezime,adresa, telefon, naziv_mesta) VALUES ('0705989710080','Nemanja','Stankovic','Niska 16b Kaludjerica','0643152368','Beograd')

