#!/usr/bin/env python

import unittest
import day14


class TestDayFourteen(unittest.TestCase):
    def test_p1_example(self):
        data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
        self.assertEqual(day14.part_one(data, travel_time=1000), 1120)

    def test_p2_example(self):
        data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
        self.assertEqual(day14.part_two(data, travel_time=1000), 689)


if __name__ == '__main__':
    unittest.main()
