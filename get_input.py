#!/usr/bin/env python3

import os
import requests
import shutil
from datetime import datetime
from sys import argv


BASE_DIR = os.path.dirname(__file__)
URL = "https://adventofcode.com/{year}/day/{day}/input"
HEADERS = {
    "User-Agent": "https://github.com/trevorgarr/advent_of_code_2022/blob/master/get_input.py by garrood.trevor@gmail.com"
}
TEMPLATE_SOLUTION_FILE = "template_solution.py"
TEMPLATE_SOLUTION_PATH = os.path.join(BASE_DIR, TEMPLATE_SOLUTION_FILE)
TEMPLATE_TEST_FILE = "template_test.py"
TEMPLATE_TEST_PATH = os.path.join(BASE_DIR, TEMPLATE_TEST_FILE)


def print_usage():
    print("Usage:", argv[0], "[[YEAR] DAY]")
    exit(1)


def arg_to_int(i, name):
    try:
        return int(argv[i])
    except ValueError:
        print("Error:", name, "is not a number")
        print_usage()



if __name__ == "__main__":
    if len(argv) == 1:
        now = datetime.now()
        if now.month != 12 or now.day > 25:
            print("Failed to deduce day: There is no new AoC puzzle today.")
            print_usage()
        year = now.year
        day = now.day
    elif "-h" in argv[1:] or "--help" in argv[1:]:
        print_usage()
    elif len(argv) == 2:
        day = arg_to_int(1, "DAY")
        now = datetime.now()
        year = now.year
        if now.month < 12:
            year -= 1
    elif len(argv) == 3:
        year = arg_to_int(1, "YEAR")
        day = arg_to_int(2, "DAY")
    else:
        print_usage()


    dir_name = os.path.join(BASE_DIR, f"day{day:1}")
    cookies = {}

    try:
        with open(os.path.join(BASE_DIR, "cookie")) as f:
            cookies["session"] = f.read().strip()
    except FileNotFoundError:
        print("No cookie file found.")
        print("Please paste the value of the 'session' cookie on the AoC website into a file named 'cookie'.")
        exit(2)

    os.makedirs(dir_name, exist_ok=True)
    input_file = os.path.join(dir_name, "day" + str(day) + ".txt")
    solution_file = os.path.join(dir_name, "day" + str(day) + ".py")
    test_file = os.path.join(dir_name, "day" + str(day) + "_test.py")

    url = URL.format(year=year, day=day)
    req = requests.get(url, cookies=cookies, headers=HEADERS)

    if os.path.exists(solution_file) or os.path.exists(test_file):
        print("ERROR:", solution_file, "or", test_file, "exists already")
    else:
        shutil.copy(TEMPLATE_SOLUTION_PATH, solution_file)
        shutil.copy(TEMPLATE_TEST_PATH, test_file)
        print("Created", solution_file, "and", test_file)

    if req.status_code != 200:
        print("Error. Got status:", req.status_code)
        print(req.text)
        exit(3)
    else:
        with open(input_file, "w") as f:
            f.write(req.text)
        print("Input for", dir_name, "written to", input_file)

