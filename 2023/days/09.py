from util import aoc


def parse_seqs(nums: [int]) -> [[int]]:
    seqs = [nums]
    while not all(x == 0 for x in seqs[-1]):
        last_seq = seqs[-1]
        seq = [last_seq[i] - last_seq[i - 1] for i in range(1, len(last_seq))]
        seqs.append(seq)
    return seqs


def next_val(nums: [int]) -> int:
    return sum(seq[-1] for seq in parse_seqs(nums))


def prev_val(nums: [int]) -> int:
    return sum((1 - 2 * (i % 2)) * seq[0] for i, seq in enumerate(parse_seqs(nums)))


def part_one(data: str) -> int:
    return sum(next_val([int(x) for x in line.split()]) for line in data.splitlines())


def part_two(data: str) -> int:
    return sum(prev_val([int(x) for x in line.split()]) for line in data.splitlines())


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 9)
    print(part_one(input_data))
    print(part_two(input_data))
