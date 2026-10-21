import unittest

from average import average_marks


class AverageMarksTests(unittest.TestCase):
    def test_average_of_marks(self):
        self.assertEqual(average_marks([70, 80, 90]), 80.0)

    def test_empty_marks_returns_float_zero(self):
        result = average_marks([])

        self.assertEqual(result, 0.0)
        self.assertIsInstance(result, float)

    def test_zero_marks(self):
        self.assertEqual(average_marks([0, 0, 0]), 0.0)


if __name__ == "__main__":
    unittest.main()
