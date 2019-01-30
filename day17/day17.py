#!/usr/bin/env python
"""Day 17: No Such Thing as Too Much -- Advent of Code 2015"""

from typing import List


def part_one(data: str, liters_eggnog=150) -> int:
    """The number of ways to store the given amount of eggnog in the
    containers specified in data."""
    # Containers from data, sorted descending by capacity.
    containers = list(map(int, data.splitlines()))
    # Sort containers descending. This is not necessary but makes the solution
    # more intuitive.
    containers.sort(key=lambda x: -x)
    return ways_to_fill(liters_eggnog, containers)

def ways_to_fill(amount: int, containers: List[int]) -> int:
    """The number of ways to pour amount of liquid into containers.

    All containers used must be filled up entirely."""
    # Reached an acceptable configuration.
    if amount == 0:
        return 1
    # No longer satisfiable.
    if amount < 0 or not containers:
        return 0
    # Either the first container is used or it is skipped.
    return ways_to_fill(amount - containers[0], containers[1:]) + ways_to_fill(
        amount, containers[1:])


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read().rstrip()


def main():
    """Solve the day 16 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
