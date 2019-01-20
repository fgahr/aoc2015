#!/usr/bin/env python
"""Day 7: Some Assembly Required -- Advent of Code 2015"""

import re
from typing import Callable
from typing import Mapping
from collections import namedtuple

VALUE = re.compile(r'(?P<value>\d+) -> (?P<out>\w+)')
DIRECT = re.compile(r'(?P<in>\w+) -> (?P<out>\w+)')
NOT = re.compile(r'NOT (?P<in>\w+) -> (?P<out>\w+)')
LSHIFT = re.compile(r'(?P<in>\w+) LSHIFT (?P<shift>\d+) -> (?P<out>\w+)')
RSHIFT = re.compile(r'(?P<in>\w+) RSHIFT (?P<shift>\d+) -> (?P<out>\w+)')

# NOTE: In the input this solution is based upon, AND was sometimes against
# a fixed value. In those cases, the fixed value was always the left argument.
# The same was not encountered for OR; however, it was still included here.
# If fixed values appear as the right argument for your input, this solution
# requires adjustments to accomodate.
FIXED_AND = re.compile(r'(?P<fix>\d+) AND (?P<in>\w+) -> (?P<out>\w+)')
AND = re.compile(r'(?P<in1>\w+) AND (?P<in2>\w+) -> (?P<out>\w+)')
FIXED_OR = re.compile(r'(?P<fix>\d+) OR (?P<in>\w+) -> (?P<out>\w+)')
OR = re.compile(r'(?P<in1>\w+) OR (?P<in2>\w+) -> (?P<out>\w+)')

Wire = namedtuple('Wire', 'func prereq value', defaults=[None, [], None])


def part_one(data: str) -> int:
    """Determine the signal on wire 'a'."""
    wires = read_wires(data)
    return determine_current('a', wires)


def part_two(data: str) -> int:
    """Determine the signal on wire 'a' after setting wire 'b' to the
    original value of 'a'."""
    wires = read_wires(data)
    current_a = determine_current('a', wires)
    wires = read_wires(data)
    wires['b'] = Wire(value=current_a)
    return determine_current('a', wires)


def read_wires(data: str) -> Mapping[int, Wire]:
    """Read the wiring information from data."""
    wires = {}
    for line in data.splitlines():
        wire_name, wire = get_wire(line)
        wires[wire_name] = wire
    return wires


def get_wire(line: str) -> (str, Wire):
    """Generate a Wire from an prereq line."""
    match = VALUE.fullmatch(line)
    if match:
        return match.group('out'), Wire(value=int(match.group('value')))

    match = DIRECT.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_direct(), prereq=[match.group('in')])

    match = NOT.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_not(), prereq=[match.group('in')])

    match = LSHIFT.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_lshift(int(match.group('shift'))),
            prereq=[match.group('in')])

    match = RSHIFT.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_rshift(int(match.group('shift'))),
            prereq=[match.group('in')])

    match = FIXED_AND.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_fixed_and(int(match.group('fix'))),
            prereq=[match.group('in')])

    match = AND.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_and(), prereq=[match.group('in1'),
                                       match.group('in2')])

    match = FIXED_OR.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_fixed_or(int(match.group('fix'))),
            prereq=[match.group('in')])

    match = OR.fullmatch(line)
    if match:
        return match.group('out'), Wire(
            func=signal_or(), prereq=[match.group('in1'),
                                      match.group('in2')])

    raise ValueError('Line not matched: {}'.format(line))


def determine_current(wire_name: str,
                      wires: Mapping[str, Wire]) -> (int, Mapping[str, Wire]):
    """Determine the current on one of the given wires."""
    def get_current(name: str) -> int:
        """Recursively calculate the current on wires as needed."""
        wire = wires[name]
        if not wire:
            raise LookupError('No wire found with name: {}'.format(name))
        if wire.value is not None:
            return wire.value
        num_args = len(wire.prereq)

        if num_args == 1:
            req = wire.prereq[0]
            result = Wire(value=get_current(req))
            # Memoize.
            wires[req] = result
            return wire.func(result.value)

        if num_args == 2:
            req1, req2 = wire.prereq[0], wire.prereq[1]
            res1, res2 = Wire(value=get_current(req1)), Wire(
                value=get_current(req2))
            value = wire.func(res1.value, res2.value)
            # Memoize.
            wires[name] = Wire(value=value)
            return value

        raise ValueError(
            'Unhandled number of arguments for wire: {}'.format(wire))

    return get_current(wire_name)


def signal_direct() -> Callable[[int], int]:
    """A circuit no-op, transmitting the signal as-is."""
    return lambda x: x


def signal_lshift(shift: int) -> Callable[[int], int]:
    """A circuit element performing a fixed LSHIFT on a signal."""
    return lambda x: limit_signal(x << shift)


def signal_rshift(shift: int) -> Callable[[int], int]:
    """A circuit element performing a fixed RSHIFT on a signal."""
    return lambda x: limit_signal(x >> shift)


def signal_not() -> Callable[[int], int]:
    """A circuit element performing bitwise NOT on a signal."""
    return lambda x: limit_signal(~x)


def signal_and() -> Callable[[int, int], int]:
    """A circuit element performing bitwise AND on two signals."""
    return lambda x, y: limit_signal(x & y)


def signal_fixed_and(value: int) -> Callable[[int], int]:
    """A circuit element performing bitwise AND with a fixed value."""
    return lambda x: signal_and()(x, value)


def signal_or() -> Callable[[int, int], int]:
    """A circuit element performing a bitwise OR on two signals."""
    return lambda x, y: limit_signal(x | y)


def signal_fixed_or(value: int) -> Callable[[int], int]:
    """A circuit element performing a bitwise OR with a fixed value."""
    return lambda x: signal_or()(x, value)


def limit_signal(signal: int) -> int:
    """Limit the signal to a value in the possible range."""
    return max(0, signal % 65536)


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 7 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
