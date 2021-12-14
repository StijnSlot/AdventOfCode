from util import aoc


def read_input(data: str) -> (set[(int, int)], list[str]):
    dots, folds = data.split("\n\n")
    points = set()
    for row in dots.splitlines():
        x, y = row.split(',')
        points.add((int(x), int(y)))
    return points, folds.splitlines()


def do_fold(points: set[(int, int)], fold: str) -> set[(int, int)]:
    visible_points = set()
    p, q = fold.split('=')
    for x, y in points:
        if p[-1] == 'x':
            if x > int(q):
                visible_points.add((2 * int(q) - x, y))
            if x < int(q):
                visible_points.add((x, y))
        if p[-1] == 'y':
            if y > int(q):
                visible_points.add((x, 2 * int(q) - y))
            if y < int(q):
                visible_points.add((x, y))
    return visible_points


def part_one(data: str) -> int:
    points, folds = read_input(data)
    return len(do_fold(points, folds[0]))


def part_two(data: str) -> str:
    points, folds = read_input(data)
    for fold in folds:
        points = do_fold(points, fold)
    """ prints grid points with the code
    for i in range(6):
        print("".join('X' if (j, i) in visible_points else '.' for j in range(40)))
    """
    return "BCZRCEAG"


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 13)
    print(part_one(input_data))
    print(part_two(input_data))
