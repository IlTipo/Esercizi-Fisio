# Passi di Bruno

Gioco riabilitativo per l'arto inferiore, pensato per un paziente (Bruno) che fatica a muovere l'anca, il ginocchio e la caviglia separatamente (deficit di controllo motorio selettivo, sinergie) e a camminare con un passo regolare. L'idea si ispira ai tavoli interattivi come Tyromotion Myro: grandi bersagli da toccare, feedback immediato e report delle sedute.

## Come si usa

Apri `index.html` in Chrome o Edge, sul PC, sul tablet o su uno schermo touch. Non serve installare niente.

- **Senza fotocamera** tutti i giochi funzionano col tocco, con i tasti o con il terapista che segna le ripetizioni.
- **Con la webcam** (pulsante "Attiva fotocamera") il gioco stima in 2D gli angoli di anca, ginocchio e caviglia con MediaPipe Pose. La prima volta serve internet per scaricare il modello.

Nel menu si impostano il nome del paziente, l'arto da allenare (destro o sinistro) e la voce guida in italiano.

## I giochi

| Gioco | Obiettivo clinico | Come funziona |
|---|---|---|
| **Piano con la gamba** (gioco musicale) | Controllo graduato e mantenimento di una posizione articolare, timing | Le note scendono in 3-5 corsie come in un gioco di tasti di pianoforte; ogni corsia è una posizione della gamba (mostrata da una piccola sagoma). Il cursore verde si muove con l'angolo dell'articolazione (fotocamera) oppure col dito o con i tasti. Se la gamba è nella corsia giusta quando la nota arriva, la nota suona; le note lunghe vanno tenute. Brani: Inno alla gioia, Fra Martino, Brilla brilla stellina, oppure allenamento libero con salti piccoli. Movimenti: ginocchio da seduto, ginocchio in piedi, caviglia, anca. La calibrazione (riposo e massimo comodo) adatta le corsie al movimento del giorno. Con la fotocamera la nota vale metà se le articolazioni che devono restare ferme si muovono. Punti, combo, stelle e record per brano. |
| **Mappa della gamba** | Schema corporeo, discriminazione dei segmenti, cinestesia | *Tocca la parte*: tocca coscia, gamba, piede, anca, ginocchio o caviglia su una gamba che cambia posizione a ogni prova. *Quale si muove?*: oscilla una sola articolazione; a ogni risposta giusta il movimento diventa più piccolo e il gioco stima la soglia di percezione. *Occhi chiusi*: il terapista muove passivamente l'articolazione indicata e segna se il paziente ha riconosciuto articolazione e direzione. |
| **Muovi solo…** | Controllo motorio selettivo, uscita dalle sinergie | 4 esercizi: *Calcio al pallone* (estensione del ginocchio da seduto), *Punta al cielo* (dorsiflessione), *Tallone al sedere* (flessione del ginocchio con anca estesa), *Gamba tesa avanti* (flessione d'anca a ginocchio esteso). Una sagoma tratteggiata mostra il bersaglio. Le articolazioni che devono restare ferme hanno un anello verde o rosso. Una ripetizione è **pulita** quando raggiunge l'obiettivo, lo tiene per 1 secondo e non sposta le altre articolazioni oltre la tolleranza. Ampiezza, tolleranza e numero di ripetizioni sono regolabili. |
| **Passo a ritmo** | Cammino con cue ritmico uditivo (RAS), timing, simmetria | Il metronomo dà un suono diverso per il piede sinistro e per il destro, e le impronte scorrono verso la linea "ADESSO". I passi si registrano con i pulsanti, con i tasti ← → o A/L (anche da pedaliera USB), oppure con la webcam (marcia sul posto, di fronte). Il gioco misura i passi a tempo, l'errore medio in ms per lato, il tempo del passo e l'asimmetria. |
| **Ritrova la posizione** | Propriocezione: senso di posizione articolare (JPS) | Il terapista posiziona l'articolazione; il paziente a occhi chiusi torna alla partenza e poi la riproduce. Gli angoli si inseriscono da goniometro o si misurano con la webcam. Il gioco calcola l'errore assoluto medio e l'errore costante, cioè se il paziente tende a superare o a non arrivare al bersaglio. |

Il **Diario delle sedute** salva i risultati nel browser del dispositivo (localStorage) e li copia in formato CSV, da incollare in Excel o in cartella clinica.

## Note cliniche e limiti

- Usare sempre sotto la supervisione del fisioterapista, con un appoggio stabile per gli esercizi in piedi.
- Le misure da webcam sono stime 2D: la gamba deve essere di profilo e tutta nell'inquadratura. Servono a seguire l'andamento, non sostituiscono il goniometro.
- La webcam funziona solo aprendo il file direttamente nel browser, non dentro pagine incorporate che bloccano la fotocamera.

## Struttura

- `src/body.html`: sorgente del gioco (HTML, CSS e JS in un solo file)
- `build.py`: genera `index.html` (pagina completa) da `src/body.html`
- `index.html`: il gioco pronto da aprire
