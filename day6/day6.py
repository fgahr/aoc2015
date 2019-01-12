#!/usr/bin/env python

from collections import namedtuple
from typing import Callable
from abc import ABC
from abc import abstractmethod
import re

Point = namedtuple('Point', 'x y')


class LightBoard(ABC):
    @abstractmethod
    def turn_on_area(self, corner1: Point, corner2: Point):
        ...

    @abstractmethod
    def turn_off_area(self, corner1: Point, corner2: Point):
        ...

    @abstractmethod
    def toggle_area(self, corner1: Point, corner2: Point):
        ...

    @abstractmethod
    def num_lights_lit(self) -> int:
        ...


class LightBoardOnOff(LightBoard):
    def __init__(self, size: int):
        self.size = size
        self.board = [False for i in range(size * size)]

    def turn_on_area(self, corner1: Point, corner2: Point):
        def turn_on(value: bool) -> bool:
            return True

        self.modify_area(corner1, corner2, turn_on)

    def turn_off_area(self, corner1: Point, corner2: Point):
        def turn_off(value: bool) -> bool:
            return False

        self.modify_area(corner1, corner2, turn_off)

    def toggle_area(self, corner1: Point, corner2: Point):
        def toggle(value: bool) -> bool:
            return not value

        self.modify_area(corner1, corner2, toggle)

    def modify_area(self, corner1: Point, corner2: Point,
                    fun: Callable[[bool], bool]):
        xmin = min(corner1.x, corner2.x)
        xmax = max(corner1.x, corner2.x) + 1
        ymin = min(corner1.y, corner2.y)
        ymax = max(corner1.y, corner2.y) + 1
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                board_idx = self.board_idx(x, y)
                self.board[board_idx] = fun(self.board[board_idx])

    def board_idx(self, x, y):
        return y * self.size + x

    def num_lights_lit(self) -> int:
        return sum([1 for light in self.board if light == True])


class LightBoardBrightnessLevels(LightBoard):
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
        xmin = min(corner1.x, corner2.x)
        xmax = max(corner1.x, corner2.x) + 1
        ymin = min(corner1.y, corner2.y)
        ymax = max(corner1.y, corner2.y) + 1
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                board_idx = y * self.size + x
                self.board[board_idx] = fun(self.board[board_idx])

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
    for line in data.splitlines():
        p1, p2 = extract_points(line)
        if line.startswith("toggle"):
            board.toggle_area(p1, p2)
        elif line.startswith("turn on"):
            board.turn_on_area(p1, p2)
        elif line.startswith("turn off"):
            board.turn_off_area(p1, p2)
        else:
            raise Exception("Unexpected input line: " + line)
    return board


def extract_points(line: str) -> (Point, Point):
    search_result = re.search(r'(\d+),(\d+) through (\d+),(\d+)', line)
    p1 = Point(int(search_result.group(1)), int(search_result.group(2)))
    p2 = Point(int(search_result.group(3)), int(search_result.group(4)))
    return p1, p2


def read_data() -> str:
    with open('input.txt') as input:
        return input.read()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
