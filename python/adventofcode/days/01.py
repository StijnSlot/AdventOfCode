from adventofcode.util import aoc


def sliding_window(data : list, start : int, window_length : int):
    return sum(data[i] for i in range(start, start + window_length))


def part_one(data):
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i in range(len(data.splitlines()) - 1) if data_rows[i] < data_rows[i+1])


def part_two(data):
    data_rows = [int(x) for x in data.splitlines()]
    return sum(1 for i in range(len(data_rows) - 3)
               if sliding_window(data_rows, i, 3) < sliding_window(data_rows, i + 1, 3))


if __name__ == "__main__":
    input_data = aoc.get_input(1)
    print(part_one(input_data))
    print(part_two(input_data))
