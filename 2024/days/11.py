from util import aoc


def simulate_step(stones: {int: int}) -> {int: int}:
    new_stones = {}
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] = count + (new_stones[1] if 1 in new_stones else 0)
        elif len(str(stone)) % 2 == 0:
            l2 = len(str(stone)) // 2
            left, right = int(str(stone)[:l2]), int(str(stone)[l2:])
            new_stones[left] = count + (new_stones[left] if left in new_stones else 0)
            new_stones[right] = count + (new_stones[right] if right in new_stones else 0)
        else:
            s = stone * 2024
            new_stones[s] = count + (new_stones[s] if s in new_stones else 0)
    return new_stones


def part_one(data: str) -> int:
    stones = {int(c): 1 for c in data.split()}
    for _ in range(25):
        stones = simulate_step(stones)
    return sum(count for count in stones.values())


def part_two(data: str) -> int:
    stones = {int(c): 1 for c in data.split()}
    for i in range(75):
        stones = simulate_step(stones)
    return sum(count for count in stones.values())


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 11)
    print(part_one(input_data))
    print(part_two(input_data))
