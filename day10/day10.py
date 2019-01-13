#!/usr/bin/env python

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


def iterate_look_and_say(input: str, iterations: int) -> str:
    digits = list(map(int, input))
    for _ in range(0, iterations):
        digits = look_and_say(digits)

    return digits


def look_and_say(input: List[int]) -> List[int]:
    return list(chain.from_iterable(map(encode_group, groupby(input))))


def encode_group(group: Tuple[int, Iterable[int]]) -> List[int]:
    key, elements = group
    return [len(list(elements)), key]


def read_data() -> str:
    with open('input.txt') as input:
        return input.readline().rstrip()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
