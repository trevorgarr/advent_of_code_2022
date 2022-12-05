"""
Advent of Code Day 4:
Bingo
Trevor Garrood
"""

def parse_input(input):
    output = []
    for line in input:
        line = line.split(",")
        first_elf = line[0].split("-")
        second_elf = line[1].split("-")
        output.append([int(first_elf[0]), int(first_elf[1]), int(second_elf[0]), int(second_elf[1])])
    return output

def part_one(lines):
    overlapping = 0
    for line in lines:
        first_elf_low, first_elf_high = line[0], line[1]
        second_elf_low, second_elf_high = line[2], line[3]
        is_first_in_second_range = first_elf_low >= second_elf_low and first_elf_high <= second_elf_high
        is_second_in_first_range = second_elf_low >= first_elf_low and second_elf_high <= first_elf_high
        if is_first_in_second_range or is_second_in_first_range:
            overlapping += 1
    return overlapping



def part_two(lines):
    overlapping = 0
    for line in lines:
        first_elf_low, first_elf_high = line[0], line[1]
        second_elf_low, second_elf_high = line[2], line[3]
        is_first_low = first_elf_low >= second_elf_low and first_elf_low <= second_elf_high
        is_first_high = first_elf_high >= second_elf_low and first_elf_high <= second_elf_high
        is_second_low = second_elf_low >= first_elf_low and second_elf_low <= first_elf_high
        is_second_high = second_elf_high >= first_elf_low and second_elf_high <= first_elf_high

        is_f_low = first_elf_low <= second_elf_low <= first_elf_high
        is_s_low = second_elf_low <= first_elf_low <= second_elf_high

        if is_f_low or is_s_low:
            overlapping += 1
    return overlapping

if __name__ == "__main__":
    f = open("day4.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("INPUT =", parsed_input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
