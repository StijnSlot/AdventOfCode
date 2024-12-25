from util import aoc
from dataclasses import dataclass
from itertools import combinations
import random


@dataclass
class Gate:
    operand: str
    in1: str
    in2: str
    out: str

    def execute(self, wires: {str: bool}) -> bool:
        if self.in1 not in wires or self.in2 not in wires or self.out in wires:
            return False
        if self.operand == 'AND':
            wires[self.out] = wires[self.in1] and wires[self.in2]
        elif self.operand == 'OR':
            wires[self.out] = wires[self.in1] or wires[self.in2]
        else:
            wires[self.out] = wires[self.in1] ^ wires[self.in2]
        return True


def read_data(data: str) -> ({str, bool}, [Gate]):
    part1, part2 = data.split('\n\n')
    wires, gates = {}, []
    for line in part1.splitlines():
        a, b = line.split(': ')
        wires[a] = bool(int(b))
    for line in part2.splitlines():
        parts = line.split()
        gates.append(Gate(parts[1], parts[0], parts[2], parts[4]))
    return wires, gates


def simulate(wires: {str, bool}, gates: [Gate]):
    while any(gate.execute(wires) for gate in gates):
        pass


def to_num_str(wires: {str, bool}, letter: chr) -> str:
    Z = reversed(sorted(z for z in wires if z[0] == letter))
    return ''.join('1' if wires[z] else '0' for z in Z)


def swap(gates: [Gate], out_a: str, out_b: str):
    a = next(gate for gate in gates if gate.out == out_a)
    b = next(gate for gate in gates if gate.out == out_b)
    a.out = out_b
    b.out = out_a


def part_one(data: str) -> int:
    wires, gates = read_data(data)
    simulate(wires, gates)
    return int(to_num_str(wires, 'z'), 2)


def part_two(data: str) -> str:
    original_wires, gates = read_data(data)
    swap(gates, 'z39', 'jct')
    swap(gates, 'z21', 'rcb')
    swap(gates, 'z09', 'gwh')
    swap(gates, 'wbw', 'wgb')

    # prints any incorrect additions for a single bit position -> x_n + y_n != z_n, z_n+1
    for i in range(45):
        for xi, yi in ((False, False), (True, False), (False, True), (True, True)):
            wires = {**{f'x{i:02}': False for i in range(45)},
                     **{f'y{i:02}': False for i in range(45)},
                     f'x{i:02}': xi,
                     f'y{i:02}': yi}
            simulate(wires, gates)
            if wires[f'z{i:02}'] != xi ^ yi or wires[f'z{i+1:02}'] != xi and yi:
                print(f'x{i:02}', wires[f'x{i:02}'])
                print(f'y{i:02}', wires[f'y{i:02}'])
                print(f'z{i:02}', wires[f'z{i:02}'])
                print(f'z{i+1:02}', wires[f'z{i+1:02}'])
                print()

    return ','.join(sorted(('z39', 'jct', 'z21', 'rcb', 'z09', 'gwh', 'wbw', 'wgb')))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 24)
    print(part_one(input_data))
    print(part_two(input_data))
