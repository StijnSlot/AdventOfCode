from util import aoc


def support_tls(x: str) -> bool:
    brackets = 0
    valid_abba = False
    for i in range(len(x) - 3):
        if x[i] == '[':
            brackets += 1
        elif x[i] == ']':
            brackets -= 1
        elif x[i] == x[i+3] and x[i+1] == x[i+2] and x[i] != x[i+1] and x[i+1] not in {'[', ']'}:
            if brackets > 0:
                return False
            valid_abba = True
    return valid_abba


def support_ssl(x: str) -> bool:
    brackets = 0
    abas = set()
    babs = set()
    for i in range(len(x) - 2):
        if x[i] == '[':
            brackets += 1
        elif x[i] == ']':
            brackets -= 1
        elif x[i] == x[i+2] and x[i] != x[i+1] and x[i+1] not in {'[', ']'}:
            three_chars, rev_three_chars = x[i:i+3], x[i+1] + x[i] + x[i+1]
            if rev_three_chars in (babs if brackets == 0 else abas):
                return True
            if brackets == 0:
                abas.add(three_chars)
            else:
                babs.add(three_chars)
    return False


def part_one(data: str) -> int:
    return sum(1 for line in data.splitlines() if support_tls(line))


def part_two(data: str) -> int:
    return sum(1 for line in data.splitlines() if support_ssl(line))


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 7)
    print(part_one(input_data))
    print(part_two(input_data))
