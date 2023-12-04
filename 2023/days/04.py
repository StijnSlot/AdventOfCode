from util import aoc
import re


def parse_cards(data: str) -> [({int}, {int})]:
    cards = []
    for line in data.splitlines():
        match = re.match("Card\s+\d+:\s+([\d\s]+)\|\s+([\d\s]+)", line)
        won = {int(x) for x in match.group(1).split()}
        yours = {int(x) for x in match.group(2).split()}
        cards.append((won, yours))
    return cards


def get_points_card(won: {int}, yours: {int}) -> int:
    won_yours = len(won.intersection(yours))
    return 2 ** (won_yours - 1) if won_yours > 0 else 0


def part_one(data: str) -> int:
    cards = parse_cards(data)
    return sum(get_points_card(won, yours) for won, yours in cards)


def part_two(data: str) -> int:
    cards = parse_cards(data)
    your_cards = {i: 1 for i in range(len(cards))}
    total_cards = 0
    for i, (won, yours) in enumerate(cards):
        k = your_cards[i]
        total_cards += k
        for j in range(i, i + len(won.intersection(yours)) + 1):
            your_cards[j] += k
    return total_cards


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 4)
    print(part_one(input_data))
    print(part_two(input_data))
