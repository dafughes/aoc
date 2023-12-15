from utils import *

input = []

for p in (arr.split('\n') for arr in read_input(13).split('\n\n')):
    r = [0] * len(p)
    c = [0] * len(p[0])

    for y, line in enumerate(p):
        for x, ch in enumerate(line):
            if ch == '#':
                r[y] |= 2 ** x
                c[x] |= 2 ** y

    input.append((r, c))

def solution(p, task=1):
    for i in range(1, len(p)):
        if task == 1 and all(a == b for a, b in zip(p[:i][::-1], p[i:])):
            return i
        elif task == 2 and sum((a ^ b).bit_count() for a, b in zip(p[:i][::-1], p[i:])) == 1:
            return i

    return 0 

task1 = sum(100 * solution(r) + solution(c) for r, c in input)
task2 = sum(100 * solution(r, 2) + solution(c, 2) for r, c in input)
    
print(task1)
print(task2)
