#!/usr/bin/env python
"""Day 3: Perfectly Spherical Houses in a Vacuum -- Advent of Code 2015"""

from typing import List
from typing import NewType

Coord = NewType('coordinate', (int, int))


def part_one(data: str) -> int:
    """The number of houses receiving at least one present."""
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
    """The places visited after following the instructions from data."""
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


def move_up(place: Coord) -> Coord:
    """Move up from place."""
    x_place, y_place = place
    return (x_place, y_place + 1)


def move_down(place: Coord) -> Coord:
    """Move down from place."""
    x_place, y_place = place
    return (x_place, y_place - 1)


def move_left(place: Coord) -> Coord:
    """Move left from place."""
    x_place, y_place = place
    return (x_place - 1, y_place)


def move_right(place: Coord) -> Coord:
    """Move right from place."""
    x_place, y_place = place
    return (x_place + 1, y_place)


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
    if remaining:
        santa_instructions = santa_instructions + remaining
    return santa_instructions, robo_instructions


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.readline()


def main():
    """Solve the day 3 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
