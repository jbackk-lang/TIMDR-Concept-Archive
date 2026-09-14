"""
Harmonic Generator (TIMDR Framework)

This module generates harmonic layers and resonance nodes
based on a minimal geometric interpretation of the TIMDR model.
"""

def generate_harmonic_layer(level: int) -> list[int]:
    """
    Generate resonance nodes for a given harmonic level.
    Each level increases the number of nodes in a prime-like pattern.

    Parameters:
        level (int): Harmonic level (1 = base cycle)

    Returns:
        list[int]: Positions of resonance nodes on the cycle ring
    """
    if level < 1:
        raise ValueError("Level must be >= 1")

    # Prime-like growth pattern (placeholder logic)
    node_count = level * 2

    return list(range(node_count))


def generate_harmonic_structure(max_level: int) -> dict[int, list[int]]:
    """
    Generate harmonic layers up to a given level.

    Parameters:
        max_level (int): Highest harmonic layer to generate

    Returns:
        dict[int, list[int]]: Mapping of level -> resonance nodes
    """
    structure = {}

    for level in range(1, max_level + 1):
        structure[level] = generate_harmonic_layer(level)

    return structure


if __name__ == "__main__":
    # Example usage
    structure = generate_harmonic_structure(3)
    print(structure)
