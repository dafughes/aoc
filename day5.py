from utils import *
import re


class Mapping:
    def __init__(self):
        self.ranges = []

    def add(self, src, len, offset):
        self.ranges.append((src, len, offset))

    def get(self, val):
        for r in self.ranges:
            if r[0] <= val < (r[0] + r[1]):
                return val + r[2]
        return val
    
    def reverse(self, val):
        for r in self.ranges:
            if r[0] <= (val - r[2]) < (r[0] + r[1]):
                return val - r[2]
        return val


input = read_input(5)

mappings = []

# Parse input
seeds = list(map(int, re.findall('\d+', input.split('\n\n')[0])))
        
for m in input.split('\n\n')[1:]:
    mapping = Mapping()
    for line in m.split('\n'):
        values = list(map(int, re.findall('\d+', line)))
        if values:
            mapping.add(values[1], values[2], values[0] - values[1])
    
    mappings.append(mapping)


def forward(seed, mappings):
    for m in mappings:
        seed = m.get(seed)
    return seed

def backward(loc, mappings):
    for m in reversed(mappings):
        loc = m.reverse(loc)
    return loc




# Task 1
task1 = min([forward(seed, mappings) for seed in seeds])
print(task1)



# Task 2
# Numbers are nonnegative integers so work backwards from location 0 upwards until valid seed is found
seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

def contains_seed(seed, seeds):
    return any((x[0] <= seed < (x[0] + x[1]) for x in seeds))


# Slow af
location = 0
while True:
    if contains_seed(backward(location, mappings), seeds):
        break
    location += 1


print(location)



