#!/usr/bin/env python

import unittest
import day18

class TestDaySeventeen(unittest.TestCase):
    def test_p1_example(self):
        data = '\n'.join([
            '.#.#.#',
            '...##.',
            '#....#',
            '..#...',
            '#.#..#',
            '####..'
        ])
        self.assertEqual(day18.part_one(data, size=6, steps=4), 4)


if __name__ == '__main__':
    unittest.main()
