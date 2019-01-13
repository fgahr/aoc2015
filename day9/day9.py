#!/usr/bin/env python

import re
import itertools

input_pattern = re.compile(r'(?P<src>\w+) to (?P<dest>\w+) = (?P<dist>\d+)')


def part_one(data: str) -> int:
    """Determine the shortest path given distances from data."""
    places = []
    distances = {}
    min_distance = 0
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
        # Make sure we have a reasonable (high) starting point later.
        min_distance += dist

    for route in list(itertools.permutations(places)):
        route_distance = 0
        previous = None
        for current in route:
            if not previous:
                previous = current
                continue
            route_distance += distances[previous][current]
            previous = current
        min_distance = min(min_distance, route_distance)
    return min_distance


def parse_line(line: str) -> (str, str, int):
    """Get source, destination, and distance from an input line."""
    m = input_pattern.fullmatch(line)
    return (m.group('src'), m.group('dest'), int(m.group('dist')))


def read_data() -> str:
    with open('input.txt') as input:
        return input.read()


def main():
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))


if __name__ == '__main__':
    main()
