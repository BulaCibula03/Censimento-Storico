# Censimento Storico – Tirocinio

**Webapp per esplorare, analizzare e visualizzare dati storici e genealogici dei censimenti antichi.**

---

## Descrizione

Questo progetto nasce con l'obiettivo di offrire una piattaforma interattiva per l'esplorazione e l’analisi di dati storici provenienti da censimenti. Permette di scoprire nomi, cognomi, titoli nobiliari, statistiche demografiche e strutture familiari del passato, facilitando la ricerca genealogica e la comprensione delle comunità storiche.

## Funzionalità Principali

- **Caricamento e visualizzazione dati storici**
- **Ricerca avanzata**
- **Statistiche dettagliate**
- **Classifiche dinamiche**
- **Analisi demografiche**
- **Dati demo integrati**
- **Interfaccia moderna** con TailwindCSS, Flask e strumenti frontend moderni

## Tecnologie Utilizzate

- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Backend**: Python, Flask
- **Build**: Docker, Node.js, npm
- **Analisi**: pandas, librerie custom Python

---

## Avvio

1. **Clona il repository**

```bash
git clone https://github.com/BulaCibula03/Tirocinio.git
cd Tirocinio
```
2. **Rendi eseguibili gli script di esecuzione e di stop**
```bash
chmod +x start.sh
chmod +x stop.sh
```

3. **Costruisci e avvia la webapp**
```bash
./start.sh
```

4. **Accedi alla webapp**
   Vai su [http://localhost:5000](http://localhost:5000)
   
5. **Ferma la webapp**
```bash
./stop.sh
```

---

## Struttura del progetto

- `/app/templates/` – Template HTML
- `/app/static/` – File statici (CSS, JS)
- `/app/funzioni.py` – Funzioni di analisi sui dati storici
- `/app/routes.py` – Rotte e logica Flask
- `/requirements.txt` – Dipendenze Python
- `/Dockerfile` – Dockerfile multi-stage con Python, Node e Tailwind
- `/docker-compose.yml` – Definizione dei servizi
- `/package.json` - Definizione dei plugin e servizi Node.js
- `/tailwind.config.js` - Configurazioni Tailwind CSS

---

## Contributi

Contributi, segnalazioni di bug e suggerimenti sono benvenuti! Apri una issue o una pull request su GitHub.

## Licenza

Questo progetto è rilasciato sotto licenza MIT.

---

**Autori**: [BulaCibula03](https://github.com/BulaCibula03) e [Tokyo222307](https://github.com/Tokyo222307)
