# Figures — Layout and Specification

This document defines the structure and requirements for all figures
included in the AstroCycles‑TIMDR paper and future publications.

---

# Figure 1 — Harmonic Structure (ASCII → PDF)
**Source:** diagrams/harmonic_ascii.md  
**Purpose:** Show static geometric structure of harmonic layers  
**Final Format:** PDF vector graphic  
**Notes:**  
- Concentric rings  
- Node density increases with harmonic level  
- Should match ASCII version conceptually  

---

# Figure 2 — Resonance Timeline (ASCII → PDF)
**Source:** paper/paper_draft.md (Figure 2)  
**Purpose:** Show dynamic resonance distribution over time  
**Final Format:** PDF horizontal timeline  
**Notes:**  
- Dots represent resonance events  
- Should include axis labels  
- Optional: color-coded harmonic levels  

---

# Figure 3 — Harmonic Density Map (Planned)
**Purpose:** Visualize node density across harmonic layers  
**Format:** Heatmap or radial density plot  
**Status:** Planned  

---

# Figure 4 — Multi-Layer Resonance Map (Planned)
**Purpose:** Show resonance clustering across multiple layers  
**Format:** 2D or radial plot  
**Status:** Planned  

---

# Figure 5 — TIMDR Operator Geometry (Planned)
**Purpose:** Formal geometric interpretation of TIMDR operator  
**Format:** Vector diagram  
**Status:** Planned  

---

# General Requirements for All Figures

- Format: **PDF (vector)**  
- Resolution: infinite (no rasterization)  
- Style: geometric, minimal, scientific  
- Colors: grayscale or muted scientific palette  
- Fonts: consistent with paper  
- Export naming: `figure_X_description.pdf`  

---

# Workflow for Adding Figures

1. Create draft (ASCII or conceptual)
2. Convert to graphical form (Python, vector tool, etc.)
3. Export as PDF to `figures/`
4. Reference in `paper/paper_draft.md`
5. Update this layout file

---

This layout ensures consistency across all figures in the TIMDR project.
