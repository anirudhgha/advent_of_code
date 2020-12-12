import numpy as np

# part 1
def next_stat(chunk, i, j):
    if chunk[i, j] == 'L':
        if (chunk == '#').sum() == 0:
            return '#'
        else:
             return 'L'
    elif chunk[i, j] == '#':
        if (chunk == '#').sum() >=5:
            return 'L'
        else:
            return '#'
    else:
        return chunk[i][j]

# part 2
def next_state(layout, i, j, rows, cols):
    if layout[i,j] == '.':
        return '.'
    # cardinals
    right = ''.join(list(layout[i, j+1:cols+1])).replace('.','')      
    left = ''.join(list(layout[i, 0:j])).replace('.','')[::-1]     
    up = ''.join(list(layout[0:i, j])).replace('.','')[::-1]   
    down = ''.join(list(layout[i+1:rows+1, j])).replace('.','')      
    # diagonals
    all_diag = ''
    a,b = i,j
    while a >= 0 and b < cols:
        a -= 1
        b += 1
        if a >= 0 and b < cols:
            if layout[a,b] != '.':
                all_diag += layout[a,b]
                break
    a,b = i,j
    while a >= 0 and b >= 0:
        a -= 1
        b -= 1
        if a >= 0 and b >= 0:
            if layout[a,b] != '.':
                all_diag += layout[a,b]
                break
    a,b = i,j
    while a < rows and b >= 0:
        a += 1
        b -= 1
        if a < rows and b >= 0:
            if layout[a,b] != '.':
                all_diag += layout[a,b]
                break
    a,b = i,j
    while a < rows and b < cols:
        a += 1
        b += 1
        if a < rows and b < cols:
           if layout[a,b] != '.':
                all_diag += layout[a,b]
                break
        
    all_cardinals = ''
    if left:
        all_cardinals += left[0]
    if right:
        all_cardinals += right[0]
    if up:
        all_cardinals += up[0]
    if down:
        all_cardinals += down[0]
    
    all_cardinals += all_diag

    if layout[i, j] == 'L':
        if all_cardinals.count('#') == 0:
            return '#'
        else:
            return 'L'
    
    elif layout[i,j] == '#':
        if all_cardinals.count('#') >= 5:
            return 'L'
        else:
            return '#'
   

with open('day11_input.txt', 'r') as file:
    lines = file.read().splitlines()

cols = len(lines[0])
rows = len(lines)
print(cols, rows)
layout = [['.' for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        layout[i][j] = lines[i][j]

layout = np.array(layout)

still_changing = True
while still_changing:
    hold = np.copy(layout)
    for i in range(rows):
        for j in range(cols):
            if j > 0:
                left = j-1
            else:
                left = 0
            if j < cols-1:
                right = j+1
            else:
                right = cols-1
            if i > 0:
                top = i-1
            else:
                top = 0
            if i < rows-1:
                bot = i + 1
            else:
                bot = rows-1
            hold[i,j] = next_state(layout, i, j, rows, cols)

    if np.array_equal(layout, hold):
        still_changing = False
    else:
        layout= np.copy(hold)
print((hold == '#').sum())