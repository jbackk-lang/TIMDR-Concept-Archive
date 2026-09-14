# AstroCycles‑TIMDR — API Overview

This document provides an overview of the public API for the
AstroCycles‑TIMDR framework. It describes the main modules, functions,
and data structures used throughout the project.

---

# 1. Modules

The framework is organized into the following modules:

- `algorithms.harmonic_generator`
- `algorithms.resonance_detector`
- `pipeline.run_pipeline`
- `visualization.ascii_plot`
- `timdr_cli` (command line interface)

Each module is designed to be minimal, geometric, and reproducible.

---

# 2. algorithms.harmonic_generator

### `generate_harmonic_layer(level: int) -> list[int]`
Generates a single harmonic layer with node positions.

**Parameters:**
- `level` — harmonic level (1 = base layer)

**Returns:**
- list of node indices

---

### `generate_harmonic_structure(levels: int) -> dict[int, list[int]]`
Generates multiple harmonic layers.

**Parameters:**
- `levels` — number of layers to generate

**Returns:**
- dictionary mapping layer → node list

---

# 3. algorithms.resonance_detector

### `detect_resonance(phase: float) -> bool`
Checks whether a phase value exceeds the resonance threshold.

### `next_phase(phase: float, step: float) -> float`
Advances the phase and wraps around at 1.0.

### `simulate_cycle(steps: int, step_size: float) -> list[int]`
Simulates a cycle and returns resonance event indices.

---

# 4. pipeline.run_pipeline

### `run_pipeline() -> dict`
Runs the full TIMDR pipeline:

- loads datasets  
- generates harmonic structure  
- simulates resonance events  
- returns a summary dictionary  

---

# 5. visualization.ascii_plot

### `ascii_plot(events: list[int], total_steps: int, width: int = 80) -> str`
Creates a horizontal ASCII plot of resonance events.

---

# 6. Command Line Interface (CLI)

After installation:

