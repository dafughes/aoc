from utils import *

rows = []
cols = []

for p in (arr.split('\n') for arr in read_input(13).split('\n\n')):
    w = len(p[0])
    h = len(p)

    r = [0] * h
    c = [0] * w

    for y, line in enumerate(p):
        for x, ch in enumerate(line):
            if ch == '#':
                r[y] |= 2 ** x
                c[x] |= 2 ** y

    rows.append(r)
    cols.append(c)

def get_reflection(p):
    for i in range(1, len(p)):
        if all(a == b for a, b in zip(p[:i][::-1], p[i:])):
            return i

    return 0 

task1 = 0
for r, c in zip(rows, cols):
    task1 += 100 * get_reflection(r) + get_reflection(c)       
    
print(task1)

def get_smudge(p):
    for i in range(1, len(p)):
        if sum((a ^ b).bit_count() for a, b in zip(p[:i][::-1], p[i:])) == 1:
            return i
            
    return 0

task2 = 0
for r, c in zip(rows, cols):
    task2 += 100 * get_smudge(r) + get_smudge(c)

print(task2)
