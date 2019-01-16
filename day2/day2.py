#!/usr/bin/env python
"""Day 2: I Was Told There Would Be No Math -- Advent of Code 2015"""


def part_one(data: str) -> int:
    """Determine the total amount of wrapping paper required."""
    total_paper_amount = 0
    for box in data.splitlines():
        total_paper_amount += paper_amount(box)
    return total_paper_amount


def part_two(data: str) -> int:
    """The amount of ribbon required for a box described in ."""
    total_ribbon_length = 0
    for box in data.splitlines():
        total_ribbon_length += ribbon_length(box)
    return total_ribbon_length


def paper_amount(box: str) -> int:
    """The amount of paper required for the boxes described in data."""
    height, width, length = dimensions(box)
    front_amount = width * height
    top_amount = width * length
    side_amount = length * height
    extra_amount = min(front_amount, top_amount, side_amount)
    return extra_amount + 2 * (front_amount + top_amount + side_amount)


def ribbon_length(box: str) -> int:
    """The amount of ribbon required for the boxes described in data."""
    height, width, length = dimensions(box)
    # Determine the two smallest sides:
    first_smallest, second_smallest, _ = sorted([height, width, length])
    perimeter = 2 * (first_smallest + second_smallest)
    volume = height * width * length
    return perimeter + volume


def dimensions(box: str) -> (int, int, int):
    """The dimensions of the box described in height,width,length format."""
    return [int(num) for num in box.split('x')]


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 2 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
