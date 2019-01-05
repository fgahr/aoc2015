#!/usr/bin/env python

def part_one(data: str) -> int:
    """Find the resulting floor from the given elevator directions."""
    return data.count('(') - data.count(')')

def part_two(data: str) -> int:
    """Find the character position (starting at 1) when the basement is entered first."""
    floor = 0
    position = 1
    for char in data:
        floor = move_elevator(floor, char)
        if floor == -1:
            return position
        position += 1
    raise Exception('Basement is never entered.')

def move_elevator(floor: int, control: str) -> int:
    if control == '(':
        return floor + 1
    if control == ')':
        return floor - 1

def read_data():
    with open('input.txt') as input:
        return input.readline()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))

if __name__ == '__main__':
    main()
