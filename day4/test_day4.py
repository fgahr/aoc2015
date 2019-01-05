#!/usr/bin/env python

import unittest
import day4

class TestDayFour(unittest.TestCase):

    def test_p1_adcdef(self):
        self.assertEqual(day4.part_one('abcdef'), 609043)

    def test_p1_pqrstuv(self):
        self.assertEqual(day4.part_one('pqrstuv'), 1048970)

if __name__ == '__main__':
    unittest.main()
