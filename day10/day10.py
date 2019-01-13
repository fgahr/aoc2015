#!/usr/bin/env python

from typing import Iterable, List, Tuple
from itertools import groupby, chain


def part_one(data: str) -> int:
    """The length of the resulting string after applying
    look_and_say repeatedly 40 times."""
    digits = list(map(int, data))
    for _ in range(0, 40):
        digits = look_and_say(digits)

    return len(digits)


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


if __name__ == '__main__':
    main()
