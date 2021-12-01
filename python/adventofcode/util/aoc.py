import requests
import os
from adventofcode.config import ROOT_DIR

"""Code used from https://github.com/alvesvaren/AoC-2020/blob"""

_SESSION_FILE_NAME = "session.txt"
year = 2021


def _set_read_file(filename: str, default: str = None):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        if default:
            with open(filename, "w") as file:
                file.write(default)
                return default
        return None


def _get_session():
    session = _set_read_file(os.path.join(ROOT_DIR, _SESSION_FILE_NAME))
    if not session:
        session = _set_read_file(
            _SESSION_FILE_NAME,
            input("Enter your session cookie: ")
        )
    return session.strip()


def get_input(day: int, overwrite: bool = False):
    """
    Usage:
    ```python
    import aoc
    data_rows = aoc.get_input(5).splitlines()
    ```python
    """
    data_dir = os.path.join(ROOT_DIR, "data")
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    file_name = os.path.join(data_dir, f"{day}.txt")
    data = _set_read_file(file_name)
    if overwrite:
        data = None
    if not data:
        response = requests.get(
                f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": _get_session()})
        if not response.ok:
            if response.status_code == 404:
                raise FileNotFoundError(response.text)
            raise RuntimeError(f"Request failed, code: {response.status_code}, message: {response.content}")
        data = _set_read_file(file_name, response.text[:-1])
    return data