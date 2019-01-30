#!/usr/bin/env python

import unittest
import day17

class TestDaySeventeen(unittest.TestCase):
    def test_p1_example(self):
        self.assertEqual(day17.ways_to_fill(25, [20, 15, 10, 5, 5]), 4)


if __name__ == '__main__':
    unittest.main()
