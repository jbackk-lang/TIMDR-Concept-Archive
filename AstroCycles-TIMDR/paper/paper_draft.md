paper/paper_draft.md
# Geometric Harmonic Model of Astrological Cycles  
### Based on the TIMDR Framework  
**Author:** Jacek  
**Version:** Preprint Draft (2026)

---

# Abstract
This paper presents a geometric model for representing astrological cycles
using the TIMDR framework. The model introduces harmonic layers, resonance
nodes, and phase‑shift thresholds as a unified structure for analyzing
multi‑level periodicity. The approach integrates astronomical cycle data,
harmonic aspect geometry, and algorithmic resonance detection.

---

# 1. Introduction
Astrological cycles can be interpreted as geometric structures composed of
harmonic layers and resonance transitions. The TIMDR framework provides a
minimal set of assumptions for modeling these structures mathematically.

This paper proposes:
- a harmonic layer generator,
- a resonance detection operator,
- a unified pipeline for cycle analysis,
- and a geometric interpretation of multi‑level periodicity.

---

# 2. Background

## 2.1 Harmonic Systems
Harmonic systems consist of discrete layers, each defined by a number of
resonance nodes. Higher layers exhibit increased node density and shorter
phase intervals.

## 2.2 TIMDR Framework
The TIMDR model assumes:
- geometric phase progression,
- threshold‑based resonance events,
- and prime‑like harmonic growth.

---

# 3. Data Sources

## 3.1 Planetary Cycles Dataset
File: `data/planetary_cycles.json`  
Contains synodic and orbital periods for major planets.

## 3.2 Harmonic Aspect Angles
File: `data/harmonic_aspects.json`  
Defines geometric aspect ratios and angular separations.

---

# 4. Methods

## 4.1 Harmonic Layer Generation
Algorithm: `algorithms/harmonic_generator.py`  
Generates harmonic layers using a prime‑like node expansion.

## 4.2 Resonance Detection
Algorithm: `algorithms/resonance_detector.py`  
Detects resonance events when the phase exceeds a threshold.

## 4.3 Pipeline Integration
Script: `pipeline/run_pipeline.py`  
Combines datasets and algorithms into a unified analysis flow.

---

# 5. Model Structure

## 5.1 Harmonic Layers
Harmonic layers are represented as concentric rings with increasing node
counts. Each node corresponds to a resonance point.

## 5.2 Resonance Nodes
Resonance nodes represent transition points where the system changes
harmonic state.

## 5.3 Phase Shift Geometry
Phase progression is modeled as a directional vector on the cycle ring.

---

# 6. Diagrams

## 6.1 Conceptual Diagram
See: `diagrams/harmonic_structure.md`

## 6.2 ASCII Diagram
See: `diagrams/harmonic_ascii.md`

---

# 7. Results (Preliminary)

- Harmonic structure generated for 3 layers  
- Resonance events detected in simulated cycles  
- ASCII visualization produced from pipeline output  

---

# 8. Discussion
The TIMDR model provides a minimal geometric interpretation of astrological
cycles. Preliminary results show consistent resonance patterns across
simulated cycles.

---

# 9. Future Work
- Full graphical diagrams  
- Integration with real ephemerides  
- Multi‑layer resonance mapping  
- Formal definition of the TIMDR operator  

---

# 10. Conclusion
The TIMDR framework offers a structured, geometric approach to modeling
astrological cycles. This preprint establishes the foundation for further
research and visualization.

---

# References
(To be added in the final version.)

---

# Figure 1 — ASCII Harmonic Structure (TIMDR)

This figure illustrates the conceptual harmonic layering used in the TIMDR
framework. Each layer contains resonance nodes (●) distributed according to
harmonic density.

**Interpretation:**
- Higher layers contain more nodes and shorter phase intervals  
- Lower layers represent fundamental harmonic cycles  
- Node spacing corresponds to geometric phase distance  
- This structure is used for resonance detection and cycle modeling  

---

# Figure 2 — ASCII Resonance Timeline

This figure shows the distribution of resonance events detected by the
TIMDR resonance detector during a simulated cycle of 200 steps.

Each dot (●) represents a resonance event. The horizontal axis represents
phase progression over time.


**Interpretation:**
- The timeline shows clustering of resonance events
- Gaps represent stable harmonic intervals
- Dense regions indicate harmonic interference
- This structure is used to analyze resonance density and cycle transitions




