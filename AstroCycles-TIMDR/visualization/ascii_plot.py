visualization/ascii_plot.py
"""
ASCII Visualization for TIMDR Pipeline

This module generates a simple ASCII plot of resonance events
detected by the TIMDR pipeline.
"""

from pipeline.run_pipeline import run_pipeline

def ascii_plot(events, total_steps, width=80):
    """
    Create an ASCII plot of resonance events.

    Parameters:
        events (list[int]): Steps where resonance occurred
        total_steps (int): Total number of simulation steps
        width (int): Width of the ASCII plot

    Returns:
        str: ASCII plot as a string
    """
    scale = total_steps / width
    line = [" "] * width

    for e in events:
        pos = int(e / scale)
        if 0 <= pos < width:
            line[pos] = "●"

    return "|" + "".join(line) + "|"


def main():
    print("Running pipeline for ASCII visualization...\n")

    summary = run_pipeline()
    events = summary["resonance_events"]

    print("\nASCII Resonance Plot:")
    print(ascii_plot(events, total_steps=200))


if __name__ == "__main__":
    main()
