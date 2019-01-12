#!/usr/bin/env python

import re
from typing import Callable
from typing import Mapping
from collections import namedtuple

value_pattern = re.compile(r'(?P<value>\d+) -> (?P<out>\w+)')
direct_pattern = re.compile(r'(?P<in>\w+) -> (?P<out>\w+)')
not_pattern = re.compile(r'NOT (?P<in>\w+) -> (?P<out>\w+)')
lshift_pattern = re.compile(
    r'(?P<in>\w+) LSHIFT (?P<shift>\d+) -> (?P<out>\w+)')
rshift_pattern = re.compile(
    r'(?P<in>\w+) RSHIFT (?P<shift>\d+) -> (?P<out>\w+)')
fixed_and_pattern = re.compile(r'(?P<fix>\d+) AND (?P<in>\w+) -> (?P<out>\w+)')
and_pattern = re.compile(r'(?P<in1>\w+) AND (?P<in2>\w+) -> (?P<out>\w+)')
fixed_or_pattern = re.compile(r'(?P<fix>\d+) OR (?P<in>\w+) -> (?P<out>\w+)')
or_pattern = re.compile(r'(?P<in1>\w+) OR (?P<in2>\w+) -> (?P<out>\w+)')

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
    wires = {}
    for line in data.splitlines():
        wire_name, wire = get_wire(line)
        wires[wire_name] = wire
    return wires


def get_wire(line: str) -> (str, Wire):
    """Generate a Wire from an prereq line."""
    m = value_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(value=int(m.group('value')))

    m = direct_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_direct(), prereq=[m.group('in')])

    m = not_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(func=signal_not(), prereq=[m.group('in')])

    m = lshift_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_lshift(int(m.group('shift'))), prereq=[m.group('in')])

    m = rshift_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_rshift(int(m.group('shift'))), prereq=[m.group('in')])

    m = fixed_and_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_fixed_and(int(m.group('fix'))), prereq=[m.group('in')])

    m = and_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_and(), prereq=[m.group('in1'),
                                       m.group('in2')])

    m = fixed_or_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_fixed_or(int(m.group('fix'))), prereq=[m.group('in')])

    m = or_pattern.fullmatch(line)
    if m:
        return m.group('out'), Wire(
            func=signal_or(), prereq=[m.group('in1'),
                                      m.group('in2')])

    raise ValueError('Line not matched: {}'.format(line))


def determine_current(wire_name: str,
                      wires: Mapping[str, Wire]) -> (int, Mapping[str, Wire]):
    def get_current(name: str) -> int:
        wire = wires[name]
        if not wire:
            raise LookupError('No wire found with name: {}'.format(name))
        if wire.value is not None:
            return wire.value
        num_args = len(wire.prereq)

        if num_args == 1:
            req = wire.prereq[0]
            result = Wire(value=get_current(req))
            wires[req] = result
            return wire.func(result.value)

        if num_args == 2:
            req1, req2 = wire.prereq[0], wire.prereq[1]
            res1, res2 = Wire(value=get_current(req1)), Wire(
                value=get_current(req2))
            value = wire.func(res1.value, res2.value)
            wires[name] = Wire(value=value)
            return value

    return get_current(wire_name)


def signal_direct() -> Callable[[int], int]:
    return lambda x: x


def signal_lshift(shift: int) -> Callable[[int], int]:
    return lambda x: limit_signal(unsigned(x) << shift)


def signal_rshift(shift: int) -> Callable[[int], int]:
    return lambda x: limit_signal(unsigned(x) >> shift)


def signal_not() -> Callable[[int], int]:
    return lambda x: limit_signal(~unsigned(x))


def signal_and() -> Callable[[int, int], int]:
    return lambda x, y: limit_signal(unsigned(x) & unsigned(y))


def signal_fixed_and(value: int) -> Callable[[int], int]:
    return lambda x: signal_and()(x, value)


def signal_or() -> Callable[[int, int], int]:
    return lambda x, y: limit_signal(unsigned(x) | unsigned(y))


def signal_fixed_or(value: int) -> Callable[[int], int]:
    return lambda x: signal_or()(x, value)


def unsigned(signal: int) -> int:
    return signal + (1 << 32)


def limit_signal(signal: int) -> int:
    return max(0, signal % 65536)


def read_data() -> str:
    with open('input.txt') as input:
        return input.read()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
