# Introduzione al Progetto

La fonte originale dei dati è l'Australian Government's Bureau of Meteorology e i dati più recenti possono essere raccolti dal <a href="http://www.bom.gov.au/climate/dwo/">sito </a>.

Il set di dati da utilizzare ha colonne extra come "RainToday" e l'obiettivo da predire è "RainTomorrow", che è stato raccolto a questo <a href="https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData">indirizzo</a>.

Questo set di dati contiene le osservazioni delle metriche meteorologiche per ogni giorno dal 2008 al 2017. 



# Descrizione del Progetto

Di seguito, utilizzeremo gli algoritmi di classificazione per creare un modello basato sui dati di addestramento e valutare i dati di test utilizzando diverse metriche di valutazione.

Gli algoritmi utilizzati saranno i seguenti:
- Regressione Lineare
- Regressione Logistica
- KNN
- Decision Tree
- SVM

I modelli verranno valutati utilizzando i seguenti parametri:
- Accuracy Score
- Jaccard Index
- F1 Score
- Log-loss
- Errore Assoluto Medio
- Errore Quadratico Medio
- R quadro
