from util import aoc
from itertools import count
from dataclasses import dataclass, field


_part_one_limit = 100000
_total_disk_space = 70000000
_needed_space = 30000000


@dataclass()
class Node:
    id: int = field(default_factory=count().__next__, init=False)
    name: str
    parent: int
    file_size: int = 0
    children: list[int] = field(default_factory=list, init=False)
    _total_size: int = -1

    def cd(self, x: str, dirs: dict) -> int:
        if x == '..':
            if self.parent == -1:
                raise ValueError("cd called from root")
            return self.parent
        for child_id in self.children:
            if dirs[child_id].name == x:
                return child_id
        raise ValueError("cd directory not found in current directory")

    def total_size(self, dirs: dict) -> int:
        if self._total_size != -1:
            return self._total_size
        self._total_size = self.file_size + sum(dirs[x].total_size(dirs) for x in self.children)
        return self._total_size


def parse_data(data: str) -> tuple[int, dict[int, Node]]:
    cur_dir = Node('/', -1)
    root_id = cur_dir.id
    dirs = {root_id: cur_dir}
    for line in data.splitlines():
        if line.startswith("$ cd"):
            _, _, cd = line.split()
            if cd == '/':
                cur_dir = dirs[root_id]
                continue
            next_dir_id = cur_dir.cd(cd, dirs)
            cur_dir = dirs[next_dir_id]
        elif line.startswith("dir"):
            _, x = line.split()
            if x not in {dirs[y].name for y in cur_dir.children}:   # check for duplicate ls calls, not really needed
                new_dir = Node(x, cur_dir.id)
                dirs[new_dir.id] = new_dir
                cur_dir.children.append(new_dir.id)
        elif not line.startswith("$ ls"):
            # must be a line with file size, e.g. 123 a.bat
            x, _ = line.split()
            cur_dir.file_size += int(x)
    return root_id, dirs


def part_one(data: str) -> int:
    _, dirs = parse_data(data)
    return sum(x.total_size(dirs) for x in dirs.values() if x.total_size(dirs) < _part_one_limit)


def part_two(data: str) -> int:
    root_id, dirs = parse_data(data)
    extra_space_needed = _needed_space + dirs[root_id].total_size(dirs) - _total_disk_space
    return min(x.total_size(dirs) for x in dirs.values() if extra_space_needed <= x.total_size(dirs))


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 7)
    print(part_one(input_data))
    print(part_two(input_data))
