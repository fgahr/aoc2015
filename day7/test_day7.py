#!/usr/bin/env python

import unittest
import day7

class TestDaySeven(unittest.TestCase):
    def test_p1_example(self):
        data = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
        wires = {}
        for line in data.splitlines():
            wire_name, wire = day7.get_wire(line)
            wires[wire_name] = wire

        self.assertEqual(day7.determine_current('x', wires), 123)
        self.assertEqual(day7.determine_current('y', wires), 456)
        self.assertEqual(day7.determine_current('d', wires), 72)
        self.assertEqual(day7.determine_current('e', wires), 507)
        self.assertEqual(day7.determine_current('f', wires), 492)
        self.assertEqual(day7.determine_current('g', wires), 114)
        self.assertEqual(day7.determine_current('h', wires), 65412)
        self.assertEqual(day7.determine_current('i', wires), 65079)

if __name__ == '__main__':
    unittest.main()
