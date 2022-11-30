from util import aoc
import re


def parse_room(line) -> tuple[str, ...]:
    match = re.match("([a-z-]+)(\d+)\[([a-z]+)\]", line)
    return tuple(match.groups())


def real_room(code: str, checksum: str) -> bool:
    most_common = sorted((- code.count(c), c) for c in set(code) if c != '-')
    return checksum == "".join(c for _, c in most_common[:len(checksum)])


def shift(code: str, id: int) -> str:
    return "".join([chr((ord(c) - 97 + id) % 26 + 97) if c != '-' else ' ' for c in code]).strip()


def part_one(data: str) -> int:
    rooms = [parse_room(line) for line in data.splitlines()]
    return sum(int(id) for (code, id, checksum) in rooms if real_room(code, checksum))


def part_two(data: str) -> int:
    rooms = [parse_room(line) for line in data.splitlines()]
    real_rooms = [(code, id, checksum) for (code, id, checksum) in rooms if real_room(code, checksum)]
    return next(id for (code, id, checksum) in real_rooms if shift(code, int(id)) == "northpole object storage")


if __name__ == "__main__":
    input_data = aoc.get_input(2016, 4)
    print(part_one(input_data))
    print(part_two(input_data))
