#!/usr/bin/env python
"""Day 9: All in a Single Night -- Advent of Code 2015"""

from typing import Callable
from typing import Mapping
from typing import List
import re
import itertools

INPUT_PATTERN = re.compile(r'(?P<src>\w+) to (?P<dest>\w+) = (?P<dist>\d+)')


def part_one(data: str) -> int:
    """Determine the shortest path given distances from data."""
    return examine_routes(data, min)


def part_two(data: str) -> int:
    """Determine the shortest path given distances from data."""
    return examine_routes(data, max)


def examine_routes(data: str, selector: Callable[[int, int], int]) -> int:
    """From the routes in data, select a length based on the given function."""
    places = []
    distances = {}
    for line in data.splitlines():
        source, destination, dist = parse_line(line)
        if source not in places:
            places.append(source)
        if destination not in places:
            places.append(destination)
        if source not in distances.keys():
            distances[source] = {}
        if destination not in distances.keys():
            distances[destination] = {}
        # Store distances both ways for convenience.
        distances[source][destination] = dist
        distances[destination][source] = dist

    # Distance of route as encountered in input; starting point for optimization.
    extremal_distance = route_distance(places, distances)
    for route in list(itertools.permutations(places)):
        extremal_distance = selector(extremal_distance,
                                     route_distance(route, distances))
    return extremal_distance


def route_distance(route: List[str],
                   distances: Mapping[str, Mapping[str, int]]) -> int:
    """The cumulative distance following the given route."""
    distance = 0
    previous = None
    for current in route:
        if not previous:
            previous = current
            continue
        distance += distances[previous][current]
        previous = current
    return distance


def parse_line(line: str) -> (str, str, int):
    """Get source, destination, and distance from an input line."""
    match = INPUT_PATTERN.fullmatch(line)
    return (match.group('src'), match.group('dest'), int(match.group('dist')))


def read_data() -> str:
    """Read the data from the input file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 9 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
