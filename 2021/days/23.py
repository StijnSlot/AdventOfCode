from functools import cache


def map_char_to_score(c: str):
    mapping = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return mapping[c]


def map_char_to_room(c: str, room_size: int):
    mapping = {'A': 0, 'B': room_size, 'C': 2 * room_size, 'D': 3 * room_size}
    return mapping[c]


def hallway_clear(i, j, hallway, room_size):
    if j <= 0 and hallway[1] != ".":
        return False
    if j <= 1 and i >= room_size and hallway[2] != ".":
        return False
    if j <= 2 and i >= 2 * room_size and hallway[3] != ".":
        return False
    if j <= 3 and i >= 3 * room_size and hallway[4] != ".":
        return False
    if j >= len(hallway) - 1 and hallway[-2] != ".":
        return False
    if j >= len(hallway) - 2 and i < 3 * room_size and hallway[-3] != ".":
        return False
    if j >= len(hallway) - 3 and i < 2 * room_size and hallway[-4] != ".":
        return False
    if j >= len(hallway) - 4 and i < room_size and hallway[-5] != ".":
        return False
    return True


def penalty(i, j, c, room_size):
    room = (i // room_size) * 2 + 2
    hallway = j if j < 2 else j + 4 if j > 4 else 2 * j - 1
    dis = abs(room - hallway) + i % room_size + 1
    return map_char_to_score(c) * dis


@cache
def dfs(rooms, hallway, room_size):
    # print(rooms, hallway)
    sol = 99999999999999999999
    dis = 0
    changes = True
    while changes:
        changes = False
        for i, x in enumerate(hallway):
            if x == ".":
                continue
            j = map_char_to_room(x, room_size)
            if not hallway_clear(j, i, hallway, room_size):
                continue
            if all(room != '.' for room in rooms[j:j+room_size]):
                continue
            if any(room not in [x, '.'] for room in rooms[j:j+room_size]):
                continue
            k = next(k for k in reversed(range(j, j+room_size)) if rooms[k] == '.')
            dis += penalty(k, i, x, room_size)
            rooms = rooms[:k] + x + rooms[k+1:]
            hallway = hallway[:i] + "." + hallway[i+1:]
            changes = True
    if all(r != '.' and 0 <= i - map_char_to_room(r, room_size) < room_size for i, r in enumerate(rooms)):
        return dis
    for i, x in enumerate(rooms):
        if x == ".":
            continue
        if any(rooms[i-k-1] != "." for k in range(i % room_size)):
            continue
        dest_room = map_char_to_room(x, room_size)
        if 0 <= i - dest_room < room_size and all(rooms[k] == x for k in range(i, dest_room + room_size)):
            continue
        for j, y in enumerate(hallway):
            if y != ".":
                continue
            if not hallway_clear(i, j, hallway, room_size):
                continue
            sol = min(sol, dfs(rooms[:i] + "." + rooms[i+1:], hallway[:j] + x + hallway[j + 1:], room_size) + dis + penalty(i, j, x, room_size))
    return sol


def part_one(data: str) -> int:
    grid = data.splitlines()
    room0 = grid[2][3] + grid[3][3]
    room1 = grid[2][5] + grid[3][5]
    room2 = grid[2][7] + grid[3][7]
    room3 = grid[2][9] + grid[3][9]
    return dfs(room0 + room1 + room2 + room3, ".......", 2)


def part_two(data: str) -> int:
    grid = data.splitlines()
    room0 = grid[2][3] + "DD" + grid[3][3]
    room1 = grid[2][5] + "CB" + grid[3][5]
    room2 = grid[2][7] + "BA" + grid[3][7]
    room3 = grid[2][9] + "AC" + grid[3][9]
    return dfs(room0 + room1 + room2 + room3, ".......", 4)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 23)
    # print(part_one(input_data))
    print(part_two(input_data))
