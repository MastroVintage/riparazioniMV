# ARTICOLI RIPARAZIONI — catalogo (per Claude)
Articoli, guide e casi di riparazione (riviste, forum, blog, bollettini, appunti) utili all'SL-P1200 o a lettori con la stessa piattaforma (AN8370S / EHDGA1243-AN8371S / MN6617 / MN6618A / AN8290S, pickup SOALP1200).

## Struttura
Una sottocartella per articolo: `AR###_<slug-breve>\`
- `originale\`  file come caricato (PDF, immagini, HTML salvato)
- `KB\00_INDEX.md`  scheda: titolo, autore, fonte, data, lingua, modello trattato, sintomi, causa, componenti sostituiti/misure, rilevanza per SL-P1200, affidabilita'
- `KB\ocr\pNNN.txt` + `KB\pages\pNNN.png`  testo e pagine (articoli scansionati); `KB\testo.md` per articoli nativi digitali
- `KB\topics.tsv` (facoltativo)

## Tabella articoli
| id | titolo | fonte / data | modello | sintomo -> causa | rilevanza SL-P1200 | entry |
|---|---|---|---|---|---|---|
| (vuoto) | | | | | | |

## Regole
- Controllo pagine bloccante come da skill (articoli multipagina).
- Separare FATTI dell'articolo da OPINIONI/consigli dell'autore; segnare affidabilita' (service note ufficiale > rivista tecnica > forum).
- Ogni articolo entra nel RAG: `..\_RAG\build_corpus.py` scansiona automaticamente `ARTICOLI_RIPARAZIONI\*\KB`.
