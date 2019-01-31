#!/usr/bin/env python

import unittest
import day19

test_data_p1_1 = """
H => HO
H => OH
O => HH

HOH
"""

test_data_p1_2 = """
H => HO
H => OH
O => HH

HOHOHO
"""


class TestDayNineteen(unittest.TestCase):
    def test_p1_example_1(self):
        self.assertEqual(day19.part_one(test_data_p1_1), 4)

    def test_p1_example_2(self):
        self.assertEqual(day19.part_one(test_data_p1_2), 7)


if __name__ == '__main__':
    unittest.main()
