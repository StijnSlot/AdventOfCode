import os
from config import ROOT_DIR, YEAR


def generate_day(day: int):
    file_path = os.path.join(ROOT_DIR, f"{YEAR}/days/{str(day).zfill(2)}.py")

    if os.path.exists(file_path):
        print(f"Did not generate for year {YEAR}, day {day}, file already exists")
        return

    with open(file_path, 'w') as f:
        f.write(create_template(day))


def create_template(day: int):
    template_path = os.path.join(ROOT_DIR, "util/template.txt")

    with open(template_path) as f:
        return f.read().replace("{day}", str(day)).replace("{year}", str(YEAR))


def main():
    for i in range(1, 26):
        generate_day(i)


if __name__ == '__main__':
    main()
