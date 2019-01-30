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
        # The scoring function is convex (or rather, its negative is). Hence
        # we can trace a path to the maximum by following local adjustments.
        next_quantities = max_neighboring_quantities(ingredients, quantities)
        if next_quantities == quantities:
            # Reached maximum point
            return dough_score(ingredients, quantities)
        quantities = next_quantities


def part_two(data: str) -> int:
    """The best possible score of 500 calories cookies given the input data."""
    total_quantity = 100
    calory_goal = 500
    by_calories_asc = lambda ingredient: -ingredient.calories
    ingredients = [parse_ingredient(line) for line in data.splitlines()]
    ingredients.sort(key=by_calories_asc)
    calories = [ingredient.calories for ingredient in ingredients]

    # FIXME: This code produces the right answer, but poorly.
    # It is slow and is limited to working properly with four ingredients.
    # This assumption is violated in the test, although it passes regardless.
    # Also, if there were only one ingredient with non-zero calories, it would
    # break.
    best_score = 0
    for i in range(0, calory_goal // calories[0]):
        remaining_calories = calory_goal - i * calories[1]
        for j in range(0, remaining_calories // calories[1]):
            remaining_ingredients = total_quantity - i - j
            for k in range(0, remaining_ingredients + 1):
                for l in range(0, remaining_ingredients - k + 1):
                    quantities = [i, j, k, l]
                    total_calories = sum(
                        [q * c for q, c in zip(quantities, calories)])
                    if total_calories == 500:
                        best_score = max(best_score,
                                         dough_score(ingredients, quantities))

    return best_score


def max_neighboring_quantities(ingredients: List[Ingredient],
                               quantities: List[int]) -> List[int]:
    """The quantities yielding the best dough, varying the given
    quantities in small steps."""
    indices = range(0, len(quantities))
    best_neighbor = quantities
    best_score = dough_score(ingredients, quantities)
    for plus, minus in itertools.product(indices, repeat=2):
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
        r'(?P<name>\w+): capacity (?P<cap>-?\d+), durability (?P<dur>-?\d+), '
        + r'flavor (?P<fla>-?\d+), texture (?P<tex>-?\d+), ' +
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
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
