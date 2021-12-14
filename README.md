# AdventOfCode2021
Repository to host my solutions for Advent of Code, written in Python 3.10.

## Usage
To run this project, do the following steps:
1. Log into `https://adventofcode.com` and copy the session cookie to `session.txt`. 
2. Do either of the following:
    * Configure the year in `config.py` and then run `main.py` to generate all solutions for a given year.
    * Run a specific day by going into the `year/days` folder and picking a file (e.g. `2021/days/01.py`)

### Day template
To generate a placeholder file for all days in as given year, do the following:
1. Configure the year in `config.py`
2. (Optional) Adjust `util/template.txt` to your liking
3. Run `util/generate_days.py`
This will create a placeholder solution for any days that do not already have a file (e.g. will create `days/01.py` if not already exists).