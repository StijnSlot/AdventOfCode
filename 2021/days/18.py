from util import aoc


class SnailFish:
    def __init__(self, left, right, x=None):
        assert x is None or (left is None and right is None)
        self.left = left
        self.right = right
        self.parent = None
        self.x = x

    @classmethod
    def from_line(cls, line: str, i: int):
        assert line[i] == '['
        if line[i + 1] == '[':
            left, i = cls.from_line(line, i + 1)
        else:
            left, i = cls(None, None, int(line[i + 1])), i + 2
        assert line[i] == ','
        if line[i + 1] == '[':
            right, i = cls.from_line(line, i + 1)
        else:
            right, i = cls(None, None, int(line[i + 1])), i + 2
        assert line[i] == ']'
        snail = cls(left, right)
        left.parent = snail
        right.parent = snail
        return snail, i + 1

    def magnitude(self) -> int:
        if self.x is not None:
            return self.x
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def do_explode(self):
        # left addition
        child, parent = self, self.parent
        while parent is not None and parent.left is child:
            child, parent = parent, parent.parent
        if parent is not None:
            dest = parent.left
            while dest.x is None:
                dest = dest.right
            dest.x += self.left.x

        # right addition
        child, parent = self, self.parent
        while parent is not None and parent.right is child:
            child, parent = parent, parent.parent
        if parent is not None:
            dest = parent.right
            while dest.x is None:
                dest = dest.left
            dest.x += self.right.x

        self.left = None
        self.right = None
        self.x = 0

    def explode(self, depth):
        if self.x is not None:
            return False
        if self.left.explode(depth + 1):
            return True
        elif self.right.explode(depth + 1):
            return True
        if depth >= 4:
            self.do_explode()
            return True
        return False

    def split(self):
        if self.left is not None and self.left.split():
            return True
        elif self.right is not None and self.right.split():
            return True
        elif self.x is not None and self.x >= 10:
            self.left = SnailFish(None, None, self.x // 2)
            self.right = SnailFish(None, None, (self.x + 1) // 2)
            self.x = None
            self.left.parent = self
            self.right.parent = self
            return True
        return False


def add(snail1, snail2):
    if snail1 is None:
        return snail2
    snail = SnailFish(snail1, snail2)
    snail1.parent = snail
    snail2.parent = snail
    while snail.explode(0) or snail.split():
        pass
    return snail


def part_one(data: str) -> int:
    snail = None
    for line in data.splitlines():
        new_snail, _ = SnailFish.from_line(line, 0)
        snail = add(snail, new_snail)
    return snail.magnitude()


def part_two(data: str) -> int:
    return max(add(SnailFish.from_line(line1, 0)[0], SnailFish.from_line(line2, 0)[0]).magnitude()
               for line1 in data.splitlines()
               for line2 in data.splitlines()
               if line1 != line2)


if __name__ == "__main__":
    input_data = aoc.get_input(2021, 18)
    print(part_one(input_data))
    print(part_two(input_data))
