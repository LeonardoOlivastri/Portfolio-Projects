# Introduzione al Progetto

Molto spesso le percezioni sul rischio di viaggiare e vivere in alcuni Stati esteri sono basate su indicazioni derivate da organi di Stato o giornali. 
Tutto questo concorre spesso a creare un’opinione pubblica condivisa, che però non sempre si basa su fatti reali. 

In questo progetto ci baseremo sui dati rilasciati dal Dipartimento di Stato Usa, cercando di estrapolare delle informazioni utilizzando delle query in SQL.

# Descrizione del Progetto

Il progetto ha utilizzato 4 tabelle provenienti da <a href="https://data.world/travelwarnings/travel-danger"> questa fonte</a>:
- BTSCountryCode (rinominata *country_code.csv*)
- BTSOriginUS_10_09_to_06_16 (rinominata *destinations.csv*)
- SDamerican_deaths_abroad_10_09_to_06_16 (rinominata *deaths_abroad.csv*)
- SDwarnings_10_09_to_06_16 (rinominata *warnings.csv*)

Si sono generati due file .sql, uno per la creazione delle tabelle e uno per tutte le query.
Le query sono state poi esportate in CSV e sono visionabili singolarmente. 

# Finalità del Progetto

Lo scopo di questo progetto è l'utilizzo di query in SQL e non l'estrapolazione di informazioni significative in sé. 
Il dataset è stato impiegato come semplice esercitazione.
