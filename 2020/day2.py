import re

with open('day2_input.txt', 'r') as file:
    lines = file.read().splitlines()

valid_part1 = 0
valid_part2 = 0
for i in lines:
    low, high, letter, _, string = re.split(' |-|:', i)
    if string.count(letter) >= int(low) and string.count(letter) <= int(high):
        valid_part1 += 1
    if string[int(low)-1] == letter and string[int(high)-1] != letter or string[int(high)-1] == letter and string[int(low)-1] != letter:
        valid_part2 += 1
print(valid_part1)
print(valid_part2)
