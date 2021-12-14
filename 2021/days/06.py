from util import aoc


def get_fish(data: str) -> dict[int, int]:
    nums = data.split(",")
    return {int(num): nums.count(num) for num in set(nums)}


def simulate(fish: dict[int, int], days: int) -> dict[int, int]:
    for _ in range(days):
        fish = {num-1: fish[num] for num in fish}
        if -1 in fish:
            fish[8] = fish[-1]
            fish[6] = fish[6] + fish[-1] if 6 in fish else fish[-1]
            fish.pop(-1)
    return fish


def part_one(data: str) -> int:
    fish = simulate(get_fish(data), 80)
    return sum(fish[num] for num in fish)


def part_two(data: str) -> int:
    fish = simulate(get_fish(data), 256)
    return sum(fish[num] for num in fish)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 6)
    print(part_one(input_data))
    print(part_two(input_data))
