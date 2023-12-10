from util import aoc
from collections import Counter
from functools import cmp_to_key


def parse_data(data: str) -> [(str, int)]:
    return [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]


def strength(hand: str, jokers: bool = False) -> int:
    """Returns a number for the type of hand, 0 being 5-of-a-kind"""
    counter = Counter(hand).most_common()
    if jokers:
        to_replace = counter[1][0] if counter[0][0] == 'J' and len(counter) > 1 else counter[0][0]
        new_hand = hand.replace('J', to_replace)
        c = [x for _, x in Counter(new_hand).most_common()]
    else:
        c = [x for _, x in counter]
    if c[0] > 3:
        return 5 - c[0]
    if c[0] == 3 and c[1] == 2:
        return 2
    if c[0] == 3:
        return 3
    if c[0] == c[1] == 2:
        return 4
    if c[0] == 2:
        return 5
    return 6


ORDER = ['A', 'K', 'Q', 'J', 'T'] + [str(x) for x in range(9, 1, -1)]
ORDER2 = ['A', 'K', 'Q', 'T'] + [str(x) for x in range(9, 1, -1)] + ['J']


def compare(h1: str, h2: str, jokers: bool):
    sh1, sh2 = strength(h1, jokers), strength(h2, jokers)
    if sh1 > sh2:
        return -1
    if sh1 < sh2:
        return 1
    for i in range(len(h1)):
        order = ORDER2 if jokers else ORDER
        o1, o2 = order.index(h1[i]), order.index(h2[i])
        if o1 < o2:
            return 1
        if o1 > o2:
            return -1
    return 0


def compare1(hand1: (str, int), hand2: (str, int)) -> int:
    return compare(hand1[0], hand2[0], False)


def compare2(hand1: (str, int), hand2: (str, int)) -> int:
    return compare(hand1[0], hand2[0], True)


def part_one(data: str) -> int:
    hands = parse_data(data)
    hands = sorted(hands, key=cmp_to_key(compare1))
    return sum((i+1) * h[1] for i, h in enumerate(hands))


def part_two(data: str) -> int:
    hands = parse_data(data)
    print(hands)
    hands = sorted(hands, key=cmp_to_key(compare2))
    print(hands[::-1])
    return sum((i+1) * h[1] for i, h in enumerate(hands))


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 7)
    print(part_one(input_data))
    print(part_two(input_data))
