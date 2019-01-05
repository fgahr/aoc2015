#!/usr/bin/env python

import hashlib
from typing import Callable

def part_one(data: str) -> int:
    """Determine the smallest number leading to a suitable md5 hash for data."""
    return smallest_number_satisfying(data, starts_with_five_zeros)

def part_two(data: str) -> int:
    """Determine the smallest number leading to a suitable md5 hash for data."""
    return smallest_number_satisfying(data, starts_with_six_zeros)

def smallest_number_satisfying(data: str, pred: Callable[[str], bool]) -> int:
    "The smallest number generating a hash from data which satisfies the given predicate."
    num = 1
    while True:
        res, ok = advent_coin_hash(data, num, pred)
        if ok:
            return num
        num += 1

def advent_coin_hash(data: str, num: int, pred: Callable[[str], bool]) -> (str, bool):
    """Return the hash from data and num, and whether it satisfies pred."""
    h = hashlib.new('md5')
    h.update((data + str(num)).encode('utf-8'))
    result = h.hexdigest()
    return result, pred(result)

def starts_with_five_zeros(md5_hash: str) -> bool:
    return md5_hash.startswith('00000')

def starts_with_six_zeros(md5_hash: str) -> bool:
    return md5_hash.startswith('000000')

def read_data() -> str:
    with open('input.txt') as input:
        return input.readline().rstrip()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))

if __name__ == '__main__':
    main()
