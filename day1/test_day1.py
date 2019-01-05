#!/usr/bin/env python

import unittest
import day1


class TestDayOne(unittest.TestCase):
    def test_p1_to_floor_0(self):
        self.assertEqual(day1.part_one('(())'), 0)
        self.assertEqual(day1.part_one('()()'), 0)

    def test_p1_to_floor_3(self):
        self.assertEqual(day1.part_one('((('), 3)
        self.assertEqual(day1.part_one('(()(()('), 3)
        self.assertEqual(day1.part_one('))((((('), 3)

    def test_p1_to_basement_1(self):
        self.assertEqual(day1.part_one('())'), -1)
        self.assertEqual(day1.part_one('))('), -1)

    def test_p1_to_basement_3(self):
        self.assertEqual(day1.part_one(')))'), -3)
        self.assertEqual(day1.part_one(')())())'), -3)

    def test_p2_one_step(self):
        self.assertEqual(day1.part_two(')'), 1)

    def test_p2_five_steps(self):
        self.assertEqual(day1.part_two('()())'), 5)


if __name__ == '__main__':
    unittest.main()
