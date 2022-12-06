"""
Advent of Code Day 5
Vents
Trevor Garrood
"""
import re


containers = {1: ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
              2: ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
              3: ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
              4: ['R', 'S', 'C', 'L'],
              5: ['M', 'V', 'T', 'P', 'F', 'B'],
              6: ['T', 'R', 'Q', 'N', 'C'],
              7: ['G', 'V', 'R'],
              8: ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
              9: ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']}

containers_p2 = {1: ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
                2: ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
                3: ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
                4: ['R', 'S', 'C', 'L'],
                5: ['M', 'V', 'T', 'P', 'F', 'B'],
                6: ['T', 'R', 'Q', 'N', 'C'],
                7: ['G', 'V', 'R'],
                8: ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
                9: ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']}

def parse_input(input):
    output = []
    for line in input:
        line = re.sub('\D', '', line)
        if len(line) == 3:
            output.append([int(line[0]),int(line[1]),int(line[2])])
        else:
            output.append([int(line[0:2]),int(line[2]),int(line[3])])
    return output

def part_one(lines):
    for move in lines:
        for i in range(0, move[0]):
            moved = containers[move[1]].pop()
            containers[move[2]].append(moved)
    top_of_stack = []
    for key in containers:
        top_of_stack.append(containers[key][-1])
    return top_of_stack

def part_two(lines):
    for move in lines:
        moved = containers_p2[move[1]][-move[0]:]
        containers_p2[move[1]] = containers_p2[move[1]][:len(containers_p2[move[1]])-move[0]]
        containers_p2[move[2]].extend(moved)
    top_of_stack = []
    for key in containers_p2:
        top_of_stack.append(containers_p2[key][-1])
    return top_of_stack

if __name__ == "__main__":
    f = open("day5.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print(parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
