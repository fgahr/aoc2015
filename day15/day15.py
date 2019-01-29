#!/usr/bin/env python
"""Day 15: Science for Hungry People -- Advent of Code 2015"""

from typing import List
import re
import itertools

from collections import namedtuple

Ingredient = namedtuple('Ingredient',
                        'name capacity durability flavor texture calories')


def part_one(data: str) -> int:
    """The best possible cookie score given the ingredient properties from data."""
    total_quantity = 100
    ingredients = [parse_ingredient(line) for line in data.splitlines()]
    # There are 4 ingredients total in the input, so nothing is lost here.
    quantities = [total_quantity // len(ingredients) for _ in ingredients]
    while True:
        next_quantities = max_neighboring_quantities(ingredients, quantities)
        if next_quantities == quantities:
            # Reached maximum point
            return dough_score(ingredients, quantities)
        quantities = next_quantities


def max_neighboring_quantities(ingredients: List[Ingredient],
                               quantities: List[int]) -> List[int]:
    """The quantities yielding the best dough, varying the given
    quantities in small steps."""
    indices = range(0, len(quantities))
    best_neighbor = quantities
    best_score = dough_score(ingredients, quantities)
    for plus, minus in itertools.product(indices, indices):
        if plus == minus:
            continue
        quants = [q for q in quantities]
        if quants[plus] == 100 or quants[minus] == 0:
            continue
        quants[plus] += 1
        quants[minus] -= 1
        varied_score = dough_score(ingredients, quants)
        if varied_score > best_score:
            best_score = varied_score
            best_neighbor = quants
    return best_neighbor


def dough_score(ingredients: List[Ingredient], quantities: List[int]) -> int:
    """The score of the dough described by the ingredients and quantities."""
    capacity, durability, flavor, texture = 0, 0, 0, 0
    for count, ingredient in enumerate(ingredients):
        quantity = quantities[count]
        capacity += ingredient.capacity * quantity
        durability += ingredient.durability * quantity
        flavor += ingredient.flavor * quantity
        texture += ingredient.texture * quantity
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    return max(0, capacity * durability * flavor * texture)


def parse_ingredient(line: str) -> Ingredient:
    """Parse an ingredient description from the input."""
    pattern = re.compile(
        r'(?P<name>\w+): capacity (?P<cap>-?\d+), durability (?P<dur>-?\d+), ' +
        r'flavor (?P<fla>-?\d+), texture (?P<tex>-?\d+), ' +
        r'calories (?P<cal>-?\d+)')
    match = pattern.fullmatch(line)
    name = match.group('name')
    capacity = int(match.group('cap'))
    durability = int(match.group('dur'))
    flavor = int(match.group('fla'))
    texture = int(match.group('tex'))
    calories = int(match.group('cal'))
    return Ingredient(
        name=name,
        capacity=capacity,
        durability=durability,
        flavor=flavor,
        texture=texture,
        calories=calories)


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 15 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
