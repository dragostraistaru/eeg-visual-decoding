# EEG Visual Decoding

Proiect de echipă despre reconstrucția aproximativă a conținutului vizual perceput de utilizator pornind de la semnale EEG. Soluția propusă urmărește un pipeline incremental:

`EEG input -> preprocesare -> feature extraction -> clasificare / retrieval -> rezultat final`

În etapa finală, dacă modelul de retrieval funcționează bine, poate fi adăugat și un pas de generare care pornește de la cea mai apropiată imagine găsită, nu de la zero.

## Echipa

- Nume membru 1: `de completat`
- Nume membru 2: `de completat`
- Nume membru 3: `de completat`
- Nume membru 4: `de completat`

## Problema abordată

Semnalele EEG conțin informații despre modul în care creierul răspunde la stimuli vizuali. Proiectul propune un sistem inteligent care primește ca input un semnal EEG asociat unui stimul și produce un output aproximativ sub formă de:

- categorie / etichetă,
- cea mai apropiată imagine din dataset,
- sau, în extensie, o variantă generată asemănătoare imaginii recuperate.

Scopul este să demonstrăm că un agent AI poate interpreta instrucțiuni, poate folosi instrumente software și poate produce un rezultat relevant pe baza datelor EEG.

## Obiectiv

Obiectivul principal al proiectului este să ajungem la o soluție robustă de tip:

1. încărcare și preprocesare EEG,
2. extragere de caracteristici,
3. clasificare sau retrieval,
4. evaluare a rezultatelor,
5. demo interactiv pentru prezentare.

Extensia opțională este o etapă de generare care pornește din rezultatul retrieval-ului.

## Tip de AI folosit

Proiectul combină mai multe componente de AI:

- deep learning pentru procesare EEG,
- CNN / EEGNet pentru clasificare,
- embedding-based retrieval,
- similarity learning,
- posibil generare asistată de un model de tip diffusion sau un modul similar, dacă etapa de extensie este realizată.

## Dataset-uri vizate

Pentru varianta EEG -> imagine:

- THINGS-EEG
- THINGS-EEG2
- EEG-ImageNet

## Pipeline propus

```text
EEG Signal
	↓
Preprocessing
	↓
Feature Extraction
	↓
Classification / Retrieval
	↓
Top-k Images
	↓
(Optional) Image Generation
```

Fluxul de mai sus reprezintă varianta de bază a proiectului. Obiectivul principal este să ajungem la clasificare sau retrieval, iar generarea rămâne o extensie peste rezultatul găsit.

## Evaluare și KPI-uri

Vom urmări indicatori precum:

- accuracy,
- top-1 / top-5 accuracy,
- cosine similarity între embeddings,
- timp de inferență,
- pentru imagine: similaritate vizuală și calitatea reconstrucției.

## Modul de interacțiune

Demo-ul final va fi o interfață simplă, recomandat în **Streamlit**, care va permite:

- selectarea sau încărcarea unui semnal EEG,
- rularea pipeline-ului,
- afișarea rezultatului prezis,
- afișarea top-k candidați sau a imaginii recuperate,
- afișarea scorurilor de evaluare.

## Structura proiectului

```text
proiect-eeg/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_explorare_date.ipynb
│   ├── 02_preprocesare.ipynb
│   ├── 03_clasificare.ipynb
│   ├── 04_retrieval.ipynb
│   └── 05_generare.ipynb
│
├── src/
│   ├── preprocessing/
│   │   ├── load_data.py
│   │   ├── filter.py
│   │   └── normalize.py
│   │
│   ├── features/
│   │   ├── eeg_features.py
│   │   └── spectrogram.py
│   │
│   ├── models/
│   │   ├── eegnet.py
│   │   ├── classifier.py
│   │   ├── retriever.py
│   │   └── generator.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   └── visualize_results.py
│   │
│   └── utils/
│       └── helpers.py
│
├── app/
│   └── streamlit_app.py
│
├── outputs/
│   ├── figures/
│   ├── predictions/
│   └── generated_images/
│
├── saved_models/
├── requirements.txt
├── .gitignore
└── README.md
```

## Cum lucrăm în practică

- în notebook-uri facem explorarea datelor, testarea preprocesării și primele experimente;
- în `src/` mutăm codul stabil și reutilizabil;
- în `app/` construim demo-ul final;
- în `outputs/` salvăm grafice, predicții și rezultate;
- în `saved_models/` păstrăm modelele antrenate.

## Etape de livrare

### Etapa 1 - Definirea problemei și analiza datelor de intrare

- alegerea dataset-ului;
- înțelegerea semnalelor EEG;
- preprocesare de bază;
- primele observații și grafice.

### Etapa 2 - Dezvoltarea modelului și evaluarea performanței

- feature extraction;
- model de clasificare sau retrieval;
- metrici de evaluare;
- comparații între variante.

### Etapa 3 - Îmbunătățiri

- top-k retrieval mai bun;
- model mai performant;
- integrare generare peste rezultat;
- optimizări de timp și calitate.

## Impact și SDG-uri

Proiectul se poate lega foarte bine de:

- **SDG 3** - Sănătate și bunăstare, prin aplicații pentru persoane cu dizabilități;
- **SDG 9** - Industrie, inovație și infrastructură, prin dezvoltarea unor metode AI aplicate;
- **SDG 10** - Reducerea inegalităților, prin sprijinirea comunicării asistive.

## Bibliografie și resurse utile

- MNE-Python: https://github.com/mne-tools/mne-python
- Braindecode: https://github.com/braindecode/braindecode
- ARL EEG Models: https://github.com/vlawhern/arl-eegmodels
- EEG-Conformer: https://github.com/eeyhsong/EEG-Conformer
- EEG Visual Classification: https://github.com/perceivelab/eeg_visual_classification
- EEG2Image: https://github.com/prajwalsingh/EEG2Image
## Cum rulăm proiectul

1. Creăm mediul virtual:
	```powershell
	python -m venv .venv
	```
2. Activăm mediul în PowerShell:
	```powershell
	.\.venv\Scripts\Activate.ps1
	```
3. Instalăm dependențele:
	```powershell
	pip install -r requirements.txt
	```
4. Pornim notebook-urile sau aplicația Streamlit, în funcție de etapa proiectului.

## Note

- Structura de mai sus este gândită pentru un proiect de echipă și pentru livrările intermediare cerute la laborator.
- Dacă dataset-ul ales și resursele disponibile o permit, pasul de generare poate fi adăugat după retrieval, nu neapărat din prima.
