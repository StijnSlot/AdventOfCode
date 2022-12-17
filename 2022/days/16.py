from functools import lru_cache
from util import aoc
from dataclasses import dataclass, field
from itertools import combinations
import re


_line_re = "Valve (\w+) has flow rate=(\d+); tunnels* leads* to valves* ([\w+, ]*)"
valves = {}


@dataclass
class Valve:
    flow_rate: int
    adj: list[str]
    dis: dict[str, int] = field(init=False, default_factory=dict)
    for_person: bool = True


@lru_cache(maxsize=None)
def dfs(u: str, time: int, opened: tuple, is_person: bool = True) -> int:
    if time <= 0:
        return 0
    # print(v, time, opened)
    valve = valves[u]
    result = 0
    for v in valve.dis:
        if valves[v].for_person == is_person and v not in opened:
            result = max(result, dfs(v, time - valve.dis[v], opened, is_person))
    if u not in opened and valve.flow_rate > 0:
        add_flow = (time - 1) * valve.flow_rate
        result = max(result, add_flow)
        cur_opened = tuple(sorted(opened + (u,)))
        for v in valve.dis:
            if valves[v].for_person == is_person and v not in opened and valve.dis[v] < time - 1:
                result = max(result, add_flow + dfs(v, time - valve.dis[v] - 1, cur_opened, is_person))
    return result


def pre_compute_dis() -> None:
    for u in valves:
        valves[u].dis = {v: (1 if v in valves[u].adj else 999999) for v in valves}
        valves[u].dis[u] = 0
    change = True
    while change:
        change = False
        for u in valves:
            for v in valves:
                for z in valves:
                    new_value = valves[u].dis[z] + valves[z].dis[v]
                    if new_value < valves[u].dis[v]:
                        valves[u].dis[v] = new_value
                        change = True
    # delete zero flow nodes and itself
    for u in valves:
        valves[u].dis = {v: valves[u].dis[v] for v in valves[u].dis if valves[v].flow_rate > 0 and u != v}


def read_data(data: str) -> None:
    global valves
    valves = {}
    for line in data.splitlines():
        match = re.match(_line_re, line)
        name, rate, adj = match.groups()
        valves[name] = Valve(int(rate), adj.split(', '))


def part_one(data: str) -> int:
    read_data(data)
    pre_compute_dis()
    return dfs('AA', 30, ())


def part_two(data: str) -> int:
    read_data(data)
    pre_compute_dis()
    relevant_valves = [v for v in valves if valves[v].flow_rate > 0]
    combis = [c for i in range(1, len(relevant_valves) // 2) for c in combinations(relevant_valves, i)]
    result = 0
    for i, combi in enumerate(combis):
        for x in combi:
            valves[x].for_person = False
        a, b = dfs('AA', 26, (), True), dfs('AA', 26, (), False)
        dfs.cache_clear()
        result = max(result, a + b)
        for x in combi:
            valves[x].for_person = True
    return result


if __name__ == "__main__":
    input_data = aoc.get_input(2022, 16)
    print(part_one(input_data))
    print(part_two(input_data))
