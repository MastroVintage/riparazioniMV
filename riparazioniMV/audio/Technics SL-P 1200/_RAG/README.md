# _RAG — corpus di ricerca per Claude (progetto Technics SL-P1200)
- corpus.jsonl: 1 riga = 1 chunk (~1400 caratteri, overlap 200) di testo OCR con metadati: source, title, kind, relevance_SL_P1200, page (numero stampato), page_tag, section (da topics.tsv), chips, refs (IC/TJ/VR/CN/TP/Q/D), image (percorso pagina relativo alla cartella del dispositivo), text.
- Fonti: SM_SL-P1200 (service manual, KB\), TG17_SL-XP7, TG_SL-P150, TG25_AutoCD, TSG_1986-1990, TG_Adjustments (UNIVERSITY\...).
- Ricerca: dalla cartella "Technics SL-P 1200":  python _RAG\search.py "testo da cercare" [-k 8] [-s SOURCE]
- Ricostruzione dopo nuovi documenti:  python _RAG\build_corpus.py  (aggiungere la nuova fonte nella lista SRC).
- L'OCR delle tabelle e' rumoroso: per valori numerici aprire sempre l'immagine indicata in "image".
## Fatti verificati a vista (prevalgono sull'OCR)
- SL-P1200 / PL1200X / P1300: pickup SOALP1200, MIN RF 0.84 Vpp, lubrificante RZZ0L05, T/T height N/A (TSG_1986-1990 p.8).
- SL-P1200 IC101 = AN8370S, IC501 = AN8290S (spindle), IC302 = MN6617S, IC303 = MN6618A, IC301 = EHDGA1243 (KB\ic_list.tsv).
