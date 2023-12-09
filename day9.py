from utils import *

sequences = [list(map(int, line.split(' '))) for line in read_input(9).split('\n')]

def diff(seq):
    return [seq[i] - seq[i - 1] for i in range(1, len(seq))]

def is_zero(seq):
    return all(x == 0 for x in seq)

def extrapolate(seq, forward=True):
    values = []
    while not is_zero(seq):
        values.append(seq[-1 if forward else 0])
        seq = diff(seq)

    value = 0
    for x in values[::-1]:
        value = x + value if forward else x - value
    return value



task1 = sum(extrapolate(seq) for seq in sequences)
print(task1)

task2 = sum(extrapolate(seq, False) for seq in sequences)
print(task2)