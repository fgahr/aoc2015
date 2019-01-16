#!/usr/bin/env python
"""Day 13: Knights of the Dinner Table -- Advent of Code 2015"""

from typing import Mapping, Set, List
import itertools
import re

INPUT = re.compile(r'(?P<name1>\w+) would (?P<change>(?:lose|gain) \d+) ' +
                   r'happiness units by sitting next to (?P<name2>\w+).')
CHANGE = re.compile(r'(?P<kind>lose|gain) (?P<amount>\d+)')


def part_one(data: str) -> int:
    """The change in happiness for optimal seating according to data."""
    names, happiness_changes = parse_input(data)
    names = list(names)
    seating_orders = list(itertools.permutations(names))
    maximum_change = happiness_change(seating_orders[0], happiness_changes)
    for seating_order in seating_orders:
        total_change = happiness_change(seating_order, happiness_changes)
        maximum_change = max(maximum_change, total_change)

    return maximum_change


def happiness_change(seating: List[str],
                     changes: Mapping[str, Mapping[str, int]]) -> int:
    """The total happiness change for the given seating order."""
    change = 0
    previous = seating[-1]
    for current in seating:
        change += changes.setdefault(previous, {}).setdefault(current, 0)
        change += changes.setdefault(current, {}).setdefault(previous, 0)
        previous = current
    return change


def parse_input(data: str) -> (Set[str], Mapping[str, Mapping[str, int]]):
    """Extract the names and associated happines changes from data."""
    names = set()
    happiness_changes = {}
    for line in data.splitlines():
        match = INPUT.fullmatch(line)
        if not match:
            raise ValueError('Illegal input: {}'.format(line))
        amount = change_amount(match.group('change'))
        name1 = match.group('name1')
        name2 = match.group('name2')
        names.add(name1)
        names.add(name2)
        if name1 not in happiness_changes.keys():
            happiness_changes[name1] = {}
        happiness_changes[name1][name2] = amount
    return names, happiness_changes


def change_amount(change_description: str) -> int:
    """The amount of happines change from a description in the input."""
    match = CHANGE.fullmatch(change_description)
    amount = int(match.group('amount'))
    if match.group('kind') == 'gain':
        return amount
    if match.group('kind') == 'lose':
        return -amount
    raise ValueError(
        'Unable to parse change information: {}'.format(change_description))


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 13 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
