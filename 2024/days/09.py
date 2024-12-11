from util import aoc
from dataclasses import dataclass


@dataclass
class File:
    file_id: int
    size: int

    def score(self, pos: int) -> int:
        return self.score_size(pos, self.size)

    def score_size(self, pos: int, size: int) -> int:
        return self.file_id * (sum_seq(pos + size - 1) - sum_seq(pos - 1))


@dataclass
class Hole:
    size: int
    files: [File]

    def remaining_size(self):
        return self.size - sum(f.size for f in self.files)

    def add_file(self, file: File):
        self.size -= file.size
        self.files.append(file)

    def score(self, i: int):
        score_sum = 0
        for j, f1 in enumerate(self.files):
            score_sum += f1.score(i)
            i += f1.size
        return score_sum


def sum_seq(n: int) -> int:
    return n * (n+1) // 2


def read_data(data: str) -> ([File], [Hole]):
    files = [File(i, int(x)) for i, x in enumerate(data[::2])]
    holes = [Hole(int(x), []) for x in data[1::2]]
    return files, holes


def part_one(data: str) -> int:
    files, holes = read_data(data)
    i = files.pop(0).size
    running_sum = 0
    hole, file = holes.pop(0), files.pop()
    while len(files) > 0 or file.size > 0:
        if file.size == 0:
            file = files.pop()
        if hole.size <= file.size:
            running_sum += file.score_size(i, hole.size)
            i += hole.size
            file.size -= hole.size
            hole = holes.pop(0)
            if len(files) > 0:
                skip_file = files.pop(0)
                running_sum += skip_file.score(i)
                i += skip_file.size
        else:
            running_sum += file.score(i)
            i += file.size
            hole.size -= file.size
            file.size = 0
    return running_sum + file.score(i)


def part_two(data: str) -> int:
    files, holes = read_data(data)
    for i, file in reversed(list(enumerate(files))):
        hole = next((hole for hole in holes[:i] if hole.remaining_size() >= file.size), None)
        if hole is not None:
            hole.files.append(file)
    running_sum, i = 0, 0
    handled_file_ids = set()
    for file, hole in zip(files, holes):
        if file.file_id not in handled_file_ids:
            running_sum += file.score(i)
            handled_file_ids.add(file.file_id)
        running_sum += hole.score(i + file.size)
        handled_file_ids.update(f.file_id for f in hole.files)
        i += file.size + hole.size
    return running_sum


if __name__ == "__main__":
    input_data = aoc.get_input(2024, 9)
    print(part_one(input_data))
    print(part_two(input_data))
