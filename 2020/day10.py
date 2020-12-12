
def find_connected(lines, i):
    ind = []
    for j in range(i-1, i-4, -1):
        if lines[i] - lines[j] <= 3 and j >= 0:
            ind.append(j)
    return ind

with open ('day10_input.txt', 'r') as file:
    lines = file.read().splitlines()
for i, line in enumerate(lines):
    lines[i] = int(line)

lines = sorted(lines)
lines.insert(0, 0)
lines.append(lines[-1] + 3)
dif1, dif3 = 0,0
for i, line in enumerate(lines):
    if i > 0 and line - lines[i-1] == 1:
        dif1 += 1
    elif i > 0 and line - lines[i-1] == 3:
        dif3 += 1

print(dif1*dif3) # part 1

node_combos = [0 for i in range(len(lines))]
node_combos[len(lines)-1] = 1
for i in range(len(lines)-1, -1, -1):
    connected_ind = find_connected(lines, i)
    for node in connected_ind:
        node_combos[node] += node_combos[i]

print(node_combos[0]) # part 2


