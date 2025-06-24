# Censimento Storico – Tirocinio

**Webapp per esplorare, analizzare e visualizzare dati storici e genealogici dei censimenti antichi.**

---

## Descrizione

Questo progetto nasce con l'obiettivo di offrire una piattaforma interattiva per l'esplorazione e l’analisi di dati storici provenienti da censimenti. Permette di scoprire nomi, cognomi, titoli nobiliari, statistiche demografiche e strutture familiari del passato, facilitando la ricerca genealogica e la comprensione delle comunità storiche.

## Funzionalità Principali

- **Caricamento e visualizzazione dati storici**: carica il tuo file di censimento per esplorarne i dati.
- **Ricerca avanzata**: filtra e cerca tra i dati storici con strumenti potenti e flessibili.
- **Statistiche dettagliate**: visualizza analisi approfondite su età, composizione dei nuclei familiari, titoli, suddivisione per quartieri, ecc.
- **Classifiche dinamiche**: consulta classifiche di nomi, cognomi, titoli e altre informazioni genealogiche.
- **Analisi demografiche**: età media, distribuzione per età e genere, suddivisione per quartieri, struttura dei gruppi familiari.
- **Esempio integrato**: dati demo di un censimento storico (es. “Censimento di Crema 1592-93”) per mostrare le potenzialità dell’applicazione.
- **Interfaccia moderna**: interfaccia responsive realizzata con HTML, CSS (Tailwind), JavaScript e Python (backend).

## Tecnologie Utilizzate

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python, Flask
- **Gestione dati**: Pandas, librerie Python custom per analisi storica
- **Build & Tooling**: Node.js, npm

## Avvio rapido

1. **Clona il repository**
   ```bash
   git clone https://github.com/BulaCibula03/Tirocinio.git
   cd Tirocinio
   ```

2. **Installa le dipendenze**
   > Assicurati di avere Python 3.x, Node.js e npm installati

   ```bash
   pip install -r requirements.txt
   npm install
   ```

3. **Avvia il server**
   ```bash
   npm run dev
   ```

4. **Apri il browser**
   Vai su [http://localhost:5000](http://localhost:5000) per utilizzare la webapp.

## Struttura del progetto

- `/app/templates/` – Template HTML dell’interfaccia
- `/app/static/` – File statici (CSS, JS, immagini)
- `/app/funzioni.py` – Funzioni di analisi sui dati storici
- `/app/routes.py` – Rotte e API Python/Flask
- `/requirements.txt` – Dipendenze Python

## Esempio di utilizzo

1. Carica un file di censimento storico tramite l’interfaccia web.
2. Esplora i dati: visualizza persone, famiglie, quartieri, titoli, ecc.
3. Utilizza la ricerca avanzata e le funzioni di filtro.
4. Analizza le statistiche e le classifiche demografiche.

## Contributi

Contributi, segnalazioni di bug e suggerimenti sono benvenuti! Apri una issue o una pull request su GitHub.

## Licenza

Questo progetto è rilasciato sotto licenza MIT.

---

**Autori**: [BulaCibula03](https://github.com/BulaCibula03) e [Tokyo222307](https://github.com/Tokyo222307)
