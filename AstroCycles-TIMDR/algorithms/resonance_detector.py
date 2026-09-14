"""
Resonance Detector (TIMDR Framework)

This module detects resonance points within harmonic cycles.
A resonance occurs when the phase shift reaches a threshold
defined by the TIMDR geometric operator.
"""

def detect_resonance(phase: float, threshold: float = 0.85) -> bool:
    """
    Determine whether a resonance event occurs.

    Parameters:
        phase (float): Current phase position (0.0 to 1.0)
        threshold (float): Resonance threshold (default: 0.85)

    Returns:
        bool: True if resonance occurs, False otherwise
    """
    if not 0.0 <= phase <= 1.0:
        raise ValueError("Phase must be between 0.0 and 1.0")

    return phase >= threshold


def next_phase(phase: float, step: float) -> float:
    """
    Advance the phase by a given step, wrapping around at 1.0.

    Parameters:
        phase (float): Current phase
        step (float): Increment step

    Returns:
        float: Updated phase value
    """
    new_phase = phase + step
    if new_phase >= 1.0:
        new_phase -= 1.0
    return new_phase


def simulate_cycle(steps: int, step_size: float, threshold: float = 0.85):
    """
    Simulate a full cycle and return all resonance events.

    Parameters:
        steps (int): Number of simulation steps
        step_size (float): Phase increment per step
        threshold (float): Resonance threshold

    Returns:
        list[int]: Indices where resonance occurred
    """
    phase = 0.0
    resonances = []

    for i in range(steps):
        if detect_resonance(phase, threshold):
            resonances.append(i)
        phase = next_phase(phase, step_size)

    return resonances


if __name__ == "__main__":
    # Example simulation
    events = simulate_cycle(100, 0.02)
    print("Resonance events at steps:", events)
