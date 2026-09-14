tests/test_resonance_detector.py
import unittest
from algorithms.resonance_detector import detect_resonance, next_phase

class TestResonanceDetector(unittest.TestCase):

    def test_resonance_detection(self):
        self.assertFalse(detect_resonance(0.5))
        self.assertTrue(detect_resonance(0.9))

    def test_phase_wrapping(self):
        self.assertEqual(next_phase(0.95, 0.1), 0.05)
        self.assertEqual(next_phase(0.2, 0.3), 0.5)

if __name__ == "__main__":
    unittest.main()
