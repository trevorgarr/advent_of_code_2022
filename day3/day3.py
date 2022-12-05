"""
Advent of Code Day 3:

Trevor Garrood
"""
def parse_input(input):
    return input

def part_one(lines):
    total = 0
    for line in lines:
        repeated_letter = ""
        first_part, second_part = line[:len(line)//2], line[len(line)//2:]
        letter_set = set()
        for char in first_part:
            letter_set.add(char)
        for char in second_part:
            if char in letter_set:
                repeated_letter = char
        value = ord(repeated_letter)-96 if repeated_letter.islower() else ord(repeated_letter)-64+26
        total += value
        print(repeated_letter, value)
    return total


def part_two(lines):
    total = 0
    for i in range(0, len(lines), 3):
        elf_one = lines[i]
        elf_two = lines[i+1]
        elf_three = lines[i+2]
        elf_one_set = set()
        potential_matches = set()
        repeated_letter = ""
        for char in elf_one:
            elf_one_set.add(char)
        for char in elf_two:
            if char in elf_one_set:
                potential_matches.add(char)
        for char in elf_three:
            if char in potential_matches:
                repeated_letter = char
        value = ord(repeated_letter)-96 if repeated_letter.islower() else ord(repeated_letter)-64+26
        total += value
        print(repeated_letter, value)
    return total

if __name__ == "__main__":
    f = open("day3.txt", "r")
    data = f.read()
    input = data.splitlines()
    parsed_input = parse_input(input)
    print("PART ONE =", part_one(parsed_input))
    print("PART TWO =", part_two(parsed_input))
    f.close()
