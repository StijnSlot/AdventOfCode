from util import aoc
from dataclasses import dataclass
import re

MAX_PRESS = 100
GAME_REGEX = re.compile("Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Game:
    button_a: Point
    button_b: Point
    goal: Point

    def __init__(self, game_str):
        groups = GAME_REGEX.match(game_str).groups()
        self.button_a = Point(int(groups[0]), int(groups[1]))
        self.button_b = Point(int(groups[2]), int(groups[3]))
        self.goal = Point(int(groups[4]), int(groups[5]))

    def solve(self, start=0, max_press=MAX_PRESS):
        min_cost, i = 999999999999999, 0
        visited = []  # to stop looping if no possible solution for X is found after 100 steps
        while i < start + max_press and self.goal.x >= self.button_a.x * i and len(visited) < 100:
            rem_x = self.goal.x - self.button_a.x * i
            j = rem_x // self.button_b.x
            a = rem_x % self.button_b.x
            visited.append(a)
            if a == 0:
                visited = []
                dif = self.goal.y - (self.button_a.y * i + self.button_b.y * j)
                # print(i, dif)
                if dif == 0:
                    min_cost = min(min_cost, 3*i + j)
                elif abs(dif) > 10000:
                    i += abs(dif) // 1000
            i += 1
        return min_cost if min_cost != 999999999999999 else None


def part_one(data: str) -> int:
    games = [Game(game_str) for game_str in data.split('\n\n')]
    return sum(game.solve() or 0 for game in games)


def part_two(data: str) -> int:
    games = [Game(game_str) for game_str in data.split('\n\n')]
    total = 0
    for game in games:
        game.goal = Point(game.goal.x + 10000000000000, game.goal.y + 10000000000000)
        total += game.solve(max_press=10000000000000) or 0
    return total


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 13)
    # print(part_one(input_data))
    print(part_two(input_data))
