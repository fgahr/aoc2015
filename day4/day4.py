#!/usr/bin/env python
"""Day 4: The Ideal Stocking Stuffer -- Advent of Code 2015"""

import hashlib
from typing import Callable


def part_one(data: str) -> int:
    """The smallest number leading to an md5 hash with five leading zeros for data."""
    return smallest_number_satisfying(data, starts_with_five_zeros)


def part_two(data: str) -> int:
    """The smallest number leading to an md5 hash with six leading zeros for data."""
    return smallest_number_satisfying(data, starts_with_six_zeros)


def smallest_number_satisfying(data: str, pred: Callable[[str], bool]) -> int:
    "The smallest number generating a hash from data which satisfies the given predicate."
    num = 1
    while True:
        _, valid = advent_coin_hash(data, num, pred)
        if valid:
            return num
        num += 1


def advent_coin_hash(data: str, num: int,
                     pred: Callable[[str], bool]) -> (str, bool):
    """Return the hash from data and num, and whether it satisfies pred."""
    md5_hasher = hashlib.new('md5')
    md5_hasher.update((data + str(num)).encode('utf-8'))
    result = md5_hasher.hexdigest()
    return result, pred(result)


def starts_with_five_zeros(md5_hash: str) -> bool:
    """Whether the given md5 hash starts with five zeros."""
    return md5_hash.startswith('00000')


def starts_with_six_zeros(md5_hash: str) -> bool:
    """Whether the given md5 hash starts with six zeros."""
    return md5_hash.startswith('000000')


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.readline().rstrip()


def main():
    """Solve the day 4 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
