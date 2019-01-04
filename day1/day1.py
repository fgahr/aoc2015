#!/usr/bin/env python

data = None

def part_one():
    """Find the resulting floor from the given elevator directions."""
    floor = data.count('(') - data.count(')')
    print('Part one solution: {}'.format(floor))

def part_two():
    """Find the character position (starting at 1) when the basement is entered first."""
    position = basement_position()
    print('Part two solution: {}'.format(position))

def basement_position() -> int:
    floor = 0
    position = 1
    for char in data:
        floor = move_elevator(floor, char)
        if floor == -1:
            return position
        position += 1
    raise Exception('Basement is never entered.')

def move_elevator(floor: int, char: str) -> int:
    if char == '(':
        return floor + 1
    if char == ')':
        return floor - 1

def read_data():
    global data
    with open('input.txt') as input:
        data = input.readline()

def main():
    read_data()
    part_one()
    part_two()

if __name__ == '__main__':
    main()
