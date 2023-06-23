import unittest
import avg

class AverageTest(unittest.TestCase):
    def test_average_of_empty_list(self):
        with self.assertRaises(ValueError):
            avg.calculate_average([])

    def test_average_of_positive_numbers(self):
        self.assertEqual(avg.calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(avg.calculate_average([10, 20, 30, 40, 50]), 30.0)

    def test_average_of_negative_numbers(self):
        self.assertEqual(avg.calculate_average([-1, -2, -3, -4, -5]), -3.0)
        self.assertEqual(avg.calculate_average([-10, -20, -30, -40, -50]), -30.0)

    def test_average_of_mixed_numbers(self):
        self.assertEqual(avg.calculate_average([-1, 2, -3, 4, -5]), -0.6)
        self.assertAlmostEqual(avg.calculate_average([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)

if __name__ == '__main__':
    unittest.main()
