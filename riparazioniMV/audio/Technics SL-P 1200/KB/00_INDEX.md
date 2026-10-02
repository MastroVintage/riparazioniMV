# KB Technics SL-P1200 — punto di ingresso (per Claude)
Leggere SOLO questo file all'inizio; poi aprire i file mirati. Tutto deriva da DATA/Technics_SL-P1200_service_unito_pulito.pdf (Service Manual ORDER NO. HAD8609723C0, 1986).
Percorso locale: E:\tools\repo\riparazioniMV\audio\Technics SL-P 1200\KB\  (repo git riparazioniMV, remote MastroVintage/riparazioniMV)

## Fatti chiave (verificati sul manuale)
- IC101 = AN8370S optical servo control (focus/tracking/APC/RF) — Main PCB D.
- IC501 = AN8290S spindle motor drive — Spindle Motor Drive PCB C. (NON AN8370S)
- IC302 MN6617S DSP/EFM/CLV, IC303 MN6618A digital filter, IC304 MN4416S-12 RAM 16K, IC301 EHDGA1243 data slice+PLL.
- IC401 MN15261PDK system control+FL, IC402 MN1550PDM remote, IC403 MN1280-R reset.
- Audio: IC821 MN51005PDN S/P conv -> IC822/823 PCM54KP-M DAC (L/R) -> S/H uPD4053 IC824/825 + M5238 IC826/827 -> LPF AL079 IC830/831 -> buffer NJM5532 IC828/829 (Class-AA). Headphone IC851 NJM4556.
- Clock: X 16.9344 MHz (XCK IC302-25), SMCK 4.2336 MHz. FL VPP -33V. AN8290S GND/PGND = VEE -8.0V, DCR 2.5V.

## File (ordine di utilita')
| file | contenuto | uso |
|---|---|---|
| ic_list.tsv | tutti gli IC: ref, part, funzione, scheda, tile schema, file pin | prima consultazione per qualsiasi IC |
| pins/ICxxx_PART.tsv | piedinature trascritte (AN8370S, AN8290S, MN6617S, MN6618A, EHDGA1243, MN15261PDK, MN1550PDM, MN51005PDN) | funzione pin; tensioni ai pin -> guardare il tile dello schema |
| adjustments.md | sequenza regolazioni, VR, dischi test, pagine | taratura |
| index_components.tsv | indice OCR (approssimato, recall ~50%) token->sheet,x,y,tile | trovare R/C/Q/D/TJ/VR sugli schemi; se manca, cercare visivamente nel tile |
| sheets/<S>/overview.png | foglio intero 2000px | orientarsi (scala x300dpi = W/2000) |
| sheets/<S>/rXcY.png | tile 1600x1600 @300dpi, overlap 200px, passo 1400 | lettura dettagli/tensioni/forme d'onda |
| sheets/<S>/full_300dpi.png | foglio intero 300dpi | crop personalizzati |
| manual/img/mNN.png | pagina manuale NN (1-bit 300dpi) | lettura testo/tabelle/figure |
| manual/ocr/mNN.txt | OCR pagina NN (rumoroso su tabelle) | grep veloce |
| _tools/ | script (stitch, clean, tiles, OCR index) + TSV OCR grezzi | rigenerare |

Tile da coordinate 300dpi: col = floor(x/1400) (se x%1400>1400-? vedi overlap), row = floor(y/1400); box esatti in _tools/sheets_meta.json.

## Fogli (sheets/)
| sheet | contenuto | pagine man. |
|---|---|---|
| S1_pcb_A | PCB lato rame/serig.: FL(A), Operation(B), Spindle motor drive(C), Remote unit, Socket(F), Spindle control(G), Laser switch control(H), Pitch control(K), Pitch VR(L), Headphone(M), Extension | 49-51 |
| S2_pcb_B | PCB: Main(D), Audio(I), Regulator(E), Line out(N), Power source(J) | 52-54 |
| S3_sch_1 | Schema griglia col 1-16: note/switch S1..S631, telecomando (IC1001 MN6030), codici tasti, FL601, Pitch control(K), Spindle motor drive(C, IC501), FL(A, IC601), Operation(B) | 55-58 |
| S4_sch_2 | Schema col 17-34: Main(D) completo (servo, DSP, RAM, filtro, system control, reset, traverse/plunger), Regulator(E), Socket(F), Pitch VR(L) | 59-62 |
| S5_sch_3 | Schema col 35-53: Spindle control(G, IC331), Laser switch control(H), Audio(I), Power source(J, USA/others), Headphone(M), Line out(N), fusibili | 63-66 |
| S6_block | Schema a blocchi | 67-70 |
Mappa rapida S4 (overview 2000px): IC402 sx-alto; IC103/IC102 coil drive in alto; IC301 centro-alto; IC101 dx-centro; IC401 sx-basso; IC403/IC304 centro-basso; IC302 centro; IC303 dx-basso; regolatori IC11-14 a dx.
Mappa rapida S5: IC821 centro-sx, DAC IC823(R) IC822(L) in basso, S/H+filtri+buffer al centro, regolatori IC801-806 in alto.

## Pagine manuale (manual/img)
m00_* copertina/spec/precauzioni laser/pannello posteriore/comandi | m05-m09 uso (play, random, program, pitch, search, time mode, auto space, auto cue) | m10 pulizia lente, precauzioni pickup | m10-m12(16-20) smontaggio | m21-m22 resistenze e condensatori | m23-m26 ricambi (IC/Q/D p.23) | m27-m32 esplosi meccanica + imballo | m33 sostituzione IC SMD | m34(?)-m40 regolazioni elettriche | m41-m45 terminal function LSI | m46 terminal guide (package/pinout IC, transistor, diodi) | m47-48 PCB & wiring connection diagram
Nota numerazione: mNN = numero pagina stampato sul manuale (verificato per NN>=5).

## Procedura di lookup consigliata
1. IC -> ic_list.tsv -> pins/ -> tile schema per tensioni.
2. Componente passivo/TJ -> grep index_components.tsv; se assente -> overview del foglio probabile -> tile.
3. Taratura -> adjustments.md -> manual/img/m35..m40.
4. Ricambi/codici -> manual/img/m23..m26 (OCR inaffidabile sui codici).

## Materiale formativo collegato
- ..\UNIVERSITY\KB\00_INDEX.md : Technical Guide Vol.17 (SL-XP7) - teoria AN8370S (sez.6 pp.20-31), AN8371S data slice/PLL (= funzioni EHDGA1243), MN6617 (sez.9 pp.36-50), troubleshooting pp.55-86. Ref IC del libro = SL-XP7, non SL-P1200.
