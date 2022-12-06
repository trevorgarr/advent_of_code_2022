"""
Advent of Code Day 6
Trevor Garrood
"""

def parse_input(input):
    return input[0]

def part_one(parsed_input):
    size = 4
    for i in range(size, len(parsed_input)):
        sub_str = parsed_input[i-size:i]
        if len(set(sub_str)) == len(sub_str):
            return i

def part_two(parsed_input):
    size = 14
    for i in range(size, len(parsed_input)):
        sub_str = parsed_input[i-size:i]
        if len(set(sub_str)) == len(sub_str):
            return i

if __name__ == "__main__":
    f = open("day6.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("INPUT =", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
