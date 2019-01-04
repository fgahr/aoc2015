#!/usr/bin/env python

from typing import List
from typing import NewType

Coord = NewType('coordinate', (int, int))

def part_one(data: str) -> int:
    distinct_places = {place for place in places(data)}
    return len(distinct_places)

def places(data: str) -> List[Coord]:
    current_position = (0, 0)
    positions = [current_position]
    for instruction in data:
        if instruction == '^':
            current_position = move_up(current_position)
        elif instruction == 'v':
            current_position = move_down(current_position)
        elif instruction == '<':
            current_position = move_left(current_position)
        elif instruction == '>':
            current_position = move_right(current_position)
        positions.append(current_position)
    return positions

def move_up(p: Coord) -> Coord:
    x, y = p
    return (x, y + 1)

def move_down(p: Coord) -> Coord:
    x, y = p
    return (x, y - 1)

def move_left(p: Coord) -> Coord:
    x, y = p
    return (x - 1, y)

def move_right(p: Coord) -> Coord:
    x, y = p
    return (x + 1, y)

def read_data() -> str:
    with open('input.txt') as input:
        return input.readline()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))

if __name__ == '__main__':
    main()
