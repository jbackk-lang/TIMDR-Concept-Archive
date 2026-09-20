# API — fundamental‑ai‑model

This document describes the minimal reference API of the fundamental‑ai‑model.

---

## Orientation

**Module:** `src/orientation.py`  
**Class:** `Orientation`

### Methods

- **flip(o: int) -> int**  
  Flips orientation.

  - Input: `o ∈ {+1, −1}`  
  - Output: `−o`

---

## Horizon

**Module:** `src/horizon.py`  
**Class:** `Horizon`

### Methods

- **hide(x) -> None**  
  Moves information behind the horizon.

- **reveal() -> list**  
  Returns all hidden elements.

---

## Chain

**Module:** `src/chain.py`  
**Class:** `Chain`

### Constructor

- **Chain(states: list)**  
  Creates a chain of dependent states.

### Methods

- **valid() -> bool**  
  Returns `True` if all states are valid (truthy).

---

## Resonance

**Module:** `src/resonance.py`  
**Class:** `Resonance`

### Methods

- **align(t1, t2) -> bool**  
  Returns `True` if temporal states align (`t1 == t2`).

---

## Emergence

**Module:** `src/emergence.py`  
**Class:** `Emergence`

### Methods

- **form(resonance_ok: bool) -> str | None**  
  Returns `"E"` if resonance is valid, otherwise `None`.

---

## Pipeline

**Module:** `src/pipeline.py`  
**Function:** `pipeline(signal: int) -> str | None`

### Description

Runs the full minimal pipeline:

1. Orientation flip twice  
2. Chain validation  
3. Resonance alignment  
4. Emergence formation

Returns `"E"` on success, `None` on failure.
