from util import aoc
from dataclasses import dataclass
from typing import Optional


@dataclass
class Monkey:
    name: str
    number: Optional[int]
    operation: Optional[str]
    left: Optional[str]
    right: Optional[str]


def operation(op: str, left: int, right: int):
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left // right


def solution(monkeys: dict[str, Monkey], x: str):
    monkey = monkeys[x]
    if monkey.number is not None:
        return monkey.number
    a, b = solution(monkeys, monkey.left), solution(monkeys, monkey.right)
    monkey.number = operation(monkey.operation, a, b)
    return monkey.number


def solution_part_two(monkeys: dict[str, Monkey]):
    a, b = monkeys['root'].left, monkeys['root'].right
    x, y, h = 0, 999999999999999, 0
    sol_left, sol_right = solution(monkeys, a), solution(monkeys, b)
    while sol_left != sol_right:
        # reset
        for i in monkeys:
            if monkeys[i].operation is not None:
                monkeys[i].number = None
        h = (x + y) // 2
        monkeys['humn'].number = h
        sol_left, sol_right = solution(monkeys, a), solution(monkeys, b)
        if sol_left > sol_right:
            x = h
        elif sol_left < sol_right:
            y = h
    return h


def parse_data(data: str):
    monkeys = {}
    for line in data.splitlines():
        a, b = line.split(': ')
        if ' ' in b:
            b1, b2, b3 = b.split()
            monkey = Monkey(a, None, b2, b1, b3)
        else:
            monkey = Monkey(a, int(b), None, None, None)
        monkeys[a] = monkey
    return monkeys


def part_one(data: str) -> int:
    monkeys = parse_data(data)
    return solution(monkeys, 'root')


def part_two(data: str) -> int:
    monkeys = parse_data(data)
    return solution_part_two(monkeys)


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 21)
    print(part_one(input_data))
    print(part_two(input_data))
