"""
Advent of Code Day 1:
Trevor Garrood
"""

def parse_input(input):
    return input


def part_one(parsed_input):
    absolute_max = 0
    temp_max = 0
    for num in parsed_input:
        if num == "":
            absolute_max = max(absolute_max, temp_max)
            temp_max = 0
        else:
            temp_max += int(num)
    absolute_max = max(absolute_max, temp_max)
    return absolute_max

def part_two(parsed_input):
    temp_sum = 0
    sum_list = []
    for num in parsed_input:
        if num == "":
            sum_list.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(num)
    sum_list.append(temp_sum)
    sorted_list = sorted(sum_list)
    return sum(sorted_list[-3:])


if __name__ == "__main__":
    f = open("day1.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
