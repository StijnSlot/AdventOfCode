from util import aoc


def read_input(data: str) -> (list[int], list[list[list[int]]]):
    parts = data.split('\n\n')
    nums = [int(x) for x in parts[0].split(',')]
    boards = [[[int(x) for x in row.split()] for row in b.splitlines()] for b in parts[1:]]
    return nums, boards


def solved(nums: list[int], board: list[list[int]]) -> bool:
    return any(all(x in nums for x in row) for row in board) \
           or any(all(board[j][i] in nums for j in range(len(board))) for i in range(len(board[0])))


def search(nums: list[int], boards: list[list[list[int]]], eval_func: callable):
    """Performs binary search to find first index where eval_func is true for nums up to index"""""
    x, y = 0, len(nums)
    while x + 1 < y:
        h = (x + y) // 2
        if eval_func(solved(nums[:h + 1], board) for board in boards):
            y = h
        else:
            x = h
    return y


def score(nums: list, board: list) -> int:
    return sum(x for row in board for x in row if x not in nums)


def part_one(data: str) -> int:
    nums, boards = read_input(data)
    i = search(nums, boards, any)
    return nums[i] * score(nums[:i + 1], next(board for board in boards if solved(nums[:i+1], board)))


def part_two(data: str) -> int:
    nums, boards = read_input(data)
    i = search(nums, boards, all)
    return nums[i] * score(nums[:i + 1], next(board for board in boards if not solved(nums[:i], board)))


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 4)
    print(part_one(input_data))
    print(part_two(input_data))
