# KB UNIVERSITY — Technics/Panasonic/Quasar Technical Guide "Compact Disc Player Technology" (SL-P150 / SL-P405C Series) — per Claude
Percorso: E:\tools\repo\riparazioniMV\audio\Technics SL-P 1200\UNIVERSITY\TG_SL-P150_CD_Player_Technology\KB\
Documento: ORDER NO. AD8812333T0 (A6), Audio Division Matsushita Electric Industrial, codice stampa K881203500MIZUTA. 141 pagine numerate + copertina, indice, retro.
PDF ordinato e pulito: ..\Technics_TechGuide_CD_Player_Technology_SL-P150_SL-P405C_ordinato_pulito.pdf (144 pagine, segnalibri per capitolo). Scansioni originali: ..\_scan_originali\.
Controllo pagine (eseguito per primo): 1..141 tutte presenti. Duplicato: scan0061 pagg.1-8 = scan0060 (pp.87-94), usata scan0060. Numeri pp.34 e 38 stampati deboli ma confermati dalla sequenza. p.111 era capovolta (OSD sbagliato), corretta.

## Perche' serve per SL-P1200 (alta rilevanza: stessa piattaforma "FF-1" di prima generazione)
- Catena digitale identica al P1200: AN8370S (servo ottico) -> AN8371S data slice/PLL (nel P1200 l'ibrido EHDGA1243) -> MN6617 (DSP) + MN4416S-12 (RAM 16K) -> MN6618A (filtro digitale). Fig.18-16 p.88.
- Cap.17 (pp.46-69) = spiegazione circuitale del servo con AN8370S + componenti discreti (stessa architettura del P1200): pull-in focus, control logic, APC, RF/dropout, focus/tracking servo, kick/brake, traverse, linear motor, CLV, PLL. Tabella pin AN8370S p.68 (coincide con KB\pins\IC101_AN8370S.tsv).
- Cap.18 (pp.76-88) = MN6617 in dettaglio: EFM demod, subcode, interpolazione, correzione errori, spindle servo con FG limiter (p.85; nel P1200 FG pin66 non usato), interfaccia CPU (MLD/MCLK/MDATA, STAT), FPC (2.5V costante a PLL agganciato, p.67/86), tabella pin p.87.
- Cap.22 (pp.121-136) tarature con servo gain adjuster SZZP1094C (il service manual P1200 cita invece lo SZZP1017F): procedura focus/tracking gain con LED LOW/GOOD/HIGH (p.134); la frequenza (es. 750Hz/1.2kHz) dipende dal modello -> per P1200 usare KB\adjustments.md.
- Cap.12-16 = teoria generale (EFM, CIRC, subcode, pickup single beam 4-split PD con prisma ad angolo critico).
- NON applicabile al P1200: servo modificato AN8373S/AN8374S (pp.70-75), MASH MN6623 (pp.93-101), meccanica changer (cap.21, 23), CPU MN1554PEP.
- ATTENZIONE: qui IC-301 = MN6617 (nel P1200 IC302) e IC-301 FPC pin 78; la numerazione IC/R/VR e' quella dei modelli del libro.

## File
| file | contenuto |
|---|---|
| topics.tsv | capitoli/paragrafi -> pagine |
| chips.tsv | chip -> ruolo -> equivalente SL-P1200 -> pagine |
| pages/pNNN.png | pagina NNN pulita (show-through rimosso, raddrizzata, contenuto dritto), 300dpi 16 grigi |
| ocr/pNNN.txt | testo OCR (macchina da scrivere: buona qualita') |
| scan_map.tsv | pagina <- scansione originale |
Speciali: p000a_cover, p000b_contents, p999_backcover.

## Lookup
grep in ocr/ -> pages/pNNN.png per figure. Per tensioni/ref reali del P1200 usare sempre ..\..\..\KB\.
