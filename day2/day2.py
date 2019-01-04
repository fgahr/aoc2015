#!/usr/bin/env python

data = None

def part_one():
    """Determine the total amount of wrapping paper required."""
    total_paper_amount = 0
    for line in data.splitlines():
        total_paper_amount += paper_amount(line)
    print('Part one solution: {}'.format(total_paper_amount))

def paper_amount(line: str) -> int:
    # Box dimensions
    h, w, l = [int(num) for num in line.split('x')]
    front_amount = w*h
    top_amount = w*l
    side_amount = l*h
    extra_amount = min(front_amount, top_amount, side_amount)
    return extra_amount + 2*(front_amount + top_amount + side_amount)

def read_data():
    global data
    with open('input.txt') as input:
        data = input.read().rstrip()

def main():
    read_data()
    part_one()

if __name__ == '__main__':
    main()
