import unittest
import day4


class TestDayOneMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day4.part_one([[2,4,6,8],[2,3,4,5],[5,7,7,9],[2,8,3,7],[6,6,4,6],[2,6,4,8]]), 2)

    def test_part_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
