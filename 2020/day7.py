import re

class bag:
    def __init__(self, name, i_contain, bags):
        self.name = name        
        self.num_contains = []
        self.contains_gold = True
        contains = re.split(', ', i_contain)
        self.num_contains = []
        self.contains = []
        self.contains_me = []
        for unit in contains:
            self.num_contains.append(re.split(' ', unit)[0])
            self.contains.append(re.split(' ', unit)[1] + ' ' + re.split(' ', unit)[2])

    def find_contains_me(self, bags):
         for bag in bags:    # put yourself as containing those bags. 
            if self.name in bag.contains:
                self.contains_me.append(bag.name)   


def find_containers(bags, cur, path):
    if not bags[cur].contains_me:
        return path + ', ' + cur
    for i in bags[cur].contains_me:
        path = find_containers(bags, i, path+', '+cur)
    return path

def find_containees(bags, cur):
    if 'other bags' in bags[cur].contains:
        return 0
    sum = 0
    for num, i in enumerate(bags[cur].contains):
        sum += int(bags[cur].num_contains[num]) * find_containees(bags, i) + int(bags[cur].num_contains[num])
    return sum


with open('day7_input.txt') as file:
    lines = file.read().splitlines()
bags = []
for line in lines:
    name = re.split(r' bags contain |\.', line)[0]
    i_contain = re.split(r' bags contain |\.', line)[1]
    bags.append(bag(name, i_contain, bags))

#part 1
for bag in bags:
    bag.find_contains_me(bags)
names = []
for bag in bags:
    names.append(bag.name)
bags = dict(zip(names, bags))

path = find_containers(bags, 'shiny gold', '')
path = re.split(', ', path)
print(len(set(path)) - 2)   # part 1
count = find_containees(bags, 'shiny gold')
print(count)    # part 2

