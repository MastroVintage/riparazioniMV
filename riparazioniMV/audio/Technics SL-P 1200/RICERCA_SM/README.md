# RICERCA_SM — registro dei documenti già trovati

Usato dall'attività giornaliera "Monitor service manual SL-P1200".

## File
- `documenti_trovati.tsv` — un documento per riga, separatore TAB, codifica UTF-8.

## Colonne
| colonna | contenuto |
|---|---|
| chiave | identificativo normalizzato `modello|tipo|lingua` in minuscolo (es. `sl-p1200|service-manual|en`). Tipi: service-manual, adjustment, operating-instructions, technical-guide, troubleshooting, datasheet, brochure, forum-thread, altro |
| nome_file | nome del file salvato (vuoto se non scaricato) |
| titolo | titolo del documento |
| fonte_url | URL di provenienza (vuoto per i documenti già posseduti senza fonte nota) |
| data | data in cui è stato registrato (AAAA-MM-GG) |
| stato | `posseduto` (già nel repo), `scaricato` (in Downloads\ricercasm_*), `non_scaricato` (a pagamento / login / casella da spuntare), `segnalato` (thread o pagina senza file) |
| percorso | dove si trova (relativo al repo o cartella Downloads) |
| note | utilità e annotazioni |

## Regola di confronto (prima di segnalare o scaricare)
Un documento trovato è GIÀ NOTO se almeno una di queste corrisponde a una riga esistente:
1. stessa `chiave`;
2. stesso `nome_file` (confronto senza maiuscole, estensione, spazi, `_` e `-`);
3. stessa `fonte_url` (senza `http(s)://`, `www.` e `/` finale).
Eccezione: se è una versione migliore (scansione più leggibile, edizione/supplemento diverso, pagine mancanti) si registra come nuova riga con nota "versione migliore di <chiave>".

## Aggiornamento
A fine ricerca si aggiungono le nuove righe (non si cancellano mai righe), poi commit e push sul repo riparazioniMV.
