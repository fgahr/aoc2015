#!/usr/bin/env python
"""This module solves the day 11 problems of Advent of Code 2015."""

from typing import List, Iterable, TypeVar

T = TypeVar('T')

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_SIZE = len(ALPHABET)


def next_valid_password(data: str) -> str:
    """The next valid password, starting from data."""
    password = next_password(password_to_number(data))
    while not is_valid_password(password):
        password = next_password(password)
    return number_to_password(password)


def next_password(password: List[int]) -> List[int]:
    """The next possible password, disregarding validity checks."""
    digit_max = ALPHABET_SIZE - 1
    password_length = len(password)
    # If we are missing one or two letter pairs, we can skip incrementing the
    # last few digits
    skip_digits = digits_to_skip(num_distinct_letter_pairs(password))
    start = password_length - 1 - skip_digits
    for i in range(start + 1, password_length):
        password[i] = 0
    for i in range(start, -1, -1):
        if password[i] < digit_max:
            password[i] = next_legal_char(password[i])
            return password
        password[i] = 0
    raise OverflowError('Passwords exceeding length of starting value.')


def digits_to_skip(distinct_letter_pairs: int) -> int:
    """The number of letters which can be skipped (i.e. not being incremented
    one by one) depending on the number of distinct letter pairs present."""
    if distinct_letter_pairs == 0:
        # If no letter pair exists already, we know at least one must be
        # among the last two digits. Hence we can set those to 0 and continue
        # from there.
        return 2
    # No optimization possible, have to start at the end.
    return 0

def is_valid_password(password: List[int]) -> bool:
    """True if the list represents a valid password."""
    return has_no_illegal_char(password) and has_ascending_sequence(
        password, 3) and num_distinct_letter_pairs(password) > 1


def has_no_illegal_char(password: List[int]) -> bool:
    """True if the password contains none of the illegal chars."""
    return not any(is_illegal_char(char) for char in password)


def is_illegal_char(char: int) -> bool:
    """True if char is the base-26 representation of one of i, o, l."""
    if char in [8, 11, 14]:  # i, l, o
        return True
    return False


def next_legal_char(char: int) -> int:
    """The next legal character after char."""
    if char in [7, 10, 13]:  # h, k, n
        return char + 2  # skip i, l, o
    return char + 1


def has_ascending_sequence(password: List[int], length: int) -> bool:
    """True if the sequence has an ascending subsequence of given length."""
    return any(is_ascending(p) for p in partition(password, length))


def num_distinct_letter_pairs(password: List[int]) -> int:
    """True if the given password has at least two distinct letter pairs."""
    is_pair = lambda p: p[0] == p[1]
    first = lambda p: p[0]
    return len(set(map(first, filter(is_pair, partition(password, 2)))))


def is_ascending(seq: List[int]) -> bool:
    """True if the sequence is ascending in steps of 1."""
    if len(seq) < 2:
        return True
    return (seq[1] == seq[0] + 1) and is_ascending(seq[1:])


def partition(elements: List[T], group_size: int) -> Iterable[List[T]]:
    """Partition a list in groups of the given group_size."""
    for i in range(0, len(elements) + 1 - group_size):
        yield elements[i:(i + group_size)]


def password_to_number(word: str) -> List[int]:
    """Translate a word string to a base-26 number."""
    return list(map(char_to_digit, word))


def char_to_digit(char: str) -> int:
    """Translate a char to the corresponding base-26 digit."""
    mapping = dict(zip(ALPHABET, range(0, ALPHABET_SIZE)))
    return mapping[char]


def number_to_password(number: List[int]) -> str:
    """Translate a base-26 number to the corresponding string."""
    return ''.join(list(map(digit_to_char, number)))


def digit_to_char(digit: int) -> str:
    """Translate a base-26 digit to the corresponding character."""
    return ALPHABET[digit]


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.readline().rstrip()


def main():
    """Solve the day 11 puzzles."""
    data = read_data()
    p1_solution = next_valid_password(data)
    p2_solution = next_valid_password(p1_solution)
    print('Part one solution: {}'.format(p1_solution))
    print('Part two solution: {}'.format(p2_solution))


if __name__ == '__main__':
    main()
