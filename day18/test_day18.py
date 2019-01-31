#!/usr/bin/env python

import unittest
import day18



class TestDayEighteen(unittest.TestCase):
    def test_p1_example(self):
        example_data = '\n'.join(
            ['.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..'])
        self.assertEqual(day18.part_one(example_data, size=6, steps=4), 4)

    def test_p2_example(self):
        example_data = '\n'.join(
            ['##.#.#', '...##.', '#....#', '..#...', '#.#..#', '####.#'])
        self.assertEqual(day18.part_two(example_data, size=6, steps=5), 17)


if __name__ == '__main__':
    unittest.main()
