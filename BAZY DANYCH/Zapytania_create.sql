CREATE TABLE Dzialy(
    id_dzialu INT NOT NULL PRIMARY KEY,
    nazwa     VARCHAR(30) NOT NULL,
    adres     VARCHAR(30) NOT NULL
);

CREATE TABLE Stanowiska(
    nazwa     VARCHAR(30) NOT NULL PRIMARY KEY,
    placa_min MONEY,
    placa_max MONEY,
    CHECK (placa_min <= placa_max)
);

CREATE TABLE Pracownicy(
    id_prac     INT NOT NULL PRIMARY KEY,
    nazwisko    VARCHAR(30),
    stanowisko  VARCHAR(30) REFERENCES Stanowiska(nazwa),
    szef        INT REFERENCES Pracownicy(id_prac),
    zatrudniony DATETIME,
    placa_pod   MONEY,
    placa_dod   MONEY,
    id_dzialu   INT REFERENCES Dzialy(id_dzialu)
);
