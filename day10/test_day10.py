#!/usr/bin/env python

import unittest
import day10


class TestDayTen(unittest.TestCase):
    def test_look_and_say_1(self):
        self.assertEqual(list(day10.look_and_say([1])), [1, 1])

    def test_look_and_say_11(self):
        self.assertEqual(list(day10.look_and_say([1, 1])), [2, 1])

    def test_look_and_say_21(self):
        self.assertEqual(list(day10.look_and_say([2, 1])), [1, 2, 1, 1])

    def test_look_and_say_1211(self):
        self.assertEqual(list(day10.look_and_say([1, 2, 1, 1])), [1, 1, 1, 2, 2, 1])

    def test_look_and_say_111221(self):
        self.assertEqual(list(day10.look_and_say([1, 1, 1, 2, 2, 1])), [3, 1, 2, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()
