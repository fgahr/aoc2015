#!/usr/bin/env python

import unittest
import day11


class TestDayEleven(unittest.TestCase):
    def test_p1_adcdefgh(self):
        self.assertEqual(day11.part_one('abcdefgh'), 'abcdffaa')

    def test_p1_ghijklmn(self):
        self.assertEqual(day11.part_one('ghijklmn'), 'ghjaabcc')


if __name__ == '__main__':
    unittest.main()
