#!/usr/bin/env python

import unittest
import day2


class TestDayTwo(unittest.TestCase):
    def test_p1_2_3_4(self):
        self.assertEqual(day2.part_one('2x3x4'), 58)

    def test_p1_1_1_10(self):
        self.assertEqual(day2.part_one('1x1x10'), 43)

    def test_p2_2_3_4(self):
        self.assertEqual(day2.part_two('2x3x4'), 34)

    def test_p2_1_1_10(self):
        self.assertEqual(day2.part_two('1x1x10'), 14)


if __name__ == '__main__':
    unittest.main()
