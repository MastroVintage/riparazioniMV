# KB UNIVERSITY — Technics/Panasonic "Technical Guide Vol.17" (SL-XP7) — punto di ingresso (per Claude)
Percorso: E:\tools\repo\riparazioniMV\audio\Technics SL-P 1200\UNIVERSITY\KB\
Documento: Panasonic Technical Guide Vol.17, ORDER NO. APD860582, Auto Products Division (Matsushita Communication Industrial).
Apparecchio descritto: Technics SL-XP7 (lettore CD portatile, pickup single-beam). Manuale di FORMAZIONE (teoria di funzionamento + troubleshooting), non service manual.
PDF ordinato e pulito: ..\Technics_TechGuide_Vol17_SL-XP7_ordinato_pulito.pdf (91 pagine, segnalibri per sezione). Scansioni originali in ..\_scan_originali\ (ordine non sequenziale, mappa in scan_map.tsv).

## Perche' serve per SL-P1200 (stessa generazione di chip Matsushita 1986)
- AN8370S = stesso chip di SL-P1200 IC101 -> sezione 6 (pp.20-31) e' la spiegazione interna del servo ottico: control logic, APC, RF/dropout, auto-focus/FE, TE/kick/hold, drive.
- MN6617 = SL-P1200 IC302 MN6617S -> sezione 9 (pp.36-50): CIRC/EFM, decodifica, subcode, CLV servo (rough 11T + fine), interfaccia micro (MLD/MCLK/MDATA, STAT).
- AN8371S (data slice + PLL) svolge le stesse funzioni dell'ibrido EHDGA1243 (SL-P1200 IC301): segnali EFM, PCK, FPC, SRF, DO, SLC. Sezione 8 (pp.34-35) + 9-3 (p.44).
- Diversi: spindle AN8281S (P1200: AN8290S), micro MN1554CAC/CAF (P1200: MN15261PDK), reset MN1208 (P1200: MN1280-R), alimentazione/LCD da auto-portatile.
- ATTENZIONE: i riferimenti IC/Q/R/VR in questo libro sono quelli del SL-XP7 (es. IC601 = LSI MN6617 nel SL-XP7, p.53) e NON corrispondono alla numerazione SL-P1200. Usare il KB SL-P1200 (..\..\KB\) per ref e tensioni reali.
- Valori di riferimento utili anche per P1200 (stesso chip): pin 78 FPC del MN6617 = 2.5V costante in play (PLL agganciato), impulsi 2.5V+/-2.5V durante aggancio (p.44); TRON alto = traverse tracking servo, basso = 11T servo (p.50).

## File
| file | contenuto |
|---|---|
| topics.tsv | sezioni/sottosezioni -> pagine |
| chips.tsv | chip -> ruolo -> equivalente SL-P1200 -> pagine che lo citano |
| pages/pNNN.png | pagina NNN pulita (show-through rimosso, raddrizzata, contenuto sempre dritto: le pagine con schema orizzontale sono ruotate in landscape), 300dpi, grigi 16 livelli |
| ocr/pNNN.txt | testo OCR della pagina (buona qualita' sul testo, discreta su schemi) -> grep veloce |
| scan_map.tsv | pagina libro <- file di scansione originale e pagina, rotazione applicata |
Pagine speciali: p000a_cover, p000b_contents1, p000c_contents2, p000d_divider_circuit_operation, p054b_divider_troubleshooting. Pagine numerate 1..86 tutte presenti (nessuna mancante); la pagina bianca finale e' stata scartata.

## Lookup
1. Concetto/circuito -> topics.tsv -> ocr/pNNN.txt (grep) -> pages/pNNN.png per figure.
2. Chip -> chips.tsv.
3. Diagnosi guasto: TS-1 symptom check p55 -> TS-2 procedure pp.56-78 (logica valida anche per P1200: focus search, spindle, RF/tracking, audio), tensioni connettori/micro pp.79-86 (solo SL-XP7).
