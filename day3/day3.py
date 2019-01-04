#!/usr/bin/env python

def part_one(data: str) -> int:
    return 1

def read_data() -> str:
    with open('input.txt') as input:
        return input.readline()

def main():
    data = read_data()
    part_one(data)

if __name__ == '__main__':
    main()
