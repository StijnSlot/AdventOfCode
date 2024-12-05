from util import aoc


def read_data(data: str) -> ([(int, int)], [[int]]):
    part1, part2 = data.split('\n\n')
    rules = [tuple(int(x) for x in line.split('|')) for line in part1.splitlines()]
    updates = [[int(x) for x in line.split(',')] for line in part2.splitlines()]
    return rules, updates


def valid_update(rules: [(int, int)], update: [int]) -> bool:
    not_allowed = set()
    for u in update:
        if u in not_allowed:
            return False
        for x, y in rules:
            if y == u:
                not_allowed.add(x)
    return True


def reorder_update(rules: [(int, int)], update: [int]) -> [int]:
    new_update = []
    not_allowed = {}
    for u in update:
        if u in not_allowed:
            i = min(new_update.index(x) for x in not_allowed[u])
            new_update = new_update[:i] + [u] + new_update[i:]
        else:
            new_update.append(u)
        for x, y in rules:
            if y == u:
                if x not in not_allowed:
                    not_allowed[x] = [y]
                else:
                    not_allowed[x].append(y)
    return new_update


def part_one(data: str) -> int:
    rules, updates = read_data(data)
    return sum(update[len(update) // 2] for update in updates if valid_update(rules, update))


def part_two(data: str) -> int:
    rules, updates = read_data(data)
    updates = [reorder_update(rules, update) for update in updates if not valid_update(rules, update)]
    return sum(update[len(update) // 2] for update in updates)


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 5)
    print(part_one(input_data))
    print(part_two(input_data))
