from adventofcode.util import aoc


def read_input(data: str):
    parts = data.split('\n\n')
    nums = [int(x) for x in parts[0].split(',')]
    boards = [[[int(x) for x in row.split()] for row in b.splitlines()] for b in parts[1:]]
    return nums, boards


def solved(nums: list, board: list):
    for row in board:
        if all(x in nums for x in row):
            return True
    for i in range(len(board[0])):
        if all(board[j][i] in nums for j in range(len(board))):
            return True
    return False


def score(nums: list, board: list):
    return sum(sum(x for x in row if x not in nums) for row in board)


def part_one(data: str):
    nums, boards = read_input(data)
    x, y = 0, len(nums)
    while x + 1 < y:
        h = (x + y) // 2
        if any(solved(nums[:h + 1], board) for board in boards):
            y = h
        else:
            x = h
    return nums[y] * score(nums[:y + 1], next(board for board in boards if solved(nums[:y+1], board)))


def part_two(data: str):
    nums, boards = read_input(data)
    x, y = 0, len(nums)
    while x + 1 < y:
        h = (x + y) // 2
        if all(solved(nums[:h + 1], board) for board in boards):
            y = h
        else:
            x = h
    return nums[y] * score(nums[:y + 1], next(board for board in boards if not solved(nums[:y], board)))


if __name__ == "__main__":
    input_data = aoc.get_input(4)
    print(part_one(input_data))
    print(part_two(input_data))
