-- **CREAZIONE DATABASE**
CREATE DATABASE travel_danger;

-- **CREAZIONE TABELLE**

--Codice di ogni nazione
CREATE TABLE country_codes (
    code VARCHAR(2),
    countryname VARCHAR(100) NOT NULL,
    countryregion VARCHAR(50)
);

--Partenza e destinazione dei turisti
CREATE TABLE destinations (
    c_column INT NOT NULL,
    X int NOT NULL,
    passengers INT NOT NULL,
    origin_country VARCHAR(2),
    dest_country VARCHAR(2),
    d_date DATE
);

--Morti statunitensi all'estero
CREATE TABLE deaths_abroad (
    country VARCHAR(100),
    d_date DATE,
    d_location VARCHAR(100),
    cause_of_death VARCHAR(100)
);

--Allerte estere
CREATE TABLE warnings (
    country VARCHAR(2),
    w_date DATE
);

-- **INSERIMENTO DEI DATI**
COPY country_codes (code, countryname, countryregion)
FROM 'C:\Users\Public\Documents\country_codes.csv'
DELIMITER ','
CSV HEADER;

COPY destinations (c_column, X, passengers, origin_country, dest_country, d_date)
FROM 'C:\Users\Public\Documents\destinations.csv'
DELIMITER ','
CSV HEADER;

COPY deaths_abroad (country, d_date, d_location, cause_of_death)
FROM 'C:\Users\Public\Documents\deaths_abroad.csv'
DELIMITER ','
CSV HEADER;

COPY warnings (country, w_date)
FROM 'C:\Users\Public\Documents\warnings.csv'
DELIMITER ','
CSV HEADER;

-- Eliminazione della colonna "X" della tabella "destinations", che è un duplicato della colonna "c_column"
ALTER TABLE destinations
DROP COLUMN X;

-- Verifica visiva dell'importo dei dati
SELECT *
FROM country_codes;

SELECT *
FROM destinations;

SELECT * 
FROM deaths_abroad;

SELECT *
FROM warnings;

-- Sembra tutto ok, per cui possiamo procedere con le query
