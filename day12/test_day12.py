#!/usr/bin/env python

import unittest
import day12


class TestDayEleven(unittest.TestCase):
    def test_p1_simple_list(self):
        self.assertEqual(day12.part_one('[1,2,3]'), 6)

    def test_p1_map(self):
        self.assertEqual(day12.part_one('{"a":2, "b":4}'), 6)

    def test_p1_nested_list(self):
        self.assertEqual(day12.part_one('[[[3]]]'), 3)

    def test_p1_nested_map(self):
        self.assertEqual(day12.part_one('{"a":{"b":4},"c":-1}'), 3)

    def test_p1_negative_in_list(self):
        self.assertEqual(day12.part_one('{"a":[-1,1]}'), 0)

    def test_p1_negative_in_map(self):
        self.assertEqual(day12.part_one('[-1,{"a":1}]'), 0)

    def test_p1_empty_list(self):
        self.assertEqual(day12.part_one('[]'), 0)

    def test_p1_empty_map(self):
        self.assertEqual(day12.part_one('{}'), 0)


if __name__ == '__main__':
    unittest.main()
