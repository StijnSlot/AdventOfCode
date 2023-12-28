from util import aoc
import re
from dataclasses import dataclass
from math import prod


@dataclass
class Rule:
    dest: str
    check: str = None
    operator: str = None
    cond: int = None

    def get_dest(self, rating: {str, int}):
        if self.cond is None:
            return self.dest
        to_compare = rating[self.check]
        if self.operator == '<' and to_compare < self.cond:
            return self.dest
        if self.operator == '>' and to_compare > self.cond:
            return self.dest
        return None

    def split_ranges(self, ranges):
        new_ranges = {a: b for a, b in ranges.items() if a != self.check}
        inner, outer = (), ()
        a, b = ranges[self.check]
        if self.operator == '<':
            if b < self.cond:
                inner = (a, b)
            elif a > self.cond:
                outer = (a, b)
            else:
                inner = (a, self.cond - 1)
                outer = (self.cond, b)
        else:
            if a > self.cond:
                inner = (a, b)
            elif b < self.cond:
                outer = (a, b)
            else:
                outer = (a, self.cond)
                inner = (self.cond + 1, b)
        return {**new_ranges, self.check: inner}, {**new_ranges, self.check: outer}


@dataclass
class Workflow:
    rules: [Rule]

    def get_dest(self, rating: {str, int}):
        return next(rule.get_dest(rating) for rule in self.rules if rule.get_dest(rating) is not None)

    def is_accepted(self, workflows, rating):
        cur = next(rule.get_dest(rating) for rule in self.rules if rule.get_dest(rating) is not None)
        if cur in ['A', 'R']:
            return cur == 'A'
        return workflows[cur].is_accepted(workflows, rating)


def dfs_ranges(workflows, w, ranges):
    ranges_inner = []
    if w == 'A':
        return [ranges]
    if w == 'R':
        return []
    for r in workflows[w].rules:
        if r.cond is None:
            ranges = dfs_ranges(workflows, r.dest, ranges)
            break
        inner, outer = r.split_ranges(ranges)
        inner_range = dfs_ranges(workflows, r.dest, inner)
        if inner_range:
            ranges_inner += inner_range
        ranges = outer
    if ranges:
        return ranges_inner + ranges
    return ranges_inner


def parse_data(data: str):
    workflows, ratings = {}, []
    workflow_data, rating_data = data.split('\n\n')
    for line in workflow_data.splitlines():
        match = re.match("(\w+){([\w\d<>:,]*),(\w+)}", line)
        cat, rules, last_rule = match.groups()
        rules = [Rule(d, a, b, int(c)) for a, b, c, d in re.findall("(\w+)([<>])(\d+):(\w+)", rules)] + [Rule(last_rule)]
        workflows[cat] = Workflow(rules)
    for line in rating_data.splitlines():
        ratings.append({a: int(b) for a, b in re.findall("(\w+)=(\d+)", line)})
    return workflows, ratings


def part_one(data: str) -> int:
    workflows, ratings = parse_data(data)
    return sum(sum(rating.values()) for rating in ratings if workflows['in'].is_accepted(workflows, rating))


def part_two(data: str) -> int:
    workflows, ratings = parse_data(data)
    ranges = dfs_ranges(workflows, 'in', {x: (1, 4000) for x in 'xmas'})
    # for r in ranges:
    #     print(f'x: {r["x"]}, m: {r["m"]}, a: {r["a"]}, s: {r["s"]}')
    return sum(prod(r[x][1] - r[x][0] + 1 for x in r) for r in ranges)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 19)
    print(part_one(input_data))
    print(part_two(input_data))
