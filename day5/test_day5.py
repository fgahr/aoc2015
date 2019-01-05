#!/usr/bin/env python

import unittest
import day5

class TestDayFive(unittest.TestCase):

    def test_p1_example1(self):
        self.assertEqual(day5.part_one('ugknbfddgicrmopn'), 1)

    def test_p1_example2(self):
        self.assertEqual(day5.part_one('aaa'), 1)

    def test_p1_example3(self):
        self.assertEqual(day5.part_one('jchzalrnumimnmhp'), 0)

    def test_p1_example4(self):
        self.assertEqual(day5.part_one('haegwjzuvuyypxyu'), 0)

    def test_p1_example4(self):
        self.assertEqual(day5.part_one('dvszwmarrgswjxmb'), 0)

if __name__ == '__main__':
    unittest.main()
