from util import aoc
from functools import lru_cache


PRUNE_NUM = 16777216


@lru_cache(maxsize=None)
def simulate_step(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % PRUNE_NUM
    secret = (secret ^ (secret // 32)) % PRUNE_NUM
    return (secret ^ (secret * 2048)) % PRUNE_NUM


@lru_cache(maxsize=None)
def simulate(secret: int, steps: int) -> (int, [int]):
    digits = [secret % 10]
    for _ in range(steps):
        secret = simulate_step(secret)
        digits.append(secret % 10)
    return secret, digits


def part_one(data: str) -> int:
    return sum(simulate(int(line), 2000)[0] for line in data.splitlines())


def part_two(data: str) -> int:
    prices = []
    for line in data.splitlines():
        prices.append(simulate(int(line), 2000)[1])
    seq_prices = []
    for k, digits in enumerate(prices):
        seq_price = {}
        for i in range(4, len(digits)):
            t = tuple(digits[j] - digits[j-1] for j in range(i-3, i+1))
            if t not in seq_price:
                seq_price[t] = digits[i]
        seq_prices.append(seq_price)
    return max(sum(seq_price.get((i, j, k, l), 0) for seq_price in seq_prices)
               for i in range(-9, 10)
               for j in range(-9, 10)
               for k in range(-9, 10)
               for l in range(-9, 10))


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 22)
    print(part_one(input_data))
    print(part_two(input_data))
