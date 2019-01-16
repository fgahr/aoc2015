#!/usr/bin/env python
"""Day 8: Matchsticks -- Advent of Code 2015"""


def part_one(data: str) -> int:
    """Determine the difference between raw and parsed string length in data."""
    sum_difference = 0
    for line in data.splitlines():
        sum_difference += len(line) - parsed_length(line)
    return sum_difference


def part_two(data: str) -> int:
    """Determine the difference between raw and escaped string length in data."""
    sum_difference = 0
    for line in data.splitlines():
        sum_difference += escaped_length(line) - len(line)
    return sum_difference


def parsed_length(line: str) -> int:
    """The length of the string after evaluating."""
    return len(eval(line))


def escaped_length(line: str) -> int:
    """The length of the string after performing the necessary escapes.

    Assumes that backslashes and quotes are escaped, and the string is
    surrounded with quotes."""
    # +2 for surrounding quotes, rest is for normal escapes.
    return len(line) + 2 + line.count(r'"') + line.count('\\')


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 8 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
