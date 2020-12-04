import re


class person:
    def __init__(self, passport):
        def isInt(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        def validchar(s):
            valid = '0 1 2 3 4 5 6 7 8 9 a b c d e f'
            if s in valid:
                return True
            else:
                return False

        self.part1_valid = False
        self.part2_valid = False
        # part 1
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
            self.part1_valid = True
        # part 2
        fields = re.split(' |\n', passport)
        keys, values = [], []
        for field in fields:
            keys.append(re.split(':', field)[0])
            values.append(re.split(':', field)[1])

        self.dict = dict(zip(keys, values))
        if 'byr' in self.dict and 'iyr' in self.dict and 'eyr' in self.dict and 'hgt' in self.dict and 'hcl' in self.dict and 'ecl' in self.dict and 'pid' in self.dict:
            if len(self.dict['byr']) == 4 and int(self.dict['byr']) >= 1920 and int(self.dict['byr']) <= 2002:
                if len(self.dict['iyr']) == 4 and int(self.dict['iyr']) >= 2010 and int(self.dict['iyr']) <= 2020:
                    if len(self.dict['eyr']) == 4 and int(self.dict['eyr']) >= 2020 and int(self.dict['eyr']) <= 2030:
                        num, met = '', ''
                        for i in self.dict['hgt']:
                            if isInt(i):
                                num += i
                            else:
                                met += i
                        if (met == 'cm' and isInt(num) and int(num) >= 150 and int(num) <= 193) or (met == 'in' and isInt(num) and int(num) >= 59 and int(num) <= 76):

                            goodtogo = True
                            for char in self.dict['hcl'][1:]:
                                if validchar(char) == False:
                                    goodtogo = False
                            if goodtogo and len(self.dict['hcl'][1:]) == 6 and self.dict['hcl'][0] == '#':
                                if self.dict['ecl'] in 'amb blu brn gry grn hzl oth':
                                    goodtogo = True
                                    for num in self.dict['pid']:
                                        if isInt(num) == False:
                                            goodtogo = False
                                    if goodtogo and len(self.dict['pid']) == 9:
                                        self.part2_valid = True


with open('day4_input.txt', 'r') as file:
    lines = file.read()
passports = re.split('\n\n', lines)
people = []
for passport in passports:
    people.append(person(passport))

# part 1
valid_people = 0
for person in people:
    if person.part1_valid:
        valid_people += 1
print(valid_people)


# part 2
valid_people = 0
for person in people:
    if person.part2_valid:
        valid_people += 1
print(valid_people)
