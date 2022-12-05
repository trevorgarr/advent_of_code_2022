import unittest
import day1


class TestDayOneMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day1.part_one(["10", "20","","10","20","30"]), 60)

    def test_part_two(self):
        self.assertEqual(day1.part_two(["10","20","","20","30","","100","","200","","300","","1","2"]), 600)

if __name__ == '__main__':
    unittest.main()
