from functools import reduce
from util import aoc
from dataclasses import dataclass
import re
from operator import mul


_monkey_regex = "Monkey \d+:\s+" \
                "Starting items: ([\d, ]+)\s+" \
                "Operation: new = old ([+*]) (\d+|old)\s+" \
                "Test: divisible by (\d+)\s+" \
                "If true: throw to monkey (\d+)\s+" \
                "If false: throw to monkey (\d+)"


@dataclass
class Monkey:
    items: list
    operation: str
    operation_left_hand: str
    rule_check: int
    throw_if_true: int
    throw_if_false: int

    inspected: int = 0

    def _new_worry(self, x: int, do_division: bool, total_mod: int) -> int:
        left_hand = x if self.operation_left_hand == 'old' else int(self.operation_left_hand)
        result = x * left_hand if self.operation == '*' else x + left_hand
        result = result // 3 if do_division else result
        return result % total_mod

    def check(self, monkeys: list, do_division: bool, total_mod: int) -> None:
        for item in self.items:
            new_item = self._new_worry(item, do_division, total_mod)
            next_monkey_id = self.throw_if_true if new_item % self.rule_check == 0 else self.throw_if_false
            monkeys[next_monkey_id].items.append(new_item)
            self.inspected += 1
        self.items = []


def parse_data(data: str) -> list[Monkey]:
    monkey_strings = data.split('\n\n')
    monkeys = []
    for monkey_str in monkey_strings:
        match = re.match(_monkey_regex, monkey_str)
        groups = match.groups()
        monkeys.append(Monkey([int(x) for x in groups[0].split(', ')],
                              groups[1],
                              groups[2],
                              int(groups[3]),
                              int(groups[4]),
                              int(groups[5])))
    return monkeys


def simulate(monkeys: list[Monkey], k: int, do_division: bool):
    x = reduce(mul, [m.rule_check for m in monkeys], 1)
    for _ in range(k):
        for monkey in monkeys:
            monkey.check(monkeys, do_division, x)


def solution(monkeys: list[Monkey]) -> int:
    inspected = sorted(m.inspected for m in monkeys)
    return inspected[-1] * inspected[-2]


def part_one(data: str) -> int:
    monkeys = parse_data(data)
    simulate(monkeys, 20, True)
    return solution(monkeys)


def part_two(data: str) -> int:
    monkeys = parse_data(data)
    simulate(monkeys, 10000, False)
    return solution(monkeys)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 11)
    print(part_one(input_data))
    print(part_two(input_data))
