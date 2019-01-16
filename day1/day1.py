#!/usr/bin/env python
"""Day 1: Not Quite Lisp -- Advent of Code 2015"""


def part_one(data: str) -> int:
    """The resulting floor from the elevator directions in data."""
    return data.count('(') - data.count(')')


def part_two(data: str) -> int:
    """The stop number when the basement is first entered."""
    floor = 0
    position = 1
    for char in data:
        floor = move_elevator(floor, char)
        if floor == -1:
            return position
        position += 1
    raise Exception('Basement is never entered.')


def move_elevator(floor: int, control: str) -> int:
    """Move the elevator starting at floor given the control input."""
    if control == '(':
        return floor + 1
    if control == ')':
        return floor - 1
    raise ValueError('Unexpected control input: {}'.format(control))


def read_data():
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.readline()


def main():
    """Solve the day 1 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
