#!/usr/bin/env python
"""This module solves the day 12 problems of Advent of Code 2015."""

import re

def part_one(data: str) -> int:
    """Sum all numbers present in data."""
    # Pattern uses lookahead and lookbehind to make sure we get the full
    # numbers. Simply including non-numbers outside the matching group causes
    # problems if two numbers are separated by a single token, e.g. '1,2'.
    pattern = re.compile(r'(?<=[^0-9])(?P<number>-?\d+)(?![0-9])', re.MULTILINE)
    return sum(map(int, (pattern.findall(data))))


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.readline().rstrip()


def main():
    """Solve the day 12 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
