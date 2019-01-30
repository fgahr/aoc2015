#!/usr/bin/env python
"""Day 17: No Such Thing as Too Much -- Advent of Code 2015"""

from typing import List


def part_one(data: str, liters_eggnog=150) -> int:
    """The number of ways to store the given amount of eggnog in the
    containers specified in data."""
    return ways_to_fill(liters_eggnog, get_containers(data))


def part_two(data: str, liters_eggnog=150) -> int:
    """The number of ways to store the given amount of eggnog TWICE."""
    containers = get_containers(data)
    for num_containers in range(1, len(containers) + 1):
        ways = ways_to_fill_using_containers(liters_eggnog, num_containers,
                                             containers)
        if ways > 1:
            return ways

    raise AssertionError('No solution found.')


def ways_to_fill(amount: int, containers: List[int]) -> int:
    """The number of ways to pour amount of liquid into containers.

    All containers used must be filled up entirely."""
    if amount == 0:
        # Reached an acceptable configuration.
        return 1
    if amount < 0 or not containers:
        # No longer satisfiable.
        return 0
    # Either the first container is used or it is skipped.
    return ways_to_fill(amount - containers[0], containers[1:]) + ways_to_fill(
        amount, containers[1:])


def ways_to_fill_using_containers(amount: int, num_containers,
                                  containers: List[int]) -> int:
    """The number of ways to fill amount of liquid into exactly num_containers
    of the given available containers."""
    if amount == 0 and num_containers == 0:
        # Reached an acceptable configuration.
        return 1
    if amount < 0 or not containers or num_containers < 0:
        # No longer satisfiable.
        return 0
    with_first = ways_to_fill_using_containers(
        amount - containers[0], num_containers - 1, containers[1:])
    without_first = ways_to_fill_using_containers(amount, num_containers,
                                                  containers[1:])
    return with_first + without_first


def get_containers(data: str) -> List[int]:
    """Read the containers from data."""
    # Containers from data, sorted descending by capacity.
    containers = list(map(int, data.splitlines()))
    # Sort containers descending. This is not necessary but makes the solution
    # more intuitive.
    containers.sort(key=lambda x: -x)
    return containers


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 17 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
