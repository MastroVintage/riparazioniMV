# Technical Information Panasonic U.K. (maggio 1987) — SL-P520 / SL-P720: spindle drive surriscaldato
MODELLO CORRELATO, NON SL-P1200: i riferimenti IC e Q sono dei modelli P520/P720. Pagina unica, rif. P15/1084. La scansione originale ne conteneva tre copie identiche (scan0075 pp.1, 3, 5): tenuta la migliore (p.1).
PDF pulito: ..\DATA\TI_UK_1987-05_SL-P520_P720_spindle_pulito.pdf · pages\p01.png · ocr\p01.txt

- Sintomi: nessun funzionamento, oppure legge il TOC ma non entra in play.
- Causa: lo spindle drive IC si surriscalda e si blocca con vibrazioni, uso eccessivo di cue/review, oppure accensione e play con il transit clip ancora montato. IC4 e IC5 surriscaldano e i loro fusibili interni si aprono. La deriva termica manda in corto Q11, Q12, Q101 e Q102; il calore secca le saldature dei loro piedini.
- Rimedio: kit SZZP1090C.
  1) Sostituire Q11 e Q101 con 2SC1846, Q12 e Q102 con 2SA885. I nuovi transistor sono piu' grandi e vanno montati come in figura (lato stampato).
  2) Aggiungere 4 diodi in serie sui collegamenti dei transistor per ridurre la tensione sui rami +11 V / -11 V (IC4/IC5 -> driver). I diodi A e B prendono il posto di ponticelli.
  3) Montare il dissipatore sullo spindle IC501 (tra spindle P.C.B. e sub P.C.B.).
- Confronto con SL-P1200 (SB A6-87-17): stesso meccanismo di guasto e stesso dissipatore su IC501. Sul P1200 pero' 2SC1846/2SA885 sono i pezzi ORIGINALI da sostituire con 2SD1266/2SB941 (kit SZZP1093C), e il bollettino USA non prevede diodi in serie. Non applicare ref o kit di questo documento al P1200.
