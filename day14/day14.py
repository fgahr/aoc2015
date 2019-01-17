#!/usr/bin/env python
"""Day 14: Reindeer Olympics -- Advent of Code 2015"""

import re
from collections import namedtuple
from itertools import repeat

INPUT = re.compile(r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for ' +
                   r'(?P<fly_duration>\d+) seconds, but then must rest for ' +
                   r'(?P<rest_time>\d+) seconds.')

Reindeer = namedtuple('Reindeer', 'name speed fly_duration rest_time')


def part_one(data: str, travel_time=2503) -> int:
    """The distance the fastest reindeer could traverse in 2503 seconds."""
    distance = lambda r_deer: distance_traveled(r_deer, travel_time)
    return max(map(distance, map(reindeer_from_line, data.splitlines())))

def part_two(data: str, travel_time=2503) -> int:
    """The total score of the winner after 2503 seconds."""
    reindeers = list(map(reindeer_from_line, data.splitlines()))
    names = [r.name for r in reindeers]
    scores = dict(zip(names, repeat(0, len(names))))
    leaders = []
    for time in range(1, travel_time + 1):
        max_distance = 0
        for deer in reindeers:
            distance = distance_traveled(deer, time)
            if distance > max_distance:
                max_distance = distance
                leaders = [deer.name]
            elif distance == max_distance:
                leaders.append(deer.name)
        for leader in leaders:
            scores[leader] += 1

    return max(scores.values())

def reindeer_from_line(line: str) -> Reindeer:
    """A reindeer as described in an input line."""
    match = INPUT.fullmatch(line)
    if not match:
        raise ValueError('Invalid input line: {}'.format(line))
    name = match.group('name')
    speed = int(match.group('speed'))
    fly_duration = int(match.group('fly_duration'))
    rest_time = int(match.group('rest_time'))
    return Reindeer(name, speed, fly_duration, rest_time)


def distance_traveled(reindeer: Reindeer, time: int) -> int:
    """The distance this reindeer can travel in the given time."""
    cycle_duration = reindeer.fly_duration + reindeer.rest_time
    cycle_distance = reindeer.fly_duration * reindeer.speed
    num_full_cycles = time // cycle_duration
    full_cycles_distance = num_full_cycles * cycle_distance
    remaining_time = time % cycle_duration
    # The distance in the last cycle is at most a full cycle distance
    # but can be a fraction thereof.
    remaining_distance = cycle_distance * min(
        1, remaining_time / reindeer.fly_duration)
    return full_cycles_distance + remaining_distance


def read_data() -> str:
    """Read the data from the `input.txt` file."""
    with open('input.txt') as input_file:
        return input_file.read()


def main():
    """Solve the day 14 puzzles."""
    data = read_data()
    print('Part one solution: {}'.format(part_one(data)))
    print('Part two solution: {}'.format(part_two(data)))


if __name__ == '__main__':
    main()
