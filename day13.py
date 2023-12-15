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

def solution(p, task=1):
    for i in range(1, len(p)):
        reflection = zip(p[:i][::-1], p[i:])
        if task == 1 and all(a == b for a, b in reflection):
            return i
        elif task == 2 and sum((a ^ b).bit_count() for a, b in zip(p[:i][::-1], p[i:])) == 1:
            return i

    return 0 

task1 = 0
for r, c in zip(rows, cols):
    task1 += 100 * solution(r) + solution(c)       
    
print(task1)

task2 = 0
for r, c in zip(rows, cols):
    task2 += 100 * solution(r, 2) + solution(c, 2)

print(task2)
