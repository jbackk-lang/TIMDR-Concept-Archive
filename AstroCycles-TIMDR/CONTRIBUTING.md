# Contributing to AstroCycles‑TIMDR

Thank you for your interest in contributing to the AstroCycles‑TIMDR
framework. This document outlines the guidelines for adding new features,
datasets, algorithms, diagrams, and documentation.

---

## 1. Project Philosophy

AstroCycles‑TIMDR is a geometric, data‑driven research framework.
Contributions should follow these principles:

- clarity over complexity  
- reproducibility over intuition  
- geometry over interpretation  
- modularity over monoliths  
- scientific tone over esoteric language  

---

## 2. Repository Structure

Please follow the existing structure:

---

## 3. Adding Algorithms

- Place new algorithms in `algorithms/`
- Use clear docstrings and type hints
- Keep functions pure (no side effects)
- Add unit tests in `tests/`
- Update the pipeline if relevant

---

## 4. Adding Data

- Use JSON format  
- Keep datasets minimal and structured  
- Document fields in comments or README  
- Do not include copyrighted ephemerides  

---

## 5. Adding Diagrams

- ASCII diagrams go to `diagrams/`
- Larger diagrams will later go to `figures/`
- Keep diagrams consistent with TIMDR geometry

---

## 6. Testing

All new code must include tests:

- place tests in `tests/`
- use Python’s `unittest`
- ensure tests run without external dependencies

---

## 7. Documentation

If you add a new module:

- update `README.md`
- update `ROADMAP.md` if it affects future plans
- update `paper/paper_draft.md` if it affects the scientific model

---

## 8. Submitting Changes

1. Fork the repository  
2. Create a feature branch  
3. Commit changes with clear messages  
4. Submit a pull request  
5. Describe the purpose and impact of your changes  

---

## 9. Code Style

- Python 3.8+  
- PEP8 formatting  
- Descriptive variable names  
- No unused imports  
- Keep functions short and modular  

---

## 10. Communication

For major changes, please open an issue first to discuss direction and
alignment with the TIMDR framework.

---

Thank you for helping develop AstroCycles‑TIMDR.

