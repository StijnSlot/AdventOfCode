from importlib import import_module
from adventofcode.util import aoc
import time


def run_day(data: str, module_name: str, method: str):
    start_time = time.time()
    result = getattr(import_module(module_name), method)(data)
    if result is None:
        print(f"{method}: \033[91mfailed\033[0m")
    else:
        print(f"{method}: \033[92m{result} \033[94m({(time.time() - start_time) * 1000:.1f}ms)\033[0m")


def main():
    for i in range(1, 12):
        if i > 1:
            print('-------')
        print(f"Day {i}:")
        module_name = f"adventofcode.days.{str(i).zfill(2)}"
        data = aoc.get_input(i)
        run_day(data, module_name, 'part_one')
        run_day(data, module_name, 'part_two')


if __name__ == "__main__":
    main()
