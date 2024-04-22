# Descrizione del Progetto

Ci siamo trovati di fronte a un problema di classificazione binaria: l'acqua è potabile (1) oppure no (0). L'obiettivo è stato quello di trovare il modello che meglio predicesse la potabilità sulla base delle 9 features contenute all'interno del dataset.  

Dopo aver pulito i dati e analizzato la loro distribuzione e correlazione, abbiamo cercato le 3 features che meglio potessero descrivere la potabilità dell'acqua attraverso il calcolo della *mutual information*, in grado di intercettare anche relazioni non lineari o polinomiali.  

Fatto ciò, abbiamo analizzato le performance di tre modelli (Logistic Regression, Random Forest e K-Nearest Neighbors), fittando l'intero training set oppure solamente le 3 features selezionate. Sorprendentemente, i modelli migliori si sono rivelati essere quelli che consideravano l'intero dataset: probabilmente vi erano alcune interazioni tra le features che producevano dell'informazione che la feature selection non ha afferrato.  

Avendo selezionato i modelli di Random Forest e K-Nearest Neighbors come i migliori, abbiamo proseguito con l'ottimizzazione degli iperparametri attraverso GridSearch. Facendo ciò, si è visto che il modello in assoluto più performante è il KNN, con un'accuracy sul test set di circa il 71%.
