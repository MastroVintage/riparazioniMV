# Perdita audio toccando i condensatori di filtro

**Data:** 2026-10-01
**Categoria:** Riparazioni / Audio

## Sintomo

Durante il funzionamento, toccando la carcassa metallica di un condensatore elettrolitico, il dispositivo audio smette di suonare.

Condensatori coinvolti: due elettrolitici polarizzati, **4700 µF + 1000 µF in parallelo**, usati come **filtro di alimentazione** dopo il ponte raddrizzatore.

## Domande e risposte

### D: Il dispositivo smette di suonare se si tocca la carcassa di un elettrolitico. Quali sono le cause?

Il primo passo è distinguere tra causa meccanica ed elettrica.

**Test discriminante:** toccare lo stesso condensatore con un bastoncino isolante (plastica, legno, cacciavite da taratura) invece che con il dito.

- Smette di suonare anche con il bastoncino → guasto **meccanico**.
- Smette solo con il dito → guasto **elettrico**: il corpo inietta capacità, rumore di rete o una scarica elettrostatica.

**Cause meccaniche** (il movimento apre o chiude un contatto intermittente):

- saldatura fredda o crepata sui reofori o sui componenti vicini (causa più comune);
- pista incrinata o piazzola sollevata;
- contatto interno intermittente nel condensatore, con reoforo corroso o trafilamento di elettrolita.

Per confermare: spray congelante o phon nella zona, oppure flettere leggermente la scheda.

**Cause elettriche.** La carcassa in alluminio è quasi sempre collegata al terminale negativo.

- Il negativo non è a massa (ramo negativo di un'alimentazione duale, bootstrap, nodo ad alta impedenza).
- Interviene la protezione DC-offset o un mute. Indizio: clic del relè.
- Reset di un microcontrollore o di un PLL.
- Oscillazione in RF dello stadio: controllare l'uscita con l'oscilloscopio.
- Massa flottante: misurare la tensione AC e DC tra carcassa, telaio e terra di rete.

### D: Due elettrolitici da 4700 µF e 1000 µF in parallelo, che capacità danno?

In parallelo le capacità si sommano: **4700 + 1000 = 5700 µF**.

- **Tensione di lavoro:** vale quella del condensatore con la tensione nominale più bassa.
- **ESR:** si riduce, perché è il parallelo delle due ESR. Il condensatore più piccolo lavora meglio alle frequenze più alte.
- **Polarità:** entrambi con il + sullo stesso nodo.

### D: I condensatori sono di filtro per l'alternata raddrizzata. Cosa cambia?

La causa più probabile diventa **meccanica**.

- Il filtro di alimentazione è un nodo a bassissima impedenza: la capacità del dito (qualche centinaio di pF) è trascurabile rispetto a 5700 µF.
- I condensatori di filtro sono il punto classico delle saldature crepate: sono pesanti, subiscono vibrazioni e cicli termici dovuti alla corrente di ripple.
- Il loro negativo è spesso il **punto di massa a stella**. Se quella saldatura è intermittente si perde il riferimento di massa, e interviene la protezione o si azzera l'uscita.

**Nota:** con un'alimentazione duale (±V), il condensatore del ramo negativo ha il + a massa e la **carcassa a −V**. È normale, ma va tenuto presente durante le misure.

## Diagnosi

Probabile **saldatura crepata o intermittente** sui condensatori di filtro, sul ponte raddrizzatore o sulle connessioni di massa che partono dal loro negativo. Il tocco muove il componente, interrompe l'alimentazione o la massa e fa intervenire la protezione o il mute.

## Procedura di verifica

1. **Spegnere e scaricare i condensatori** con una resistenza da qualche centinaio di Ω e 5 W. Verificare con il tester che la tensione sia a 0 V.
2. **Ispezionare le saldature con la lente**, cercando l'anello di crepa attorno al reoforo:
   - reofori di entrambi i condensatori;
   - ponte raddrizzatore;
   - fili o terminali del secondario del trasformatore;
   - piste di massa dal negativo dei condensatori.
3. **Rifare le saldature** di tutta la zona aggiungendo stagno fresco.
4. **Misurare i condensatori fuori circuito** (capacità ed ESR). Se sono vecchi, gonfi o con tracce di elettrolita, sostituirli:
   - stessa capacità;
   - tensione uguale o superiore;
   - classe 105 °C, preferibilmente a basso ESR.
5. **Prova di conferma con l'apparecchio acceso:** osservare all'oscilloscopio la tensione continua sui condensatori mentre si muovono con un bastoncino isolante. Un ripple ampio o un buco nella tensione nel momento in cui il suono si interrompe individua il punto guasto.
6. Verificare se, quando il suono si interrompe, si sente il **clic di un relè**. Se sì, interviene la protezione per un buco di alimentazione o per la perdita di massa, e questo conferma la pista meccanica.
