# Zastosowanie: Projektowanie systemów (System Design)

## Cel
Użyć topologii informacji do:
- projektowania stabilnych systemów,
- wykrywania punktów pęknięcia,
- optymalizacji przepływu informacji.

## Jednostki
- I — sygnał wejściowy,
- S — stan systemu,
- T — transformacja,
- Tw — lokalna zmiana,
- ΔS — różnica stanów,
- ρ — obciążenie systemu,
- φ — pętla kontroli.

## Procedura

1. **Wejście jako I**
   - Każdy sygnał = informacja.

2. **Stan systemu jako S**
   - S reprezentuje aktualną konfigurację.

3. **Transformacje**
   - T = zmiany globalne,
   - Tw = zmiany lokalne.

4. **ΔS**
   - ΔS duże → ryzyko niestabilności.

5. **ρ**
   - Zbyt duże obciążenie → ρ > ρ_krytyczne → S↺.

6. **φ**
   - Pętla kontroli stabilizuje system.

7. **Projekt stabilny**
   - S↻, gdy:
     - ΔS kontrolowane,
     - ρ niskie,
     - φ działa regularnie.
