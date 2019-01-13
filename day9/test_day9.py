#!/usr/bin/env python

import unittest
import day9


class TestDayNine(unittest.TestCase):
    def test_p1_example(self):
        data = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
        self.assertEqual(day9.part_one(data), 605)

    def test_p2_example(self):
        data = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
        self.assertEqual(day9.part_two(data), 982)


if __name__ == '__main__':
    unittest.main()
