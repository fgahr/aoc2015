#!/usr/bin/env python


def part_one(data: str) -> int:
    """Determine the total amount of wrapping paper required."""
    total_paper_amount = 0
    for box in data.splitlines():
        total_paper_amount += paper_amount(box)
    return total_paper_amount


def paper_amount(box: str) -> int:
    h, w, l = dimensions(box)
    front_amount = w * h
    top_amount = w * l
    side_amount = l * h
    extra_amount = min(front_amount, top_amount, side_amount)
    return extra_amount + 2 * (front_amount + top_amount + side_amount)


def part_two(data: str) -> int:
    """Determine the amount of ribbon required."""
    total_ribbon_length = 0
    for box in data.splitlines():
        total_ribbon_length += ribbon_length(box)
    return total_ribbon_length


def ribbon_length(box: str) -> int:
    h, w, l = dimensions(box)
    # Determine the two smallest sides:
    first_smallest, second_smallest, _ = sorted([h, w, l])
    perimeter = 2 * (first_smallest + second_smallest)
    volume = h * w * l
    return perimeter + volume


def dimensions(box: str) -> (int, int, int):
    return [int(num) for num in box.split('x')]


def read_data() -> str:
    with open('input.txt') as input:
        return input.read()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
