import unittest
import day6


class TestDayOneMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day6.part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
        self.assertEqual(day6.part_one("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(day6.part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)

    def test_part_two(self):
        self.assertEqual(day6.part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19)
        self.assertEqual(day6.part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29)


if __name__ == '__main__':
    unittest.main()
