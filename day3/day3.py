#!/usr/bin/env python

from typing import List
from typing import NewType

Coord = NewType('coordinate', (int, int))


def part_one(data: str) -> int:
    """Determine the number of houses receiving at least one present from Santa."""
    distinct_places = {place for place in places(data)}
    return len(distinct_places)


def part_two(data: str) -> int:
    """Determine the number of houses receiving at least one present
    from either Santa or Robot Santa."""
    santa_instructions, robo_instructions = split_instructions(data)
    santa_places = places(santa_instructions)
    robo_places = places(robo_instructions)
    distinct_places = {place for place in santa_places + robo_places}
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


def split_instructions(data: str) -> (str, str):
    """Split the combined instruction set.

    Return the instructions for Santa and Robo Santa."""
    remaining = data
    santa_instructions = ''
    robo_instructions = ''
    while len(remaining) > 1:
        santa, robo, remaining = remaining[0], remaining[1], remaining[2:]
        santa_instructions = santa_instructions + santa
        robo_instructions = robo_instructions + robo
    if len(remaining) > 0:
        santa_instructions = santa_instructions + remaining
    return santa_instructions, robo_instructions


def read_data() -> str:
    with open('input.txt') as input:
        return input.readline()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
