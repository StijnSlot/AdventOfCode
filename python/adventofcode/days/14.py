from adventofcode.util import aoc


def read_rules(data: str) -> (str, dict[str, str]):
    word, rules_str = data.split('\n\n')
    rules = {}
    for line in rules_str.splitlines():
        a, b = line.split(' -> ')
        rules[a] = b
    return word, rules


def simulate(word: str, rules: dict[str, str], steps: int) -> int:
    rules_map = {r: word.count(r) for r in rules}
    for _ in range(steps):
        new_rules_map = {r: 0 for r in rules}
        for r in rules_map:
            new_rules_map[r[0] + rules[r]] += rules_map[r]
            new_rules_map[rules[r] + r[1]] += rules_map[r]
        rules_map = new_rules_map
    chars = {r[0] for r in rules_map}
    char_map = {c: sum(rules_map[r] for r in rules_map if r[0] == c) for c in chars}
    char_map[word[-1]] += 1    # account for last char in word
    return max(char_map.values()) - min(char_map.values())


def part_one(data: str) -> int:
    word, rules = read_rules(data)
    return simulate(word, rules, 10)


def part_two(data: str) -> int:
    word, rules = read_rules(data)
    return simulate(word, rules, 40)


if __name__ == "__main__":
    input_data = aoc.get_input(14)
    print(part_one(input_data))
    print(part_two(input_data))
