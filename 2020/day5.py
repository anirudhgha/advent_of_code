import numpy as np

with open("day5_input.txt") as file:
    lines = file.read().splitlines()
    
seat_ids = []
for i, line in enumerate(lines):
    line = line.replace('B', '1')
    line = line.replace('F', '0')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    
    row = int(line[0:7],2)
    col = int(line[-3:],2)
    
    seat_ids.append(row*8 + col)

print(np.amax(seat_ids))        # part 1

for seat_id in range(len(seat_ids)):
    if seat_id not in seat_ids:
        if seat_id+1 in seat_ids and seat_id-1 in seat_ids:
            print(seat_id)      # part 2