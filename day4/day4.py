#!/usr/bin/env python

import hashlib

def part_one(data: str) -> int:
    """Determine the smallest number leading to a suitable md5 hash for data."""
    num = 1
    while True:
        res = advent_coin_hash(data, num)
        if res:
            return num
        num += 1

def advent_coin_hash(data: str, num: int) -> str:
    h = hashlib.new('md5')
    h.update((data + str(num)).encode('utf-8'))
    result = h.hexdigest()
    if is_valid_coin_hash(result):
        return result
    return None

def is_valid_coin_hash(md5_hash: str) -> bool:
    return md5_hash.startswith('00000')

def read_data() -> str:
    with open('input.txt') as input:
        return input.readline().rstrip()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))

if __name__ == '__main__':
    main()
