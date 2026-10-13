# Service Manual Supplement SL-P1200X — ORDER NO. AD8908221S1 — Balance Out PCB (K) modificata
Da archiviare e usare con il service manual SL-P1200X, ORDER NO. HAD8707245C1 (non presente nel repo). Pagine 1-4 (copertina = p.1 non numerata; p.4 "Printed in Japan K891002480YY"), complete. p05 = foglio allegato non numerato "IMPORTANT!!! Grounding the unit".
Riguarda il SOLO SL-P1200X (versione con uscite bilanciate). Ref della scheda K (R9xx, Q9xx, IC9xx).
PDF pulito: ..\DATA\SUP_AD8908221S1_SL-P1200X_balance_out_pulito.pdf · pages\p01-p05.png · ocr\

- p01: la balance output P.C.B. e' cambiata sulle unita' con suffisso seriale "Q" o successivo. Lettura seriale (es. A E 6 1 3 1 A 2 6 5): linea di produzione, anno (6=1986 ... 9=1989), mese (1-9 = gen-set, J ott, K nov, L dic), giorno, suffisso, numero.
- p01 Replacement parts list (resistenze):

  | ref | originale | nuovo | valore | nota |
  |---|---|---|---|---|
  | R903-906 | ER0S2TKF1801 | — | — | Deletion |
  | R911-914 | ER0S2TKF5602 | ER0S2TKF2702 | 27k 1/4W | Change |
  | R915-922 | ERD25FJ150 | ERD25FJ270 | 27 ohm 1/4W | Change |
  | R935-942 | ER0S2TKF8R20 | ER0S2TKF15R0 | 15 ohm 1/4W | Change |
  | R945, 946 | ER0S2TKF6200 | — | — | Deletion |
  | R971-974 | — | ER0S2TKF3300 | 330 ohm 1/4W | Addition |
  | R991, 992 | — | ER0S2TKF2202 | 22k 1/4W | Addition |
  | R993-996 | — | ER0S2TKF3902 | 39k 1/4W | Addition |
  | R997-1000 | — | ER0S2TKF33R0 | 33 ohm 1/4W | Addition |
- p02: schema Balance Out P.C.B. (K), versione ORIGINALE. Componenti: IC901/IC902 SVINJM5532DD; IC903/IC904 SVINJM2060DD; IC981 SVITLP552 (photo interrupter, comando CONTROL da FL P.C.B. A tramite CN981); relè RLY901/902; Q901-908 2SA1309, Q909-916 2SC3311, Q917-920 2SC1847, Q921-924 2SA886; uscite CN903/CN904; CN906; ingressi BT901/BT902.
- p03: schema "BALANCED OUTPUT CIRCUIT", versione NUOVA, con le aggiunte e le cancellazioni marcate (Addition/Deletion).
- p04: PCB Balance Out, originale (sopra) e nuova (sotto).
- p05: foglio allegato per l'utente; stesso testo di SB A6-88-11 p.4 ("Grounding the unit") preceduto da: unita' modificate con circuito di massa interno della tastiera migliorato e un morsetto di massa esterno aggiunto.
- Non riguarda l'SL-P1200 base: quella versione non monta la scheda K.
