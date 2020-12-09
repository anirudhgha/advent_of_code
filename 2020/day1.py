import numpy as np


def find_addends(list, sum):
    for i in list:
        if (sum-i in list):
            return sum-i, i
    return -1, -1


nums = np.loadtxt("day1_input.txt", dtype=np.int)
print(np.prod(find_addends(nums, 2020)))    # part 1
for i in nums:
    addends = find_addends(nums, 2020-i)
    if addends[0] != -1:
        print(np.prod(addends) * i)         # part 2
        break


