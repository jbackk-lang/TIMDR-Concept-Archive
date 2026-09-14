# AstroCycles‑TIMDR — Harmonic Generator API

This document provides a detailed description of the harmonic generation
algorithms used in the TIMDR framework. These functions define the
geometric structure of harmonic layers and form the foundation of the
model.

---

# 1. Module Overview

**Module:** `algorithms.harmonic_generator`

This module implements:

- harmonic layer construction  
- multi‑layer harmonic structure generation  
- prime‑like node expansion  
- geometric interpretation of harmonic density  

The harmonic generator is one of the core components of the TIMDR model.

---

# 2. Function Reference

## 2.1 `generate_harmonic_layer(level: int) -> list[int]`

Generates a single harmonic layer.

### **Description**
A harmonic layer is defined as a sequence of node indices representing
resonance points. Higher levels contain more nodes, following a
prime‑like geometric expansion.

### **Parameters**
- `level` — harmonic level (1 = base layer)

### **Returns**
- list of integer node indices

### **Example**
```python
generate_harmonic_layer(1)
# → [0, 1]

generate_harmonic_layer(3)
# → [0, 1, 2, 3, 4, 5]
