#!/usr/bin/env python

def part_one(data: str) -> int:
    """Determine the number of nice strings in the data."""
    num_nice_strings = 0
    for line in data.splitlines():
        if is_nice_string(line):
            num_nice_strings += 1
    return num_nice_strings

def is_nice_string(string: str) -> bool:
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

def is_illegal_sequence(seq: str) -> bool:
    return seq == 'ab' or seq== 'cd' or seq == 'pq' or seq == 'xy'

def is_vowel(char: str) -> bool:
    return 'aeiou'.count(char) > 0

def read_data() -> str:
    with open('input.txt') as input:
        return input.read()

def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))

if __name__ == '__main__':
    main()
