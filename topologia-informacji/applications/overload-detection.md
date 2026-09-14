# Zastosowanie: Wykrywanie przeciążenia (Overload Detection)

## Cel
Użyć ρ, ρ_krytyczne, N, S↺ do wykrywania:
- kiedy system (człowiek / AI) jest przeciążony,
- kiedy filtrów jest za dużo,
- kiedy trzeba odpuścić.

## Kluczowe pojęcia

- ρ — gęstość informacyjna.
- ρ_krytyczne — próg przeciążenia.
- N — napięcie.
- S↻ — stabilny cykl.
- S↺ — pęknięcie / rozpad.

## Procedura

1. **Pomiar ρ (jakościowy)**
   - Ile wątków naraz?
   - Ile pojęć w jednym kroku?
   - Ile filtrów aktywnych?

2. **Objawy wysokiego ρ**
   - zmęczenie,
   - chaos,
   - brak domknięcia,
   - poczucie „za dużo naraz”.

3. **Próg ρ_krytyczne**
   - subiektywny, ale:
     - gdy pojawia się S↺ (rozpad struktury),
     - gdy decyzje stają się losowe.

4. **Redukcja ρ**
   - wyłączenie filtrów (jak zrobiliśmy),
   - uproszczenie języka,
   - rozdzielenie wątków,
   - pauza (czas jako operator T o małej Λ).

5. **Powrót do S↻**
   - mniej filtrów,
   - mniej warstw,
   - mniej napięcia N.

## Przykład

- Aktywny filtr 2.1 + próba dodania 2.2 → ρ blisko ρ_krytyczne.
- Wyłączenie filtra 2.1 (bez kasowania) → spadek ρ, powrót do S↻.
