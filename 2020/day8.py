def op_exec(op, tot, pos, arg):
    switcher = {
        'acc': acc(tot, pos, arg),
        'jmp': jmp(tot, pos, arg),
        'nop': nop(tot, pos, arg)
    }
    exe = switcher.get(op, lambda: 'invalid operation')
    return exe
def acc(tot, pos, arg):
    return tot + arg, pos+1
def jmp(tot, pos, arg):
    return tot, pos+arg
def nop(tot, pos, arg):
    return tot, pos+1
def gotoend(lines, tot, pos, visited):
    if pos >= len(lines) or pos < 0 or pos in visited:
        return tot, pos
    visited.append(pos)
    op, arg = lines[pos].split(' ')[0], int(lines[pos].split(' ')[1])
    tot, pos = op_exec(op, tot, pos, arg)
    return gotoend(lines, tot, pos, visited)


with open('day8_input.txt') as file:
    lines = file.read().splitlines()


visited = []
pos, tot = 0, 0
while pos not in visited:
    op, arg = lines[pos].split(' ')[0], int(lines[pos].split(' ')[1])
    if op=='nop':
        lines_swapped = lines[:]
        lines_swapped[pos] = 'jmp ' + lines[pos].split(' ')[1]
        copy_visited = visited[:]
        totout, posout = gotoend(lines_swapped, tot, pos, copy_visited)
        if posout == len(lines):
            print(totout)
    elif op=='jmp':
        lines_swapped = lines[:]
        lines_swapped[pos] = 'nop ' + lines[pos].split(' ')[1]
        copy_visited = visited[:]
        totout, posout = gotoend(lines_swapped, tot, pos, copy_visited)
        if posout == len(lines):
            print(totout)
    visited.append(pos)
    tot, pos = op_exec(op, tot, pos, arg)







