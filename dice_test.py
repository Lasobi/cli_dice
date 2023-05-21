import unittest
from dice import roll_dice

class TestDiceRoller(unittest.TestCase):
    
    def test_roll_dice(self):
        num_sides = 6
        num_rolls = 5
        result = roll_dice(num_sides, num_rolls)

        # Test number of rolls
        self.assertEqual(len(result), num_rolls)

        # Test each roll is within correct range
        for roll in result:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, num_sides)

if __name__ == "__main__":
    unittest.main()
