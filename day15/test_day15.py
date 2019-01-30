#!/usr/bin/env python

import unittest
import day15

data = ''.join([
    'Butterscotch: capacity -1, durability -2, flavor 6, ',
    'texture 3, calories 8\nCinnamon: capacity 2, durability 3, ',
    'flavor -2, texture -1, calories 3'
])

class TestDayFifteen(unittest.TestCase):
    def test_p1_example(self):
        self.assertEqual(day15.part_one(data), 62842880)

    def test_p2_example(self):
        self.assertEqual(day15.part_two(data), 57600000)


if __name__ == '__main__':
    unittest.main()
