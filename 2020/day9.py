import numpy as np

def find_addends(list, sum):
    for i in list:
        if (sum-i in list):
            return sum-i, i
    return -1, -1

with open('day9_input.txt', 'r') as file:
    lines = file.read().splitlines()

preamble_length = 25

# part 1
for i, line in enumerate(lines):
    lines[i] = int(line)
    if i < preamble_length:
        continue
    s1, s2 = find_addends(lines[i-preamble_length:i], lines[i])
    if s1 == -1:
        num = lines[i]
        print(lines[i])
        break

# part 2
tot = 0
done = False
for i,line in enumerate(lines):
    for j in range(i, len(lines)):
        tot += int(lines[j])
        if tot == num:
            ans = np.amin(lines[i:j+1]) + np.amax(lines[i:j+1])
            print(ans)
            done = True
        if tot > num:
            break
    tot = 0
    if done:
        break