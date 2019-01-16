#!/usr/bin/env python
"""Day 10: Elves Look, Elves Say -- Advent of Code 2015"""

from typing import Iterable, List, Tuple
from itertools import groupby, chain


def part_one(data: str) -> int:
    """The length of the resulting string after applying
    look_and_say repeatedly 40 times."""
    return len(iterate_look_and_say(data, 40))


def part_two(data: str) -> int:
    """The length of the resulting string after applying
    look_and_say repeatedly 50 times."""
    return len(iterate_look_and_say(data, 50))


def iterate_look_and_say(sequence: str, iterations: int) -> str:
    """Iterate look_and_say a given number of times starting from sequence."""
    digits = list(map(int, sequence))
    for _ in range(0, iterations):
        digits = look_and_say(digits)

    return digits


def look_and_say(sequence: List[int]) -> List[int]:
    """Perform look-and-say on the sequence."""
    return list(chain.from_iterable(map(encode_group, groupby(sequence))))


def encode_group(group: Tuple[int, Iterable[int]]) -> List[int]:
    """Encode a run of identical elements as [length, element]."""
    key, elements = group
    return [len(list(elements)), key]


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.readline().rstrip()


def main():
    """Solve the day 10 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
