# SL-P110 — Service Manual HAD8606593C0 (1986) + Adjustment manual FF1 (vale anche per SL-P115 / SL-P116) — per Claude
PARENTELA CON SL-P1200: ALTISSIMA (stessa piattaforma FF1 "regular size", 1986). Catena IC praticamente identica:
| funzione | SL-P110 | SL-P1200 |
|---|---|---|
| optical servo | IC101 AN8370S | IC101 AN8370S |
| DSP EFM/CLV | IC301 MN6617S | IC302 MN6617S |
| filtro digitale | IC302 MN6618A | IC303 MN6618A |
| data slice + PLL (ibrido) | IC304 EHDGA1243 | IC301 EHDGA1243 |
| system control + FL | IC401 MN15261PDF | IC401 MN15261PDK |
| telecomando | IC404 MN1550PDT | IC402 MN1550PDM |
| spindle driver | IC501 AN8290S | IC501 AN8290S |
| quarzo | X301 16.9344 MHz | X 16.9344 MHz |
| audio | IC802 MN6636S deglitch, IC803 AN8376S, IC804 SVIGA011 filtro | DAC PCM54 doppio, AN... (diverso) |
Fonte: lista ricambi sm_s013 (OCR, verificare a vista su img). Riferimenti IC/R/VR DIVERSI dal P1200: tradurre sempre con la tabella sopra.
## Documenti
- sm_s001..s036 = Service manual SL-P110 (pp.1-36): spec, smontaggio, ricambi (s013), terminal guide/LSI (s019-s022: AN8290S pin, MN6617, EHDGA1243), troubleshooting flow (s025), schemi e PCB (s027-s036, schemi a colori/scala grigi).
- adj_s001..s026 = Adjustment manual "regular size FF1 CD player" (pp.1-26), IDENTICO per SL-P110/P115/P116 (tre file uguali caricati): tarature tracking/focus offset, PLL, gain, pickup SOAD30A, test disc SZZP1014F/SZZP1054C, chiave 1.5mm SZZP1044C, vernice RZZ0L01; TP su IC401 MN15261 pin 32/33 (TJ302). Molto utile per il P1200 (stessa logica, stessa CPU famiglia MN15261).
## File: manual/img/<tag>.png (200dpi 1-bit), manual/ocr/<tag>.txt, scan_map.tsv. Ricerca: ..\..\..\_RAG\search.py
