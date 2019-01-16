#!/usr/bin/env python
"""Day 6: Probably a Fire Hazard -- Advent of Code 2015"""

from collections import namedtuple
from typing import Callable
from abc import ABC
from abc import abstractmethod
import re

Point = namedtuple('Point', 'x y')


class LightBoard(ABC):
    """Class describing an abstract light board."""

    @abstractmethod
    def turn_on_area(self, corner1: Point, corner2: Point):
        """Turn on the lights in the area delimited by two corners."""

    @abstractmethod
    def turn_off_area(self, corner1: Point, corner2: Point):
        """Turn off the lights in the area delimited by two corners."""

    @abstractmethod
    def toggle_area(self, corner1: Point, corner2: Point):
        """Toggle the lights in the area delimited by two corners."""

    @abstractmethod
    def num_lights_lit(self) -> int:
        """The number of lit lights on this board."""


class LightBoardOnOff(LightBoard):
    """A light board featuring non-dimmable lights: on/off only."""

    def __init__(self, size: int):
        self.size = size
        self.board = [False for i in range(size * size)]

    def turn_on_area(self, corner1: Point, corner2: Point):
        def turn_on(_: bool) -> bool:
            return True

        self.modify_area(corner1, corner2, turn_on)

    def turn_off_area(self, corner1: Point, corner2: Point):
        def turn_off(_: bool) -> bool:
            return False

        self.modify_area(corner1, corner2, turn_off)

    def toggle_area(self, corner1: Point, corner2: Point):
        def toggle(value: bool) -> bool:
            return not value

        self.modify_area(corner1, corner2, toggle)

    def modify_area(self, corner1: Point, corner2: Point,
                    fun: Callable[[bool], bool]):
        """Modify the area delimited by the corners by applying fun."""
        xmin = min(corner1.x, corner2.x)
        xmax = max(corner1.x, corner2.x) + 1
        ymin = min(corner1.y, corner2.y)
        ymax = max(corner1.y, corner2.y) + 1
        for x_pos in range(xmin, xmax):
            for y_pos in range(ymin, ymax):
                board_idx = self.board_idx(x_pos, y_pos)
                self.board[board_idx] = fun(self.board[board_idx])

    def board_idx(self, x_coord: int, y_coord: int) -> int:
        """The index of the board array represented by x and y coordinates."""
        return y_coord * self.size + x_coord

    def num_lights_lit(self) -> int:
        return sum([1 for light in self.board if light])


class LightBoardBrightnessLevels(LightBoard):
    """A light board featuring lights of varying brightness levels."""

    def __init__(self, size: int):
        self.size = size
        self.board = [0 for i in range(size * size)]

    def turn_on_area(self, corner1: Point, corner2: Point):
        def turn_on(value: int) -> int:
            return value + 1

        self.modify_area(corner1, corner2, turn_on)

    def turn_off_area(self, corner1: Point, corner2: Point):
        def turn_off(value: int) -> int:
            return max(0, value - 1)

        self.modify_area(corner1, corner2, turn_off)

    def toggle_area(self, corner1: Point, corner2: Point):
        def toggle(value: int) -> int:
            return value + 2

        self.modify_area(corner1, corner2, toggle)

    def modify_area(self, corner1: Point, corner2: Point,
                    fun: Callable[[int], int]):
        """Modify the area delimited by the corners by applying fun."""
        xmin = min(corner1.x, corner2.x)
        xmax = max(corner1.x, corner2.x) + 1
        ymin = min(corner1.y, corner2.y)
        ymax = max(corner1.y, corner2.y) + 1
        for x_pos in range(xmin, xmax):
            for y_pos in range(ymin, ymax):
                board_idx = self.board_idx(x_pos, y_pos)
                self.board[board_idx] = fun(self.board[board_idx])

    def board_idx(self, x_coord: int, y_coord: int) -> int:
        """The index of the board array represented by x and y coordinates."""
        return y_coord * self.size + x_coord

    def num_lights_lit(self) -> int:
        return sum([brightness for brightness in self.board])


def part_one(data: str) -> int:
    """Determine the number of lights turned on after following the instructions from data."""
    board = apply_instructions(data, LightBoardOnOff(1000))
    return board.num_lights_lit()


def part_two(data: str) -> int:
    """Determine the number of lights turned on after following the instructions from data."""
    board = apply_instructions(data, LightBoardBrightnessLevels(1000))
    return board.num_lights_lit()


def apply_instructions(data: str, board: LightBoard) -> LightBoard:
    """Apply the given instructions to the light board."""
    for line in data.splitlines():
        point_1, point_2 = extract_points(line)
        if line.startswith("toggle"):
            board.toggle_area(point_1, point_2)
        elif line.startswith("turn on"):
            board.turn_on_area(point_1, point_2)
        elif line.startswith("turn off"):
            board.turn_off_area(point_1, point_2)
        else:
            raise Exception("Unexpected input line: " + line)
    return board


def extract_points(line: str) -> (Point, Point):
    """Extract the rectangle-delimiting points from an input line."""
    search_result = re.search(r'(\d+),(\d+) through (\d+),(\d+)', line)
    point_1 = Point(int(search_result.group(1)), int(search_result.group(2)))
    point_2 = Point(int(search_result.group(3)), int(search_result.group(4)))
    return point_1, point_2


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 6 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
