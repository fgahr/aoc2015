#!/usr/bin/env python

import unittest
import day14


class TestDayFourteen(unittest.TestCase):
    def test_p1_comet(self):
        data = 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'
        reindeer = day14.reindeer_from_line(data)
        self.assertEqual(day14.distance_traveled(reindeer, 1000), 1120)

    def test_p1_dancer(self):
        data = 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
        reindeer = day14.reindeer_from_line(data)
        self.assertEqual(day14.distance_traveled(reindeer, 1000), 1056)


if __name__ == '__main__':
    unittest.main()
