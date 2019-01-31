#!/usr/bin/env python
"""Day 19: Medicine for Rudolph -- Advent of Code 2015"""

from typing import List, Tuple, Callable
from itertools import chain
import re


def part_one(data: str) -> int:
    """The number of different molecules after performing one substitution."""
    rules, molecule = parse_data(data)
    return len(set(chain.from_iterable(map(substitutions(molecule), rules))))


def substitutions(molecule: str) -> Callable[[Tuple[str, str]], List[str]]:
    """Returns a function for generating substitutions on molecule."""

    def substitute(rule: Tuple[str, str]) -> List[str]:
        """Perform the rule substitution in all possible places."""
        rule_from, rule_to = rule
        molecules = []
        idx = molecule.find(rule_from)
        while idx > -1:
            molecules.append(molecule[0:idx] + re.sub(
                rule_from, rule_to, molecule[idx:], count=1))
            idx = molecule.find(rule_from, idx + 1)
        return molecules

    return substitute


def parse_data(data: str) -> (List[Tuple[str, str]], str):
    """The rules and the starting molecule from the data."""
    rules = []
    molecule = ''
    for line in data.splitlines():
        if not line:
            # Skip empty line(s)
            continue
        if ' => ' in line:
            rule_from, _, rule_to = line.partition(' => ')
            rules.append((rule_from, rule_to))
        else:
            molecule = line
    return rules, molecule


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 19 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
