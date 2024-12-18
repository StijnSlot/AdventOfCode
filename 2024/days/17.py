from typing import Optional
from util import aoc
from dataclasses import dataclass
import re
from collections import deque


INPUT_REGEX = re.compile("Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)")


@dataclass
class ProgramState:
    reg_a: int
    reg_b: int
    reg_c: int
    instr_pointer: int = 0

    def reset(self, reg_a: int):
        self.reg_a = reg_a
        self.reg_b = 0
        self.reg_c = 0
        self.instr_pointer = 0

    def combo(self, operand: int):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.reg_a
        elif operand == 5:
            return self.reg_b
        elif operand == 6:
            return self.reg_c
        raise NotImplementedError()

    def do_operation(self, opcode: int, operand: int) -> Optional[int]:
        if opcode == 0:
            self.reg_a = self.reg_a // (2 ** self.combo(operand))
        elif opcode == 1:
            self.reg_b = self.reg_b ^ operand
        elif opcode == 2:
            self.reg_b = self.combo(operand) % 8
        elif opcode == 3:
            if self.reg_a != 0:
                self.instr_pointer = operand - 2
        elif opcode == 4:
            self.reg_b = self.reg_b ^ self.reg_c
        elif opcode == 5:
            return self.combo(operand) % 8
        elif opcode == 6:
            self.reg_b = self.reg_a // (2 ** self.combo(operand))
        elif opcode == 7:
            self.reg_c = self.reg_a // (2 ** self.combo(operand))
        return None


def read_data(data: str) -> (ProgramState, list[int]):
    a, b, c, program = INPUT_REGEX.match(data).groups()
    return ProgramState(int(a), int(b), int(c)), [int(x) for x in program.split(',')]


def run_program(state: ProgramState, program: [int]) -> [int]:
    output = []
    while 0 <= state.instr_pointer < len(program) - 1:
        opcode = program[state.instr_pointer]
        operand = program[state.instr_pointer + 1]
        out = state.do_operation(opcode, operand)
        if out is not None:
            output.append(out)
        state.instr_pointer += 2
    return output


def part_one(data: str) -> str:
    state, program = read_data(data)
    output = run_program(state, program)
    return ",".join(str(x) for x in output)


def part_two(data: str) -> int:
    state, program = read_data(data)
    Q = deque()
    for i in range(8):
        Q.append(i)
    while len(Q) > 0:
        i = Q.popleft()
        state.reset(i)
        output = run_program(state, program)
        if output == program:
            return i
        if output[1:] == program[-len(output)+1:]:
            Q.append(i + 1)  # keep searching for as long as the output is almost right
        if output == program[-len(output):]:
            Q.append(i * 8)
    return -1


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 17)
    print(part_one(input_data))
    print(part_two(input_data))
