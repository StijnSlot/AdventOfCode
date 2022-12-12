from util import aoc


_part_one = [20, 60, 100, 140, 180, 220]
_screen_width = 40


def new_screen_pixel(x: int, cycle: int) -> str:
    if x - 1 <= cycle % _screen_width <= x + 1:
        return '#'
    else:
        return ' '


def simulate(data: str) -> tuple[int, list[str]]:
    x, cycle, total = 1, 0, 0
    screen = []
    for line in data.splitlines():
        wait_2 = False
        screen.append(new_screen_pixel(x, cycle))
        if line == "noop":
            cycle += 1
        else:
            _, k = line.split()
            k = int(k)
            cycle += 1
            wait_2 = True
        if cycle in _part_one:
            total += cycle * x
        if wait_2:
            screen.append(new_screen_pixel(x, cycle))
            cycle += 1
            x += k
            if cycle in _part_one:
                total += cycle * x
    return total, screen


def part_one(data: str) -> int:
    return simulate(data)[0]


def part_two(data: str) -> str:
    _, screen = simulate(data)
    print_screen = ""
    for i in range(6):
        print_screen += "".join(screen[i * _screen_width: (i+1) * _screen_width]) + "\n"
    return print_screen


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 10)
    print(part_one(input_data))
    print(part_two(input_data))
