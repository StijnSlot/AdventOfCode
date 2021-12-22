from util import aoc


def read_input(data: str) -> (str, list[str]):
    first, second = data.split("\n\n")
    algo = "".join(first.splitlines())
    image = second.splitlines()
    return algo, image


def get_index(image: list[str], i: int, j: int, infinite: str) -> int:
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    index_str = ""
    for ddx, ddy in zip(dx, dy):
        x, y = i + ddx - 1, j + ddy - 1
        if 0 <= x < len(image) and 0 <= y < len(image[x]):
            index_str += '1' if image[x][y] == '#' else '0'
        else:
            index_str += '1' if infinite == '#' else '0'
    return int(index_str, 2)


def simulate_step(algo: str, image: list[str], infinite: str) -> (list[str], str):
    new_image = []
    for i in range(len(image) + 2):
        new_image.append([])
        for j in range(len(image[0]) + 2):
            if algo[get_index(image, i, j, infinite)] == '#':
                new_image[i].append('#')
            else:
                new_image[i].append('.')
    inf = algo[2**9 - 1 if infinite == '#' else 0]
    return new_image, inf


def simulate(algo: str, image: list[str], nr_of_steps: int) -> list[str]:
    inf = '.'
    for _ in range(nr_of_steps):
        image, inf = simulate_step(algo, image, inf)
    return image


def score(image):
    return sum(1 for row in image for x in row if x == '#')


def part_one(data: str) -> int:
    algo, image = read_input(data)
    image = simulate(algo, image, 2)
    return score(image)


def part_two(data: str) -> int:
    algo, image = read_input(data)
    image = simulate(algo, image, 50)
    return score(image)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 20)
    print(part_one(input_data))
    print(part_two(input_data))
