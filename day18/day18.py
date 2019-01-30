#!/usr/bin/env python
"""Day 18: Like a GIF For Your Yard -- Advent of Code 2015"""

from typing import List, TypeVar

T = TypeVar('T')


def part_one(data: str, size=100, steps=100) -> int:
    """The number of burning lights on the board from data after the given
    number of steps."""
    board = parse_board(data)
    for _ in range(0, steps):
        board = next_board(board, size)
    return num_lights(board)


def part_two(data: str, size=100, steps=100) -> int:
    """The number of burning lights on the defective board after the given
    number of steps.

    The defect manifests itself in that the four corner lights are always
    turned on."""
    board = parse_board(data)
    board[0][0] = True
    board[0][size - 1] = True
    board[size - 1][0] = True
    board[size - 1][size - 1] = True

    for _ in range(0, steps):
        board = next_board(board, size)
        board[0][0] = True
        board[0][size - 1] = True
        board[size - 1][0] = True
        board[size - 1][size - 1] = True
    return num_lights(board)


def next_board(board: List[List[bool]], size: int) -> List[List[bool]]:
    """The board in the next step of the animation.
    It is based on the currently burning lights."""
    neighbors = neighbors_board(board, size)
    new_board = empty_board(False, size)
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] and neighbors[i][j] in [2, 3]:
                new_board[i][j] = True
            if not board[i][j] and neighbors[i][j] == 3:
                new_board[i][j] = True
    return new_board


def neighbors_board(board: List[List[bool]], size: int) -> List[List[int]]:
    """The number of turned on neighboring lights for each cell of the board."""
    neighbors = empty_board(0, size)
    for i in range(0, size):
        for j in range(0, size):
            neighbors[i][j] = num_neighbors(i, j, size, board)
    return neighbors


def num_neighbors(i: int, j: int, size: int, board: List[List[bool]]) -> int:
    """The number of burning lights around i, j on the board of given size."""
    i_from, i_to = max(0, i - 1), min(size - 1, i + 1)
    j_from, j_to = max(0, j - 1), min(size - 1, j + 1)
    neighbors = 0
    for i_iter in range(i_from, i_to + 1):
        for j_iter in range(j_from, j_to + 1):
            if i_iter == i and j_iter == j:
                continue
            if board[i_iter][j_iter]:
                neighbors += 1
    return neighbors


def num_lights(board: List[List[bool]]) -> int:
    """The number of burning lights on the board."""
    return sum([sum(row) for row in board])


def parse_board(data: str) -> List[List[bool]]:
    """Parse the board from data."""

    def on_or_off(token: str) -> bool:
        """Parse a token from data as a light turned on/off."""
        if token == '#':
            return True
        if token == '.':
            return False
        raise ValueError('Invalid token: {}'.format(token))

    def parse_line(line: str) -> List[bool]:
        """Parse a line from data as a row of the board."""
        return list(map(on_or_off, line))

    return list(map(parse_line, data.splitlines()))


def board_to_str(board: List[List[bool]]) -> str:
    """Obtain the string representation of a board. Useful for debugging."""

    def light_to_token(light: bool) -> str:
        if light:
            return '#'
        return '.'

    def row_to_str(row: List[bool]) -> str:
        return ''.join(list(map(light_to_token, row)))

    return '\n'.join(list(map(row_to_str, board)))


def empty_board(value: T, size: int) -> List[List[T]]:
    """An board, initialized to value."""

    def empty_row():
        return list(map(lambda _: value, range(0, size)))

    return list(map(lambda _: empty_row(), range(0, size)))


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 18 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
