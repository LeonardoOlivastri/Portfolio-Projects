-- QUERY 1: Contare il numero di morti all'estero diviso per cause di morte
SELECT cause_of_death, COUNT(cause_of_death) AS deaths_num
FROM deaths_abroad
GROUP BY cause_of_death
ORDER BY deaths_num DESC;
/* Vedere file "Query 1": si nota che la maggior parte delle morti all'estero è relativa a omicidi, e conseguentemente
a incidenti automobilistici. Curioso il terzo e quarto dato per numero di morti, rispettivamente "suicidio" e "annegamento"*/

-- QUERY 2: Contare il numero di allerte per ogni paese estero. Si includono anche i paesi senza allerte
SELECT a.countryname, COUNT(b.country) AS warnings_num
FROM country_codes a
LEFT JOIN warnings b
ON a.code=b.country
GROUP BY a.countryname
ORDER BY warnings_num DESC;
-- Vedere file "Query 2": il Messico risulta il paese con più allerte al mondo. 

/* QUERY 3: Contare il numero di passeggeri morti in un certo paese e dividerlo per il totale dei viaggiatori che si sono recati in quel paese.
Se questo risultato è sopra un certo valore, il paese viene etichettato come "pericoloso", altrimenti come "non pericoloso" */
WITH pass_sum AS (
    SELECT d.dest_country, cc.countryname, SUM(d.passengers) AS total_passengers
    FROM destinations d
    JOIN country_codes cc ON d.dest_country = cc.code
    GROUP BY d.dest_country, cc.countryname
)
SELECT ps.countryname,
       da.deaths_num,
       ps.total_passengers,
       CASE
           WHEN (da.deaths_num::NUMERIC / ps.total_passengers::NUMERIC) > threshold THEN 'Pericoloso'
           ELSE 'Non Pericoloso'
       END AS risk_status
FROM pass_sum ps
LEFT JOIN (
    SELECT country, COUNT(*) AS deaths_num
    FROM deaths_abroad
    GROUP BY country
) da ON ps.countryname = da.country
ORDER BY risk_status DESC, da.deaths_num DESC;
/*Si è usata una CTE per identificare il numero di passeggeri volati in ciascun paese.
Il database originale li numerava in modo cumulativo viaggio dopo viaggio, per cui si è preso solamente il valore massimo.
Il risultato della CTE si può vedere nel file "Query 3a"
Nella query princpale si è poi contato il numero di morti e si è creato un indice. 
A causa di errori nel database, a volte il numero è superiore a 1 (che è impossibile).
La tabella finale può essere visionata nel file "Query 3b"*/


/*QUERY 4: Contare il numero di morti entro 1 mese dalla diramazione di un'allerta in un certo paese. 
Vengono contate solo le morti che possono essere causate da quell'allerta (omicidio, disastro naturale ecc)*/
SELECT deaths_abroad.country, COUNT(deaths_abroad.country) AS num_death_one_week
FROM deaths_abroad
INNER JOIN country_codes
ON deaths_abroad.country=country_codes.countryname
INNER JOIN warnings
ON country_codes.code=warnings.country
WHERE warnings.w_date >= deaths_abroad.d_date
    AND w_date <= d_date + INTERVAL '1 month'
    AND deaths_abroad.cause_of_death IN('Homicide', 'Disaster', 'Execution', 'Terrorist Action')
GROUP BY deaths_abroad.country
ORDER BY deaths_abroad.country ASC;
-- Vedere file "Query 4": il maggior numero di morti è in Messico


--QUERY 5: Variazione del numero di viaggi entro 1 mese dalla diramazione di un'allerta in un certo paese.
WITH helper AS (
    SELECT w.country, 
        AVG(CASE WHEN w.w_date <= d.d_date + INTERVAL '1 month' THEN 1 ELSE 0 END) AS travel_after_alert, 
        AVG(CASE WHEN w.w_date > d.d_date + INTERVAL '1 month' THEN 1 ELSE 0 END) AS normal_travel
    FROM warnings w
    INNER JOIN destinations d
    ON w.country = d.dest_country
    GROUP BY w.country
)
SELECT c.countryname,
CASE
	WHEN h.travel_after_alert > h.normal_travel THEN 'Viaggi Aumentati'
	ELSE 'Viaggi Diminuiti'
END AS change
FROM country_codes c
INNER JOIN helper h
ON c.code = h.country;
/*Si è deciso di utilizzare una CTE chiamata 'helper' per calcolare la media dei viaggi verso una nazione entro un mese dall'allerta
e la media dei viaggio verso una nazione fuori dall'allerta. Il risultato della sottoquery è visibile nel file "Query 5a"
Nella query principale si è poi utilizzato il costrutto CASE per verificare se travel_after_alert - normal_travel fosse maggiore di 0:
in quel caso la riga restituisce la stringa 'Viaggi Aumentati', e viceversa. 
Il risultato dell'intera query è visibile nel file "Query 5b"*/


--QUERY 6: Contare il numero di allerte nel 2010 per ogni continente
SELECT country_codes.countryregion, COUNT(warnings.w_date) AS warnings_num
FROM warnings
RIGHT JOIN country_codes
ON warnings.country=country_codes.code
WHERE EXTRACT(YEAR FROM warnings.w_date) = '2010'
GROUP BY country_codes.countryregion;
-- Vedere file "Query 6": il maggior numero di allerte nel 2010 è in Africa, e immediatamente dopo in Asia
