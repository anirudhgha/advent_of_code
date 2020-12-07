import re

with open("day6_input.txt") as file:
    lines = re.split('\n\n', file.read())
numpeeps = []
for row, line in enumerate(lines):
    numpeeps.append(line.count('\n') + 1)
    line = line.replace('\n', '')
    lines[row] = line

# part 1
num_anyone = 0
for group in lines:
    num_anyone += len(set(group))
print(num_anyone)


# part 2
num_everyone = 0
for row, group in enumerate(lines):
    for char in set(group):
        if group.count(char) == numpeeps[row]:
            num_everyone += 1
print(num_everyone)
