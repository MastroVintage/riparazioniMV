# Service Bulletin A6-88-11 (ago. 1988) — SL-P1200 / SL-P1200X: massa, rimbalzo tasti, switch OPEN/CLOSE, livello RF
Fonte: Matsushita Services Company (USA). Dist: A6,88,W-903. Pagine 1-4 di 4, complete. Ref = SL-P1200.
PDF pulito: ..\DATA\SB_A6-88-11_massa_switch_RF_pulito.pdf · pagine: pages\p01-p04.png · OCR: ocr\ (p03 rumoroso: testo storto in alto, leggere l'immagine)

## Sintomi
1) "Pop" sull'uscita audio all'avvio del PLAY. 2) PLAY interrotto per errore: il pickup resta dov'e' o torna a riposo; funzionamento irregolare. 3) Nessuna risposta al comando PLAY del telecomando a filo. 4) Non legge il TOC o salta ogni tanto.
## Cause
1) Massa scorretta tra l'apparecchio e il resto dell'impianto. 2) Pannello comandi non a massa: l'elettricita' statica disturba. 3) Rimbalzo dei contatti: il tasto PLAY viene interpretato male. 4) Polvere sulla lente del pickup; switch di rilevamento OPEN/CLOSE difettoso.
## Rimedi (kit TAS8512001; il kit pulizia lente SZZP1038C e' a parte)
1) (p01-p02) Capocorda di massa sul pannello posteriore: foro da 4 mm sul lato sinistro (quote a p01; attenzione ai trucioli), dadi esagonali x2, rondella, rondella grower, controdado, metal post, etichetta "GND" sotto il capocorda.
2) (p02) Massa del pannello frontale: smontare la operation PCB (keyboard PCB) come da service manual p.17; tagliare la fascetta in "E"; spostare il filo di massa dai punti A-B ai punti C-D (vite del kit in D); rifascettare in E; togliere le manopole REPEAT e AUTO SPACE; montare la nuova piastra di massa (la sua linguetta va sotto quella esistente; piegare di 80 gradi nel verso della freccia); rimontare le manopole. Riferimento in figura: SUPD660.
3) (p03) Rimbalzo: C415 da 0.001 uF a 0.01 uF (C415 e' sulla "SOCKET PCB" sul pannello posteriore).
4A) (p03) Misurare il livello RF su TJ302: deve essere 0.7-1.2 Vp-p. Pulire la lente con il kit SZZP1038C seguendo il manuale d'uso.
4B) (p03) Controllare lo switch OPEN/CLOSE S101: tutti e tre i terminali devono fare buon contatto, altrimenti sostituirlo con l'assieme SWSD12001 (figura: terminali originali e migliorati).
- Switch migliorato dalla produzione del 10/2/1987 sull'SL-P1200 e dalla prima produzione dell'SL-P1200X. Data dal seriale: X X 7 2 1 0 X X X X = anno, mese (1-9 = gen-set, J = ott, K = nov, L = dic), giorno.
- Kit (p03): 1-B ferramenta capocorda (hex nut x2, washer, lock washer, lock nut, metal post, ground label); 2-C vite; 2-D fascetta; 2-F piastra di massa; 3 condensatore 0.01 uF; 4-B switch assembly.
4) (p04) "Grounding the unit": istruzioni di collegamento delle uscite.
   - SL-P1200X, con uscite sbilanciate e BALANCED insieme: scollegare il pin 1 di entrambi i canali BALANCED.
   - SL-P1200X, solo BALANCED: se il pin 1 e' scollegato, collegare il morsetto di massa dell'apparecchio alla massa dell'altro componente; se il pin 1 e' collegato, non serve. In ogni caso il componente collegato deve essere a massa.
   - Telecomando a filo: non collegare il pin 4 alla massa dell'impianto.
   - SL-P1200 con adattatore sbilanciato-bilanciato: non collegare il pin 1 del terminale BALANCED dal lato adattatore.

## Collegamento alla KB SL-P1200
- Confronto RF: TJ302 0.7-1.2 Vp-p (questo bollettino) contro MIN RF 0.84 Vpp per pickup SOALP1200 (Troubleshooting Guide 1986-1990, p.8, UNIVERSITY\B_...). Sotto 0.84 Vpp il pickup e' da considerare debole anche se rientra nella finestra 0.7-1.2.
- TJ302 sulla Main PCB del P1200: KB\manual\img\m34.png, sotto IC101, vicino a TJ303. Attenzione: sull'SL-P110 TJ302 e' la massa del punto RF e il segnale RF e' su TJ301 (SM_SL-P110 adj_s011). Sul P1200 il bollettino indica TJ302 come punto RF; prima della misura verificare sullo schema S4 se TJ302 e' il segnale o la massa (TJ301 non compare sul m34). C415: lista condensatori KB\manual\img\m22.png.
- Lo stesso foglio "Grounding the unit", con un'introduzione "IMPORTANT!!!" in piu', e' allegato al supplemento SL-P1200X: ..\..\SUP_AD8908221S1_SL-P1200X_balance_out\KB\pages\p05.png.
