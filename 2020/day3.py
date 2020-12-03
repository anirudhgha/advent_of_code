
def hittintrees(trees, maxcol, maxrow, drow, dcol):
    treeshit, row, col = 0, 0, 0
    while row < maxrow:
        row += drow
        col = (col+dcol) % maxcol
        if (row, col) in trees:
            treeshit += 1
    return treeshit


with open('day3_input.txt', 'r') as file:
    lines = file.read().splitlines()

trees = []
for row, line in enumerate(lines):
    # find trees in line
    for col in [i for i, ch in enumerate(line) if ch == '#']:
        # add tree coordinates to list
        trees.append((row, col))
    maxrow = row
    maxcol = len(line)

prod = 1
treeshit = hittintrees(trees, maxcol, maxrow, 1, 3)
print(treeshit)                                             # part 1
prod *= treeshit

treeshit = hittintrees(trees, maxcol, maxrow, 1, 1)
prod *= treeshit

treeshit = hittintrees(trees, maxcol, maxrow, 1, 5)
prod *= treeshit

treeshit = hittintrees(trees, maxcol, maxrow, 1, 7)
prod *= treeshit

treeshit = hittintrees(trees, maxcol, maxrow, 2, 1)
prod *= treeshit
print(prod)                                             # part 2
