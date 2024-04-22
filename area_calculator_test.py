import unittest
from area_calculator import calculate_rectangle_area

class TestAreaCalculator(unittest.TestCase):
    def test_calculate_rectangle_area(self):
        """Test calculate_rectangle_area function."""
        length = 5
        width = 4
        expected_area = 20
        self.assertEqual(calculate_rectangle_area(length, width), expected_area)

if __name__ == "__main__":
    unittest.main()