from utils import *
import re, math

input = read_input(3)

dim = Vec2(max(map(lambda x: len(x), input.split('\n'))), len(input.split('\n')))

numbers = []    # number, surrounding positions
symbols = {}    # pos, symbol

for y, line in enumerate(input.split('\n')):
    x = 0
    for v in re.findall('\d+|.', line):
        if v.isdigit():
            n = int(v)
            positions = [Vec2(x + i, y) for i, _ in enumerate(v)]
            ne = [neighbors(p, dim) for p in positions]
            surrounding_positions = set([a for b in ne for a in b]) ^ set(positions)

            numbers.append((n, surrounding_positions))
            x += len(v)
        elif v != '.':
            symbols[Vec2(x,y)] = v
            x += 1
        else:
            x += 1
    

task1 = 0
for number in numbers:
    if symbols.keys() & number[1]:
        task1 += number[0]

print(task1)

task2 = 0
for symbol in symbols:
    if symbols[symbol] == '*':
        # Gear must be connected to EXACTLY two numbers
        connected = list(filter(lambda x: symbol in x[1], numbers))
        
        if len(connected) == 2:
            first = connected[0][0]
            second = connected[1][0]

            task2 += first * second

print(task2)
