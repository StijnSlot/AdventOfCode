from util import aoc
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Point:
    x: float
    y: float
    z: float = None

    def within_bounds(self, min_d: float, max_d: float) -> bool:
        return all(d is None or min_d <= d <= max_d for d in (self.x, self.y, self.z))


def det(p1: Point, p2: Point):
    return p1.x * p2.y - p1.y * p2.x


@dataclass
class Ray:
    start: Point
    vel: Point
    end: Point = field(init=False)

    def __post_init__(self):
        big_step = 1000000000000000
        self.end = Point(self.start.x + big_step * self.vel.x,
                         self.start.y + big_step * self.vel.y,
                         self.start.z + big_step * self.vel.z)

    def intersect_xy(self, ray) -> Optional[Point]:
        xdiff = Point(self.start.x - self.end.x, ray.start.x - ray.end.x)
        ydiff = Point(self.start.y - self.end.y, ray.start.y - ray.end.y)

        div = det(xdiff, ydiff)
        if div == 0:
            return None  # no intersection

        d = Point(det(self.start, self.end), det(ray.start, ray.end))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        if (x - self.start.x) * (self.end.x - self.start.x) < 0:
            # different sign, intersection behind start
            return None
        if (x - ray.start.x) * (ray.end.x - ray.start.x) < 0:
            # different sign, intersection behind start
            return None
        return Point(x, y)


def parse_data(data: str) -> [Ray]:
    rays = []
    for line in data.splitlines():
        left, right = line.split(' @ ')
        start = Point(*(int(x) for x in left.split(',')))
        vel = Point(*(int(x) for x in right.split(',')))
        rays.append(Ray(start, vel))
    return rays


def adjust_xy(ray: Ray, dx: int, dy: int) -> Ray:
    return Ray(ray.start, Point(ray.vel.x - dx, ray.vel.y - dy, ray.vel.z))


def single_intersect(rays: [Ray], dx: int, dy: int):
    adj_ray1 = adjust_xy(rays[0], dx, dy)
    intersect = None
    for ray in rays[1:]:
        adj_ray2 = adjust_xy(ray, dx, dy)
        p = adj_ray1.intersect_xy(adj_ray2)
        if p is None or (intersect is not None and intersect != p):
            return None
        intersect = p
    return intersect


def part_one(data: str) -> int:
    rays = parse_data(data)
    min_d, max_d = 200000000000000., 400000000000000.
    return sum(1
               for i, ray1 in enumerate(rays)
               for j, ray2 in enumerate(rays)
               if i < j
               and ray1.intersect_xy(ray2) is not None
               and ray1.intersect_xy(ray2).within_bounds(min_d, max_d))


def part_two(data: str) -> int:
    rays = parse_data(data)
    for dx in range(-300, 300):
        for dy in range(-300, 300):
            p = single_intersect(rays, dx, dy)
            if p is None:
                continue
            # p0 + t0 * (vz1 - dz) = p1 + t1 * (vz2 - dz)
            # t0 * dz - t1 * dz = p0 + t0 * vz1 - p1 - t1 * vz2
            # dz = (p0 + t0 * vz1 - p1 - t1 * vz2) / (t0 - t1)
            ray0, ray1 = rays[:2]
            adj_ray0 = adjust_xy(ray0, dx, dy)
            t0 = (p.x - adj_ray0.start.x) / adj_ray0.vel.x
            adj_ray1 = adjust_xy(ray1, dx, dy)
            t1 = (p.y - adj_ray1.start.y) / adj_ray1.vel.y
            dz = (ray0.start.z + t0 * ray0.vel.z - ray1.start.z - t1 * ray1.vel.z) / (t0 - t1)
            z = ray0.start.z + t0 * (ray0.vel.z - dz)
            return int(p.x + p.y + z)
    return -1


if __name__ == "__main__":
    input_data = aoc.get_input(2023, 24)
    print(part_one(input_data))
    print(part_two(input_data))
