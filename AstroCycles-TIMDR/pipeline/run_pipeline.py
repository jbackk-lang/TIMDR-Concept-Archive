"""
TIMDR Pipeline: Harmonic + Resonance Integration

This script loads planetary cycle data and harmonic aspect data,
generates harmonic layers, and detects resonance events using
TIMDR algorithms.
"""

import json
from algorithms.harmonic_generator import generate_harmonic_structure
from algorithms.resonance_detector import simulate_cycle


def load_json(path: str):
    """Load JSON data from file."""
    with open(path, "r") as f:
        return json.load(f)


def run_pipeline():
    # Load datasets
    planetary_data = load_json("data/planetary_cycles.json")
    aspect_data = load_json("data/harmonic_aspects.json")

    print("Loaded planetary cycles:", len(planetary_data["cycles"]))
    print("Loaded harmonic aspects:", len(aspect_data["aspects"]))

    # Generate harmonic structure (3 layers for demo)
    structure = generate_harmonic_structure(3)
    print("\nHarmonic structure:")
    for level, nodes in structure.items():
        print(f"  Level {level}: {nodes}")

    # Simulate resonance events
    print("\nSimulating resonance events...")
    events = simulate_cycle(steps=200, step_size=0.01)
    print("Resonance events at steps:", events)

    # Output summary
    return {
        "harmonic_structure": structure,
        "resonance_events": events,
        "planetary_cycles": planetary_data,
        "harmonic_aspects": aspect_data
    }


if __name__ == "__main__":
    summary = run_pipeline()
    print("\nPipeline completed.")
