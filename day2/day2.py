"""
Advent of Code Day 2:
Submarine Depths with aim and horizontal position
Trevor Garrood
"""

point_map = {'lost': 0,'draw':3,"won":6,"X":1,"Y":2,"Z":3}
result_map = {"AX":"draw","AY":"won","AZ":"lost","BX":"lost","BY":"draw","BZ":"won","CX":"won","CY":"lost","CZ":"draw"}

part_two_result_map = {"X":0,"Y":3,"Z":6}
part_two_point_map = {"AX":3,"AY":1,"AZ":2,"BX":1,"BY":2,"BZ":3,"CX":2,"CY":3,"CZ":1}

def parse_input(input):
    return [i.replace(" ", "") for i in input]


def part_one(parsed_input):
    total_score = 0
    for line in parsed_input:
        result = result_map.get(line)
        total_score += point_map.get(result) + point_map.get(line[1])
    return total_score

def part_two(parsed_input):
    total_score = 0
    for line in parsed_input:
        total_score += part_two_point_map.get(line) + part_two_result_map.get(line[1])
    return total_score


if __name__ == "__main__":
    f = open("day2.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
