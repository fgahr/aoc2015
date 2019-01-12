#!/usr/bin/env python


def part_one(data: str) -> int:
    """Determine the difference between raw and parsed string length in data."""
    sum_difference = 0
    for line in data.splitlines():
        sum_difference += len(line) - parsed_length(line)
    return sum_difference


def part_two(data: str) -> int:
    """Determine the difference between raw and escaped string length in data."""
    sum_difference = 0
    for line in data.splitlines():
        sum_difference += escaped_length(line) - len(line)
    return sum_difference


def parsed_length(line: str) -> int:
    return len(eval(line))

def escaped_length(line: str) -> int:
    return len(line) + 2 + line.count(r'"') + line.count('\\')

def read_data() -> str:
    with open('input.txt') as input:
        return input.read()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
