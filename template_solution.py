"""
Advent of Code Day X
Trevor Garrood
"""

def parse_input(input):
    return input

def part_one(parsed_input):
    pass

def part_two(parsed_input):
    pass

if __name__ == "__main__":
    f = open("dayX.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("INPUT =", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
