"""
Basic Usage Example for AstroCycles-TIMDR

This script demonstrates how to:
1. Load the TIMDR pipeline
2. Run harmonic + resonance analysis
3. Display the results in a simple format
"""

from pipeline.run_pipeline import run_pipeline

def main():
    print("Running TIMDR pipeline example...\n")

    summary = run_pipeline()

    print("\n--- SUMMARY ---")
    print("Harmonic structure levels:", len(summary["harmonic_structure"]))
    print("Resonance events detected:", len(summary["resonance_events"]))
    print("Planetary cycles loaded:", len(summary["planetary_cycles"]["cycles"]))
    print("Harmonic aspects loaded:", len(summary["harmonic_aspects"]["aspects"]))

    print("\nExample complete.")

if __name__ == "__main__":
    main()
