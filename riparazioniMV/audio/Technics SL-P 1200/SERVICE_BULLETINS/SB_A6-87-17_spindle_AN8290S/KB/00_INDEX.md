# Service Bulletin A6-87-17 (set. 1987) — SL-P1200: spindle drive AN8290S surriscaldato
Fonte: Matsushita Services Company (USA), Engineering Support Division. Dist: A6,97,W-877. 2 pagine (fronte + retro "OVER", non numerato). Riguarda SL-P1200 (ref IC/Q = SL-P1200).
PDF pulito: ..\DATA\SB_A6-87-17_spindle_AN8290S_pulito.pdf · pagine: pages\p01-p02.png · OCR: ocr\ · scan_map.tsv

## Sintomi
1) Nessun funzionamento. 2) Legge il TOC ma non entra in play.
## Causa
IC501 AN8290S (spindle drive) si surriscalda e va in blocco quando: A) vibrazioni durante il play fanno saltare il pickup; B) uso eccessivo dello skip; C) play con la vite di blocco trasporto (transport lock shaft) ancora inserita.
Ogni condizione fa surriscaldare e danneggiare Q12, Q13, Q101, Q102; il calore secca le saldature dei transistor (falsi contatti o ponti di stagno).
## Rimedio (kit SZZP1093C)
| ref | originale | nuovo |
|---|---|---|
| Q12 | 2SC1846 o 2SD973 | 2SD1266 |
| Q13 | 2SA885 o 2SB793 | 2SB941 |
| Q101 | 2SD1055 | 2SD1266 |
| Q102 | 2SB822 | 2SB941 |
| dissipatore | — | SMWD3E su IC501 |
- p02 Fig.1: posizione Q12/Q13 (lato sx) e Q101/Q102 (in alto a dx) sulla MAIN PCB. Fig.2: montaggio dissipatore SMWD3E tra spindle PCB e sub PCB.
- Procedura dissipatore: A) allentare le viti di spindle PCB e sub PCB; B) inserire la lamella sottile del dissipatore tra spindle PCB e sub PCB; C) rimontare le PCB; D) fissare la lamella alla sub PCB con colla tipo "3M".
- Eseguire la modifica, qualunque sia il difetto lamentato, sulle unita' con suffisso seriale fino a "J" compreso. Modifica in produzione dal 3/7/1987: suffisso da "J" a "K".

## Collegamento alla KB SL-P1200 (verificato)
- IC501 = AN8290S, Spindle Motor Drive PCB C (KB\ic_list.tsv; pin in KB\pins\).
- Ricambi originali confermati sul service manual: manual\img\m23.png (Q12 2SD973, Q101 2SD1055, Q102 2SB822).
- Schema: Q101/Q102/2SD1055/2SB822 su sheets\S4_sch_2 tile r0c1-r0c2 (x300~2500-2930, y300~500-600); 2SD973 (Q12) su S4_sch_2 x300~7147 y300~835 tile r0c4/r0c5 (index_components.tsv). Q13 non indicizzato dall'OCR: cercarlo vicino a Q12.
- Stesso guasto e kit diverso su SL-P520/P720: vedi ..\..\TI_UK_1987-05_SL-P520_P720_spindle (ref diversi, non applicare al P1200).
