# SERVICE_BULLETINS — bollettini di servizio, technical information e supplementi (SL-P1200)
Ogni documento: `<id>\KB\00_INDEX.md` (sintesi in italiano + collegamenti alla KB del P1200), `KB\pages\pNN.png` (pagine dritte e pulite, 300 dpi, 16 grigi), `KB\ocr\pNN.txt`, `KB\scan_map.tsv` (pagina -> scansione originale), `DATA\<id>_pulito.pdf`.
Scansioni originali (tutte capovolte di 180 gradi, con pagine bianche): `_scan_originali\`. Script: `_tools\` (clean_gray.py, build_sb.py).
Inclusi automaticamente nel RAG (`_RAG\build_corpus.py`, sorgente = id cartella, kind = service_bulletin).

| id | documento | data | modelli | argomento | rilevanza P1200 |
|---|---|---|---|---|---|
| SB_A6-87-17_spindle_AN8290S | Service Bulletin A6-87-17 | 09/1987 | SL-P1200 | AN8290S (IC501) surriscaldato: Q12/Q13/Q101/Q102 -> 2SD1266/2SB941, dissipatore SMWD3E, kit SZZP1093C; suffisso <= J | ALTA |
| SB_A6-88-11_massa_switch_RF | Service Bulletin A6-88-11 (4 pp.) | 08/1988 | SL-P1200, P1200X | pop, play interrotto, telecomando a filo, TOC: capocorda massa, piastra massa frontale, C415 0.001->0.01uF, S101 -> SWSD12001, RF TJ302 0.7-1.2 Vpp, kit TAS8512001 | ALTA |
| SB_A6-89-1_gommino_disc_magnet | Service Bulletin A6-89-1 | 04/1989 | SL-P1200, P1200X, P1300 | CD 8 cm: gommino disc magnet 0.5 mm -> SHGD155-1 2.5 mm; suffisso <= N | ALTA |
| TI_HAD8607677T0_FPC_jig | Technical Information HAD8607677T0 | 1986 | SL-P110 serie, SL-P1200 | fixture SZZP1070C/SZZP1071C per collaudo main PCB (CN107) | media |
| SUP_AD8908221S1_SL-P1200X_balance_out | Supplement SM SL-P1200X AD8908221S1 (4 pp. + allegato) | 1989 | SL-P1200X | Balance Out PCB (K) modificata da suffisso Q: resistenze, schema e PCB vecchio/nuovo; foglio "Grounding the unit" | solo P1200X |
| TI_UK_1987-05_SL-P520_P720_spindle | Panasonic UK Technical Information | 05/1987 | SL-P520, SL-P720 | stesso guasto spindle, kit SZZP1090C, 4 diodi in serie; ref diversi | modello correlato |

Pagine scartate: bianche (scan0073 p.6, scan0074 pp.2 e 4, scan0075 pp.2, 4, 6) e copie identiche (scan0075 pp.3 e 5).
