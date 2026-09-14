tests/test_harmonic_generator.py
import unittest
from algorithms.harmonic_generator import generate_harmonic_layer, generate_harmonic_structure

class TestHarmonicGenerator(unittest.TestCase):

    def test_layer_generation(self):
        layer = generate_harmonic_layer(1)
        self.assertEqual(len(layer), 2)
        self.assertEqual(layer, [0, 1])

    def test_structure_generation(self):
        structure = generate_harmonic_structure(3)
        self.assertEqual(len(structure), 3)
        self.assertEqual(structure[1], [0, 1])
        self.assertEqual(structure[2], [0, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()
