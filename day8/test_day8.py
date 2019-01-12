#!/usr/bin/env python

import unittest
import day8


class TestDayEight(unittest.TestCase):
    def test_p1_empty(self):
        self.assertEqual(day8.part_one(r'""'), 2)

    def test_p1_abc(self):
        self.assertEqual(day8.part_one(r'"abc"'), 2)

    def test_p1_aaa(self):
        self.assertEqual(day8.part_one(r'"aaa\"aaa"'), 3)

    def test_p1_hex(self):
        self.assertEqual(day8.part_one(r'"\x27"'), 5)

    def test_p2_empty(self):
        self.assertEqual(day8.part_two(r'""'), 4)

    def test_p2_abc(self):
        self.assertEqual(day8.part_two(r'"abc"'), 4)

    def test_p2_aaa(self):
        self.assertEqual(day8.part_two(r'"aaa\"aaa"'), 6)

    def test_p2_hex(self):
        self.assertEqual(day8.part_two(r'"\x27"'), 5)


if __name__ == '__main__':
    unittest.main()
