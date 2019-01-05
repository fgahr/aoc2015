#!/usr/bin/env python

import unittest
import day3


class TestDayThree(unittest.TestCase):
    def test_p1_simple_step(self):
        self.assertEqual(day3.part_one('>'), 2)

    def test_p1_round_trip(self):
        self.assertEqual(day3.part_one('^>v<'), 4)

    def test_p1_twitch(self):
        self.assertEqual(day3.part_one('^v^v^v^v^v'), 2)

    def test_p2_up_down(self):
        self.assertEqual(day3.part_two('^v'), 3)

    def test_p2_round_trips(self):
        self.assertEqual(day3.part_two('^>v<'), 3)

    def test_p2_linear(self):
        self.assertEqual(day3.part_two('^v^v^v^v^v'), 11)


if __name__ == '__main__':
    unittest.main()
