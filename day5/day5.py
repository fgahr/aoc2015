#!/usr/bin/env python
"""Day 5: Doesn't He Have Intern-Elves For This? -- Advent of Code 2015"""

from typing import Callable


def part_one(data: str) -> int:
    """Determine the number of nice strings in the data."""
    return num_lines_satisfying(data, is_nice_part_one)


def part_two(data: str) -> int:
    """Determine the number of nice strings in the data."""
    return num_lines_satisfying(data, is_nice_part_two)


def num_lines_satisfying(data: str, pred: Callable[[str], bool]) -> int:
    """The number of lines in data which satisfy the predicate pred."""
    return len(list(filter(pred, data.splitlines())))


def is_nice_part_one(string: str) -> bool:
    """True of the string is nice according to part one rules."""
    num_vowels = 0
    has_double_letter = False
    previous_char = ''
    for char in string:
        if is_illegal_sequence(previous_char + char):
            return False
        if is_vowel(char):
            num_vowels += 1
        if previous_char == char:
            has_double_letter = True
        previous_char = char
    return has_double_letter and (num_vowels > 2)


def is_nice_part_two(string: str) -> bool:
    """True of the string is nice according to part two rules."""
    has_double_letter_with_separator = False
    has_repeated_pair = False
    for i, _ in enumerate(string):
        if i > 1 and string[i] == string[i - 2]:
            has_double_letter_with_separator = True
        if i > 0 and pair_at_index_occurs_in_tail(i, string):
            has_repeated_pair = True
    return has_double_letter_with_separator and has_repeated_pair


def pair_at_index_occurs_in_tail(i: int, string: str) -> bool:
    """True if the pair ending at the given index also occurs in its tail."""
    pair = string[i - 1] + string[i]
    tail = string[(i + 1):]
    return pair in tail


def is_illegal_sequence(seq: str) -> bool:
    """True if seq is one of the forbidden sequences."""
    return seq in ['ab', 'cd', 'pq', 'xy']


def is_vowel(char: str) -> bool:
    """True if char is a vowel."""
    return char in 'aeiou'


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 5 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
