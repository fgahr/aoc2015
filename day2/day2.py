#!/usr/bin/env python

data = None

def part_one():
    """Determine the total amount of wrapping paper required."""
    total_paper_amount = 0
    for line in data.splitlines():
        total_paper_amount += paper_amount(line)
    print('Part one solution: {}'.format(total_paper_amount))

def paper_amount(line: str) -> int:
    h, w, l = box_dimensions(line)
    front_amount = w*h
    top_amount = w*l
    side_amount = l*h
    extra_amount = min(front_amount, top_amount, side_amount)
    return extra_amount + 2*(front_amount + top_amount + side_amount)

def part_two():
    """Determine the amount of ribbon required."""
    total_ribbon_length = 0
    for line in data.splitlines():
        total_ribbon_length += ribbon_length(line)
    print('Part two solution: {}'.format(total_ribbon_length))

def ribbon_length(line: str) -> int:
    h, w, l = box_dimensions(line)
    # Determine the two smallest sides:
    first_smallest, second_smallest, _ = sorted([h, w, l])
    perimeter = 2*(first_smallest + second_smallest)
    volume = h*w*l
    return perimeter + volume

def box_dimensions(line: str) -> (int, int, int):
    return [int(num) for num in line.split('x')]

def read_data():
    global data
    with open('input.txt') as input:
        data = input.read()

def main():
    read_data()
    part_one()
    part_two()

if __name__ == '__main__':
    main()
