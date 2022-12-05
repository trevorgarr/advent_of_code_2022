import unittest
import day2

# Currently doesn't work

class TestDayOneMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day2.part_one(["AY", "BX","CZ"]), 15)

    def test_part_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
