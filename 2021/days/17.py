from util import aoc


def read_data(data: str) -> (int, int, int, int):
    parts = data.split()
    part_x = parts[2].split('..')
    part_y = parts[3].split('..')
    return int(part_x[0][2:]), int(part_y[0][2:]), int(part_x[1][:-1]), int(part_y[1])


def height_y(dy: int, steps=None) -> int:
    k = steps if steps is not None else dy
    return k * dy - k * (k - 1) // 2


def simulate_y(dy: int, target_rect: (int, int, int, int)) -> bool:
    # binary search for y height inside target assuming parabola trajectory
    k0, k1 = dy, dy + 10000
    while k0 + 1 < k1:
        h = (k0 + k1) // 2
        y = height_y(dy, h)
        if target_rect[1] <= y <= target_rect[3]:
            return True
        if y > target_rect[3]:
            k0 = h
        else:
            k1 = h
    return False


def simulate(dx: int, dy: int, target_rect: (int, int, int, int)):
    p = (0, 0)
    while dx != 0 or (target_rect[0] <= p[0] <= target_rect[2] and p[1] >= target_rect[1]):
        if target_rect[0] <= p[0] <= target_rect[2] and target_rect[1] <= p[1] <= target_rect[3]:
            return True
        p = (p[0] + dx, p[1] + dy)
        dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else dx
        dy -= 1
    return False


def part_one(data: str) -> int:
    target_rect = read_data(data)
    return max(height_y(dy) for dy in range(target_rect[1], target_rect[1] + 500) if simulate_y(dy, target_rect))


def part_two(data: str) -> int:
    target_rect = read_data(data)
    return sum(1 for dx in range(target_rect[2] + 1)
               for dy in range(target_rect[1], target_rect[1] + 500)
               if simulate(dx, dy, target_rect))


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 17)
    print(part_one(input_data))
    print(part_two(input_data))
