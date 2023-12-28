from functools import reduce
from util import aoc
from dataclasses import dataclass
from math import gcd


@dataclass
class Module:
    name: str
    outgoing: [str]

    def receive_signal(self, high: bool, origin: str, i: int):
        return [(a, high, self.name) for a in self.outgoing]


@dataclass
class ConjunctionModule(Module):
    state: {str, bool}

    def receive_signal(self, high: bool, origin: str, i: int):
        self.state[origin] = high
        if all(x for x in self.state.values()):
            # if self.name in ['ck', 'cs', 'jh', 'dx']:
            #     print(self.name, i)
            return [(a, False, self.name) for a in self.outgoing]
        else:
            return [(a, True, self.name) for a in self.outgoing]


@dataclass
class FlipModule(Module):
    state: bool = False
    last_change: int = 0

    def receive_signal(self, high: bool, origin: str, i: int):
        if not high:
            self.state = not self.state
            return [(a, self.state, self.name) for a in self.outgoing]
        return []


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def parse_modules(data: str) -> {str, Module}:
    modules = {}
    for line in data.splitlines():
        left, right = line.split(' -> ')
        right = right.split(', ')
        if left[0] == '%':
            modules[left[1:]] = FlipModule(left[1:], right)
        elif left[0] == '&':
            modules[left[1:]] = ConjunctionModule(left[1:], right, {})
        else:
            modules[left] = Module(left, right)
    for m1 in modules:
        for m2 in modules[m1].outgoing:
            if m2 in modules and isinstance(modules[m2], ConjunctionModule):
                modules[m2].state[m1] = False
    return modules


def press_button(modules, i=None):
    queue = [('broadcaster', False, None)]
    high_pulses, low_pulses = 0, 0
    while queue:
        m, signal, origin = queue.pop(0)
        if signal:
            high_pulses += 1
        else:
            low_pulses += 1
        if m in modules:
            queue += modules[m].receive_signal(signal, origin, i)
    return high_pulses, low_pulses


def part_one(data: str) -> int:
    modules = parse_modules(data)
    high_pulses, low_pulses = 0, 0
    for _ in range(1000):
        h, l = press_button(modules)
        high_pulses += h
        low_pulses += l
    return high_pulses * low_pulses


def part_two(data: str) -> int:
    # modules = parse_modules(data)
    # for i in range(1, 5000):
    #     _, _ = press_button(modules, i)

    # answer received from the above
    ans = [3917, 3919, 4007, 4027]
    return reduce(lcm, ans)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 20)
    # print(part_one(input_data))
    print(part_two(input_data))
