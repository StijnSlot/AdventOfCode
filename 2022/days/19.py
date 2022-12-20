from util import aoc
import re
from dataclasses import dataclass
from operator import mul
from functools import reduce


@dataclass
class Robot:
    makes: str
    costs: list[tuple[str, int]]
    max_nr: int = 99999


def update_items(items, creates, robot=None):
    new_items = {**items}
    for c in creates:
        new_items[c] += creates[c]
    if robot is not None:
        for c, k in robot.costs:
            new_items[c] -= k
    return new_items


def update_creates(creates, robot):
    new_creates = {**creates}
    new_creates[robot.makes] += 1
    return new_creates


def remove_items(items, creates):
    new_items = {**items}
    for c in creates:
        new_items[c] -= creates[c]
    return new_items


def quality(blueprint, minutes, items, creates):
    if minutes <= 0:
        return items['geode']
    result = 0
    old_items = remove_items(items, creates)

    # buy other robots
    for robot in blueprint[::-1]:
        # dont create robot if already at max nr or could already buy before
        if creates[robot.makes] < robot.max_nr and \
                all(items[c] >= k for c, k in robot.costs) and \
                not all(old_items[c] >= k for c, k in robot.costs):
            result = max(result, quality(blueprint,
                                         minutes - 1,
                                         update_items(items, creates, robot),
                                         update_creates(creates, robot)))

    return max(result, quality(blueprint,
                               minutes - 1,
                               update_items(items, creates),
                               creates))


def read_data(data: str):
    blueprints = []
    re_str = "(Blueprint (\w+): )*Each (\w+) robot costs (\d+) (\w+)( and (\d+) (\w+))*"
    for line in data.splitlines():
        robot_strs = line.split('. ')
        robots = []
        for x in robot_strs:
            match = re.match(re_str, x)
            a = match.groups()
            creates = a[2]
            costs = [(a[4], int(a[3]))]
            if a[5] is not None:
                costs.append((a[7], int(a[6])))
            robots.append(Robot(creates, costs))
        for robot in robots:
            if robot.makes == 'geode':
                continue
            robot.max_nr = max(k for robot2 in robots for c, k in robot2.costs if c == robot.makes)
        blueprints.append(robots)

    return blueprints


def simulate(blueprints, minutes):
    results = []
    for i, blueprint in enumerate(blueprints):
        creates = {robot.makes: 0 for robot in blueprint}
        items = {**creates}
        creates['ore'] = 1
        results.append(quality(blueprint, minutes, items, creates))
    return results


def part_one(data: str) -> int:
    blueprints = read_data(data)
    return sum((i + 1) * x for i, x in enumerate(simulate(blueprints, 24)))


def part_two(data: str) -> int:
    blueprints = read_data(data)
    return reduce(mul, simulate(blueprints, 32))


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 19)
    print(part_one(input_data))
    print(part_two(input_data))
