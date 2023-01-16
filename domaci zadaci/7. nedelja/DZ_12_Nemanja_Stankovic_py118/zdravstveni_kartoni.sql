DROP DATABASE IF EXISTS zdravstveni_kartoni;
CREATE DATABASE IF NOT EXISTS zdravstveni_kartoni;
USE zdravstveni_kartoni;

CREATE TABLE IF NOT EXISTS pacijent (
ime VARCHAR(90),
prezime  VARCHAR(90),
JMBG VARCHAR(90),
adresa  VARCHAR(150),
telefon VARCHAR(20),
br_licence_doktora VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS doktor (
ime VARCHAR(90),
prezime  VARCHAR(90),
JMBG VARCHAR(90),
specijalizacija  VARCHAR(150),
broj_licence VARCHAR(20)
);


CREATE TABLE IF NOT EXISTS medikament (
naziv VARCHAR(90),
sifra  VARCHAR(90),
naziv_proizvodjaca VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS bolest (
naziv_bolesti VARCHAR(90),
opis VARCHAR(90),
slika BLOB
);

CREATE TABLE IF NOT EXISTS proizvodjac (
naziv VARCHAR(90),
adresa  VARCHAR(90),
telefon VARCHAR(90)
);

CREATE TABLE IF NOT EXISTS boluje_od (
ime_pacijenta VARCHAR(90),
ime_doktora  VARCHAR(90),
naziv_bolesti VARCHAR(90),
datum_diojagnoze DATETIME
);

ALTER TABLE pacijent
ADD PRIMARY KEY (JMBG);

ALTER TABLE doktor
ADD PRIMARY KEY (broj_licence);

ALTER TABLE medikament
ADD PRIMARY KEY (sifra);

ALTER TABLE bolest
ADD PRIMARY KEY (naziv_bolesti);

ALTER TABLE proizvodjac
ADD PRIMARY KEY (naziv);

ALTER TABLE boluje_od
ADD PRIMARY KEY (ime_pacijenta);

ALTER TABLE bolest
ADD COLUMN id_bolesti INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_bolesti) ;

ALTER TABLE proizvodjac
ADD COLUMN id_proizvodjac INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_proizvodjac) ;

ALTER TABLE boluje_od
ADD COLUMN id_boluje_od INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY, ADD PRIMARY KEY (id_boluje_od) ;

ALTER TABLE pacijent
ADD CONSTRAINT fk_doktor_1 FOREIGN KEY (br_licence_doktora) REFERENCES doktor(broj_licence) ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE medikament
ADD CONSTRAINT fk_proizvodjac_1 FOREIGN KEY (naziv_proizvodjaca) REFERENCES proizvodjac(naziv_proizvodjaca) ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE boluje_od
ADD CONSTRAINT fk_pacijent_1 FOREIGN KEY (ime_pacijenta) REFERENCES pacijent(ime) ON UPDATE NO ACTION ON DELETE NO ACTION,
ADD CONSTRAINT fk_doktor_2 FOREIGN KEY (ime_doktora) REFERENCES doktor(ime) ON UPDATE NO ACTION ON DELETE NO ACTION,
ADD CONSTRAINT bolest_1 FOREIGN KEY (naziv_bolesti) REFERENCES bolest(naziv_bolesti) ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE bolest
DROP COLUMN slika;

CREATE TABLE IF NOT EXISTS recept(
id_recepta INT PRIMARY KEY AUTO_INCREMENT,
naziv_medikamenta VARCHAR(90),
sifra_medikamenta VARCHAR(90),
ime_doktora VARCHAR(90),
CONSTRAINT fk_medikament_1 FOREIGN KEY (naziv_medikamenta) REFERENCES medikament(naziv) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_medikament_2 FOREIGN KEY (sifra_medikamenta) REFERENCES medikament(sifra) ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_doktor_3 FOREIGN KEY (ime_doktora) REFERENCES doktor(ime) ON UPDATE NO ACTION ON DELETE NO ACTION
);

INSERT INTO doktor (ime,prezime,JMBG,specijalizacija, broj_licence) VALUES ('Nemanja','Stankovic','0705989710080','hirurg', '545545');
INSERT INTO pacijent (ime,prezime,JMBG,adresa, telefon, br_licence_doktora) VALUES ('Petar','Petrovic','8956489710080','Nepoznata','045462368','545545');
