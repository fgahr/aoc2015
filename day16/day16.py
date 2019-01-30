#!/usr/bin/env python
"""Day 16: Aunt Sue -- Advent of Code 2015"""

from typing import Mapping, Callable
import re


def part_one(data: str) -> int:
    """Find the number of the Aunt Sue who sent you the gift."""

    def matches_p1(info: Mapping[str, int],
                   test_result: Mapping[str, int]) -> bool:
        """True if the info matches the test result."""
        for key, value in info.items():
            if test_result[key] != value:
                return False
        return True

    return find_matching_aunt(matches_p1, data)


def part_two(data: str) -> int:
    """Find the number of the Aunt Sue who ACTUALLY sent you the gift."""

    def matches_p2(info: Mapping[str, int],
                   result: Mapping[str, int]) -> bool:
        """True if the info ACTUALLY matches the test result."""
        for key, value in info.items():
            if key in ['cats', 'trees']:
                if value <= result[key]:
                    return False
            elif key in ['pomeranians', 'goldfish']:
                if value >= result[key]:
                    return False
            else:
                if result[key] != value:
                    return False
        return True

    return find_matching_aunt(matches_p2, data)


def find_matching_aunt(
        predicate: Callable[[Mapping[str, int], Mapping[str, int]], bool],
        data: str) -> int:
    """The number of the aunt from data satisfying the predicate."""
    # The result the aunt we are looking for needs to match.
    test_result = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    matches = []
    for line in data.splitlines():
        num, info = parse_aunt_information(line)
        if predicate(info, test_result):
            matches.append(num)

    if len(matches) > 1:
        raise AssertionError(
            'More than one matching aunt found: {}'.format(matches))
    if not matches:
        raise AssertionError('No matching aunt found.')
    return matches[0]


def parse_aunt_information(line: str) -> (int, Mapping[str, int]):
    """The number of the aunt, along with the remembered parameters."""
    sue_number, parameters = re.split(': ', line, maxsplit=1)
    number = int(re.sub('Sue ', '', sue_number))

    def parse_param(description: str) -> (str, int):
        """The name and value of the described parameter."""
        name, value = re.split(': ', description)
        return name, int(value)

    return number, dict(map(parse_param, re.split(', ', parameters)))


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 16 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
