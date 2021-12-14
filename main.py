from importlib import import_module
from util import aoc
from config import YEAR
import time


def run_day(data: str, module_name: str, method: str):
    start_time = time.time()
    result = getattr(import_module(module_name), method)(data)
    if result is None:
        print(f"{method}: \033[91mfailed\033[0m")
    else:
        print(f"{method}: \033[92m{result} \033[94m({(time.time() - start_time) * 1000:.1f}ms)\033[0m")


def main():
    for i in range(1, 26):
        if i > 1:
            print('-------')
        module_name = f"{YEAR}.days.{str(i).zfill(2)}"
        try:
            data = aoc.get_input(YEAR, i)
        except (FileNotFoundError, RuntimeError) as e:
            print(f"Stopping challenges for year {YEAR}, day {i} due to exception:\n{e}")
            break
        print(f"Advent of code {YEAR}, Day {i}:")
        run_day(data, module_name, 'part_one')
        run_day(data, module_name, 'part_two')


if __name__ == "__main__":
    main()
