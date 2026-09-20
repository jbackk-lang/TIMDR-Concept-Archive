# CIA TIMDER FILTER — Complete Guide
## Compression-Interpretation-Analysis for Psychology

---

## 📖 Spis Treści

1. [Przegląd](#przegląd)
2. [Trzy Etapy CIA](#trzy-etapy-cia)
3. [Mapowanie do TIMDR](#mapowanie-do-timdr)
4. [Praktyczne Zastosowania](#praktyczne-zastosowania)
5. [Przepływ Danych](#przepływ-danych)
6. [Przykłady](#przykłady)

---

## Przegląd

**CIA Filter** to warstwa przetwarzania psychicznych sygnałów TIMDR, która:

- **C (Compression)** — usuwa szum, wyodrębnia esencję
- **I (Interpretation)** — zmienia perspektywę, znajduje znaczenie
- **A (Analysis)** — diagnozuje, prognozuje, przepisuje działania

CIA filtr **redukuje chaos psychiczny do struktury**, dokładnie jak Λ–τ–ρ redukuje chaos fizyczny.

---

## Trzy Etapy CIA

### 1️⃣ COMPRESSION (C) — Zmniejszanie Szumu

```
RAW SIGNAL                    COMPRESSED SIGNAL
┌─────────────────────┐      ┌──────────────┐
│ intensity: 0.75     │      │ core: 0.62   │
│ noise: 0.35         │  →   │ coherence: 0.85
│ chaos: HIGH         │      │ noise removed: 32%
│ direction: ?        │      │ direction: CLEAR
└─────────────────────┘      └──────────────┘
```

**Co się dzieje**:
- Szacujemy szum w sygnale
- Odejmujemy szum od intensywności
- Policzamy **coherence** (czystość struktury)
- Ekstraktujemy **compression ratio** (ile przefiltrowano)

**Równanie**:
```
core_intensity = intensity - noise
coherence = 1.0 - noise + compression_factor
compression_ratio = noise / intensity
```

**Przykład — Lęk z zamieszaniem**:
```python
filter.compress(
    signal_name="anxiety",
    intensity=0.75,        # czuję się oparty
    modality="uncertainty", # ale nie wiem czego
    noise_estimate=0.35    # wiele sprzecznych sygnałów
)
→ CompressedSignal(
    core_intensity=0.62,   # czysty lęk
    coherence=0.85,        # struktura wyraźna
    compression_ratio=0.32 # usunęliśmy 32% szumu
)
```

---

### 2️⃣ INTERPRETATION (I) — Zmiana Perspektywy

Ta sama kompresja ma **różne znaczenia** w różnych schematach:

```
COMPRESSED: "uncertainty" + intensity 0.75

EMOTIONAL SCHEME:
  → "anxiety"
  → valence: -0.6 (negatywna)
  → action: "pause"

COGNITIVE SCHEME:
  → "question"
  → valence: -0.2 (neutralna)
  → action: "investigate"

GROWTH SCHEME:
  → "discovery"
  → valence: +0.5 (pozytywna!)
  → action: "explore"
```

**Schematy Interpretacji**:
- `LITERAL` — dosłownie
- `EMOTIONAL` — przez emocje
- `COGNITIVE` — przez myśl
- `SOCIAL` — przez relacje
- `SURVIVAL` — przez przetrwanie
- `GROWTH` — przez rozwój

**Równanie**:
```
meaning = meaning_map[(direction, scheme)]
valence = emotional_value(meaning, scheme)
action_bias = determine_action(meaning)
confidence = coherence × schema_match
```

**Praktyka — reframing strachu**:
```python
# Schemat SURVIVAL: "To zagrożenie!"
→ meaning="danger", valence=-0.9, action="avoid"

# Schemat GROWTH: "To wyzwanie!"
→ meaning="opportunity", valence=+0.2, action="engage"

# Ta sama intensywność, całkowicie inne działanie
```

---

### 3️⃣ ANALYSIS (A) — Diagnoza i Predykcja

Cztery tryby analizy:

| Tryb | Pytanie | Wyjście | Przykład |
|------|---------|---------|----------|
| **DIAGNOSTIC** | Co jest nie tak? | risk_level, findings | "Wysoki lęk. Wymaga interwencji." |
| **PREDICTIVE** | Co będzie? | probability, trend | "Prawdopodobnie ucieczka (82%)" |
| **PRESCRIPTIVE** | Co robić? | recommendation, action | "Wykonaj 'explore' zamiast 'avoid'" |
| **PROGNOSTIC** | Jaka perspektywa? | outlook, long-term risk | "Perspektywa polepszająca się" |

**Równania Ryzyka**:
```
risk_level = (-valence + intensity_factor + coherence_penalty) / 2.0

gdzie:
  -valence = ujemna valence zwiększa ryzyko
  intensity_factor = intensity × 0.5
  coherence_penalty = (1.0 - coherence) × 0.3
```

---

## Mapowanie do TIMDR

### CIA ↔ Operatory TIMDR

```
TIMDR OPERATOR    CIA ETAP         REZULTAT
────────────────────────────────────────────
T(X)              Compress (C)     → core_intensity, direction
I(X)              Compress (C)     → coherence, signal purity
M_p(X)            Interpret (I)    → meaning, valence, action_bias
I_t(X)            All stages       → dynamic evolution
R(X)              Compress (C)     → coherence (rezonans z polem)
FUND(X)           Analysis (A)     → risk_level → status
E(S)              Analysis (A)     → recommendation (emergencja)
```

### Przepływ CIA w TIMDR

```
PsychologicalObject
  ↓
compress(I, noise)  [operator C → redukcja szumu]
  ↓
CompressedSignal (czysty skręt Λ–τ–ρ)
  ↓
interpret(scheme)   [operator I → interpretacja M]
  ↓
InterpretedSignal (znaczenie + action)
  ↓
analyze(mode)       [operatory R, FUND, E → emergencja]
  ↓
AnalysisResult (rekomendacja behawioralna)
```

---

## Praktyczne Zastosowania

### 1. Diagnostyka Psychiczna

```python
filter_cia = CIAFilter()

result = filter_cia.process(
    signal_name="panic_attack",
    intensity=0.95,
    modality="threat",
    noise_estimate=0.40,  # dużo zamieszania sensorycznego
    interpretation_scheme=InterpretationScheme.SURVIVAL,
    analysis_mode=AnalysisMode.DIAGNOSTIC
)

if result.risk_level > 0.8:
    print("🚨 KRYZYS: Wymaga natychmiastowej interwencji")
    # → Telefon do kryzysowego
elif result.risk_level > 0.5:
    print("⚠️  PODWYŻSZONY: Monitoruj i wspomagaj")
    # → Sesja terapeutyczna
else:
    print("✓ OK: Normalny poziom lęku")
```

**Output**:
```
DIAGNOSTYKA PANIKI:
- Core signal: 0.85 (oczyszczony)
- Coherence: 0.65 (chaotyczne)
- Meaning: "mortal_danger"
- Valence: -0.95 (bardzo negatywna)
- Risk: 85%
→ Recommendation: "🚨 KRYZYS: Wymaga natychmiastowej interwencji"
```

---

### 2. Reframing Behawiorów

```python
# PROBLEM: Osoba unika nowych sytuacji
fear = filter_cia.process(
    signal_name="social_anxiety",
    intensity=0.70,
    modality="uncertainty",
    noise_estimate=0.25,
    interpretation_scheme=InterpretationScheme.SURVIVAL,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"Current: {fear.recommendation}")
# → "Unikaj nowych sytuacji (samoochrona)"

# INTERWENCJA: Zmień schemat na GROWTH
growth = filter_cia.process(
    signal_name="social_anxiety",
    intensity=0.70,
    modality="uncertainty",
    noise_estimate=0.25,
    interpretation_scheme=InterpretationScheme.GROWTH,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"After reframing: {growth.recommendation}")
# → "Eksploruj nowe sytuacje (rozwój umiejętności)"

# Ta sama intensywność, całkowicie inne działanie!
```

---

### 3. Konflikt Decyzyjny

```python
# Pacjent ma konflikt: chce pracy (opportunity) ale boi się porażki (threat)

opportunity = filter_cia.process(
    signal_name="job_opportunity",
    intensity=0.80,
    modality="opportunity",
    noise_estimate=0.10,
    interpretation_scheme=InterpretationScheme.GROWTH,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

threat = filter_cia.process(
    signal_name="failure_fear",
    intensity=0.70,
    modality="threat",
    noise_estimate=0.20,
    interpretation_scheme=InterpretationScheme.SURVIVAL,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"Opportunity: {opportunity.recommendation}")
# → "Rozwój: Wykonaj 'engage'"

print(f"Threat: {threat.recommendation}")
# → "Ochrona: Wykonaj 'avoid'")

# ROZWIĄZANIE: Fuzja schematów
integration = filter_cia.process(
    signal_name="career_decision",
    intensity=0.75,
    modality="uncertainty",
    noise_estimate=0.30,
    interpretation_scheme=InterpretationScheme.COGNITIVE,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"Resolution: {integration.recommendation}")
# → "Analiza: Wykonaj 'investigate' zamiast 'pause'"
# → Szansa na rozsądne rozważenie obu perspektyw
```

---

## Przepływ Danych

### Pojedynczy Sygnał

```
Raw Psychological Signal
    ↓
CIAFilter.process()
    ├─ Compression Stage (C)
    │  ├─ Estimate noise
    │  ├─ Remove noise from signal
    │  └─ Calculate coherence
    │  → CompressedSignal
    │
    ├─ Interpretation Stage (I)
    │  ├─ Apply scheme (EMOTIONAL/COGNITIVE/GROWTH/...)
    │  ├─ Map to meaning
    │  ├─ Calculate valence
    │  └─ Determine action bias
    │  → InterpretedSignal
    │
    └─ Analysis Stage (A)
       ├─ Assess risk
       ├─ Extract findings
       ├─ Formulate recommendation
       └─ Estimate probability
       → AnalysisResult
           ├─ recommendation: "Execute 'explore' instead of 'avoid'"
           ├─ risk_level: 0.35
           ├─ probability: 0.82
           └─ mode: PRESCRIPTIVE
```

### Wielopoziomowe Pole Psychiczne

```
PsychologicalField
├─ Emotion 1: anger (intensity 0.85)
├─ Emotion 2: fear (intensity 0.70)
├─ Thought 1: "I'm failing" (intensity 0.60)
└─ Thought 2: "I can learn" (intensity 0.65)
    ↓
For each object: CIAFilter.process()
    ↓
CIAResults[4]
    ├─ anger → "fight_or_flight" (risk: 0.80)
    ├─ fear → "avoid" (risk: 0.75)
    ├─ negative_thought → "withdraw" (risk: 0.65)
    └─ positive_thought → "explore" (risk: 0.25)
    ↓
Aggregate field_state = weighted_average(results)
    ↓
Emergent_behavior = consensus(all emergences)
    → "cautious_exploration" (weighted from conflicts)
```

---

## Przykłady

### Przykład 1: Anksiozność

```python
from cia_filter import CIAFilter, InterpretationScheme, AnalysisMode, CompressionLevel

filter = CIAFilter(compression_level=CompressionLevel.COMPRESSED)

# Surowy sygnał
print("RAW: Intensity 0.75, feels overwhelmed, uncertain why")

# Przetwarzanie
result = filter.process(
    signal_name="anxiety",
    intensity=0.75,
    modality="uncertainty",
    noise_estimate=0.35,
    interpretation_scheme=InterpretationScheme.COGNITIVE,
    analysis_mode=AnalysisMode.DIAGNOSTIC
)

print(f"\nCOMPRESSED:")
print(f"  Core: {result.interpreted.compressed.core_intensity:.2f}")
print(f"  Coherence: {result.interpreted.compressed.coherence:.2f}")

print(f"\nINTERPRETED:")
print(f"  Meaning: {result.interpreted.meaning}")
print(f"  Valence: {result.interpreted.valence:+.2f}")

print(f"\nANALYSIS:")
print(f"  Risk: {result.risk_level:.1%}")
print(f"  Recommendation: {result.recommendation}")
```

**Output**:
```
RAW: Intensity 0.75, feels overwhelmed, uncertain why

COMPRESSED:
  Core: 0.62
  Coherence: 0.85

INTERPRETED:
  Meaning: question
  Valence: -0.20

ANALYSIS:
  Risk: 32%
  Recommendation: ⚠️  DIAGNOZA: Umiarkowany question. Monitoruj sytuację.
```

---

### Przykład 2: Społeczny Lęk (Social Anxiety)

```python
# Przed terapią
before = filter.process(
    signal_name="social_interaction",
    intensity=0.80,
    modality="threat",
    noise_estimate=0.20,
    interpretation_scheme=InterpretationScheme.SURVIVAL,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"BEFORE: {before.recommendation}")
# → "💊 PRZEPIS: Wykonaj 'avoid' zamiast 'approach'. Confidence: 72%"

# Po reframingu (terapia poznawczo-behawioralna)
after = filter.process(
    signal_name="social_interaction",
    intensity=0.75,  # trochę obniżona
    modality="uncertainty",  # zmieniona perspektywa
    noise_estimate=0.15,  # czystsza
    interpretation_scheme=InterpretationScheme.GROWTH,
    analysis_mode=AnalysisMode.PRESCRIPTIVE
)

print(f"AFTER: {after.recommendation}")
# → "💊 PRZEPIS: Wykonaj 'explore' zamiast 'settle'. Confidence: 78%"
```

---

### Przykład 3: Zespołowe Przetwarzanie

```python
# Wielowarstwowy konflikt
signals = {
    "duty": ("threat", 0.70),      # "muszę się uczyć"
    "exhaustion": ("loss", 0.65),  # "jestem zmęczony"
    "possibility": ("opportunity", 0.55),  # "ale mogę się rozwijać"
}

results = {}
for name, (modality, intensity) in signals.items():
    results[name] = filter.process(
        signal_name=name,
        intensity=intensity,
        modality=modality,
        interpretation_scheme=InterpretationScheme.GROWTH,
        analysis_mode=AnalysisMode.PRESCRIPTIVE
    )

print("PSYCHICZNE POCZUCIE WEWNĘTRZNE:")
for name, result in results.items():
    print(f"  {name}: {result.interpreted.meaning} "
          f"(risk: {result.risk_level:.0%})")

# Agreguj na rekomendację
recs = [r.recommendation for r in results.values()]
print("\nKOLEKTYWNA DECYZJA:")
print("  Lepiej: Odpoczynkowa aktywność nauki (niska presja, wysoki wzrost)")
```

---

## Integracja z FAI Stack

```
PsychologicalField (psychology.py)
    ↓
CIAFilter (cia_filter.py)  ← NEW!
    ├─ Compression: cleanse signals
    ├─ Interpretation: find meaning
    └─ Analysis: generate action
    ↓
FundamentalExecutor (fundamental_executor.py)
    ├─ Execute(X) operatory TIMDR
    ├─ Generate emergences
    └─ Update field_strength
    ↓
Behavior / Decision
```

---

## Podsumowanie CIA

CIA Filter to **uniwersalny procesor psychiczny**:

✅ **Compression** — redukuje chaos do esencji  
✅ **Interpretation** — znajduje znaczenie  
✅ **Analysis** — generuje działania  

**Wynik**: Chaotyczne sygnały psychiczne → Jasne, działalne rekomendacje

---

**Status**: v3.0 — CIA Filter Integration Complete ✅
