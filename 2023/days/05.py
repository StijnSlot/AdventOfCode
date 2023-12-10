from util import aoc
from dataclasses import dataclass


@dataclass
class Converter:
    source: str
    dest: str
    ranges: [(int, int, int)]

    def convert(self, x: int) -> int:
        for r_dest, r_source, k in self.ranges:
            if r_source <= x < r_source + k:
                return r_dest + x - r_source
        return x

    def convert_range(self, x_range: (int, int)) -> [(int, int)]:
        in_ranges = [x_range]
        out_ranges = []
        for r_dest, r_source, k in self.ranges:
            new_in_ranges = []
            for cur, l in in_ranges:
                # left range
                if cur < r_source:
                    new_in_ranges.append((cur, min(l, r_source - cur)))

                # center range
                if r_source <= cur + l and cur < r_source + k:
                    start = max(r_source, cur)
                    offset = start - r_source
                    length = min(r_source + k, cur + l) - start
                    out_ranges.append((r_dest + offset, length))

                # right range
                if cur + l > r_source + k:
                    new_start = max(cur, r_source + k)
                    new_in_ranges.append((new_start, l - new_start + cur))
            in_ranges = new_in_ranges

        # leftovers
        out_ranges += in_ranges
        return out_ranges


@dataclass
class Input:
    seeds: [int]
    converters: {str, Converter}

    def convert_to(self, source: str, x: int) -> (str, int):
        converter = self.converters[source]
        y = converter.convert(x)
        return converter.dest, y

    def convert_to_ranges(self, source: str, ranges: [(int, int)]) -> (str, [(int, int)]):
        converter = self.converters[source]
        return converter.dest, [x for r in ranges for x in converter.convert_range(r)]


def parse_data(data: str) -> Input:
    parts = data.split('\n\n')
    _, seeds_str = parts[0].split(': ')
    seeds = [int(x) for x in seeds_str.split()]
    converters = {}
    for part in parts[1:]:
        lines = part.splitlines()
        map_str = lines[0]
        source, dest = map_str.split('-to-')
        dest = dest.split()[0]
        ranges = [tuple(int(x) for x in line.split()) for line in lines[1:]]
        converters[source] = Converter(source, dest, ranges)
    return Input(seeds, converters)


def convert_seed(input_data: Input, seed: int) -> int:
    cat = 'seed'
    x = seed
    while cat != 'location':
        cat, x = input_data.convert_to(cat, x)
    return x


def convert_range(input_data: Input, s_range: (int, int)) -> [(int, int)]:
    cat = 'seed'
    ranges = [s_range]
    while cat != 'location':
        cat, ranges = input_data.convert_to_ranges(cat, ranges)
    return ranges


def part_one(data: str) -> int:
    input_data = parse_data(data)
    return min(convert_seed(input_data, s) for s in input_data.seeds)


def part_two(data: str) -> int:
    input_data = parse_data(data)
    seeds = input_data.seeds
    ranges = [(x, k) for x, k in zip(seeds[::2], seeds[1::2])]
    return min(min(x for x, _ in convert_range(input_data, r)) for r in ranges)


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 5)
    print(part_one(input_data))
    print(part_two(input_data))
