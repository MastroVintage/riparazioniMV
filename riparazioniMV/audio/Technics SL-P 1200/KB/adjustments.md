# SL-P1200 Electrical adjustment - mappa rapida
Fonte: manuale pp.35-40 (KB/manual/img/m35..m40.png, testo OCR in KB/manual/ocr/). Leggere l'immagine della pagina per i dettagli (forme d'onda, impostazioni oscilloscopio).

Strumenti: servo gain adjuster SZZP1017F (+ conversion connector SZZP1032F su CN103, rimuovere shorting connector CN103 dal Main PCB), oscilloscopio 2ch 30MHz, oscillatore BF.
Dischi test: SZZP1014F test disc, SZZP1054C inspection, SZZP1056C uneven, SZZP1057C black band, disco normale.
TP del servo gain adjuster: TP1 / TP2 / TP3; selector 1 = 750Hz (focus), selector 3 = 1.2kHz (tracking).

| step | regolazione | trimmer | pagina | criterio (sintesi OCR) |
|---|---|---|---|---|
| 1 | rimuovere front panel | - | 16 | |
| 2 | collegare servo gain adjuster | - | 35 | |
| 3 | preset temporaneo dei VR | tutti | 34/35 | |
| 4 | Best eye (PD balance) | VR101 | 36 | eye pattern RF il piu' aperto possibile (CH1 su TP RF/TE, test disc) |
| 5 | Focus gain | VR104 (5k B) | 36 | selector 1, 750Hz: ampiezze uguali sui due canali (a=b) |
| 6 | Tracking gain | VR102 | 36 | selector 3, 1.2kHz: ampiezze uguali sui due canali |
| 7 | Focus/Tracking offset temporaneo | VR105 / VR103 | 37 | dopo TOC, in stop: livello DC indicato |
| 8 | Focus offset | VR105 (10k B) | 37 | black band disc SZZP1057C: minima depressione RF |
| 9 | Tracking offset | VR103 | 38 | black band disc: minima depressione RF su CH1 e ampiezza CH2 |
| 10 | Tracking error compensation | VR106 | 38 | TP tracking error comp (+)/chassis: DC 0 +/-5mV, 500mV/div, 1ms, DC |
| 11 | PLL | VR301 (1k B) | 38 | test disc SZZP1054C traccia 7 (black spot 0.5mm): centro della finestra in cui la forma d'onda e' stabile |
| 12 | Verifica play dopo regolazione | - | 39 | skip search, difetti, uneven disc |
| - | Turntable height | meccanica | 40 | |

Posizioni sullo schema: VR104/VR105/VR301 in KB/sheets/S4_sch_2/r1c3.png (+r0c3/r1c4); VR101-VR103 in S4_sch_2 r0c4/r1c4 (zona IC101 "Optical servo").
