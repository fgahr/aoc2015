#!/usr/bin/env python

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
    has_double_letter_with_separator = False
    has_repeated_pair = False
    for i in range(len(string)):
        if i > 1 and string[i] == string[i - 2]:
            has_double_letter_with_separator = True
        if i > 0 and pair_at_index_occurs_in_tail(i, string):
            has_repeated_pair = True
    return has_double_letter_with_separator and has_repeated_pair

def pair_at_index_occurs_in_tail(i: int, string: str) -> bool:
    pair = string[i-1] + string[i]
    tail = string[(i+1):]
    return pair in tail

def is_illegal_sequence(seq: str) -> bool:
    return seq == 'ab' or seq== 'cd' or seq == 'pq' or seq == 'xy'

def is_vowel(char: str) -> bool:
    return char in 'aeiou'

def read_data() -> str:
    with open('input.txt') as input:
        return input.read()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))

if __name__ == '__main__':
    main()
