#!/usr/bin/env python

import unittest
import day11


class TestDayEleven(unittest.TestCase):
    def test_p1_adcdefgh(self):
        self.assertEqual(day11.next_valid_password('abcdefgh'), 'abcdffaa')

    def test_p1_ghijklmn(self):
        self.assertEqual(day11.next_valid_password('ghijklmn'), 'ghjaabcc')


if __name__ == '__main__':
    unittest.main()
