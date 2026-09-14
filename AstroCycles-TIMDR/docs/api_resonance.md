# AstroCycles‑TIMDR — Resonance Detector API

This document provides a detailed description of the resonance detection
algorithms used in the TIMDR framework. These functions define the dynamic
behavior of phase progression and resonance events.

---

# 1. Module Overview

**Module:** `algorithms.resonance_detector`

This module implements:

- resonance threshold detection  
- phase progression with wrap‑around  
- cycle simulation  
- resonance event extraction  

It forms the **dynamic component** of the TIMDR model.

---

# 2. Function Reference

## 2.1 `detect_resonance(phase: float) -> bool`

Determines whether a given phase value triggers a resonance event.

### **Description**
A resonance occurs when the phase exceeds a predefined threshold.
This threshold represents a geometric transition point in the harmonic
structure.

### **Parameters**
- `phase` — normalized phase value in the range `[0.0, 1.0]`

### **Returns**
- `True` if resonance occurs  
- `False` otherwise

### **Example**
```python
detect_resonance(0.5)  # → False
detect_resonance(0.9)  # → True
