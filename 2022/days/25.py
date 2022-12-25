from util import aoc


snafu_map = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
snafu_map_rev = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
max_digits = 100


def part_one(data: str) -> str:
    result = sum(sum(5 ** i * snafu_map[c] for i, c in enumerate(line[::-1])) for line in data.splitlines())

    snafu = [0 for _ in range(max_digits + 1)]
    for i in range(max_digits, -1, -1):
        x = (result // (5 ** i)) % 5
        if x >= 3:
            snafu[i] = -5 + x
            j = i + 1
            snafu[j] += 1
            while snafu[j] >= 3:
                snafu[j] = -2
                j += 1
                snafu[j] += 1
        else:
            snafu[i] += x
    k = next(i for i in range(max_digits, -1, -1) if snafu[i] != 0)
    return "".join(snafu_map_rev[snafu[i]] for i in range(k, -1, -1))


def part_two(data: str) -> str:
    return 'Done :)'


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 25)
    print(part_one(input_data))
    print(part_two(input_data))
