import re
from utils import *

def parse_grid():
    return [list(line) for line in read_input(14).split('\n')]

def get_rounded_rocks(grid):
    return (Vec2(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == 'O')

def sort_rocks(rocks, tilt_dir):
    if tilt_dir == NORTH:
        return sorted(rocks, key=lambda p: p.y)
    elif tilt_dir == SOUTH:
        return sorted(rocks, key=lambda p: p.y, reverse=True)
    elif tilt_dir == WEST:
        return sorted(rocks, key=lambda p: p.x)
    else:
        return sorted(rocks, key=lambda p: p.x, reverse=True)
    
def tilt(grid, dir):
    h = len(grid)
    w = len(grid[0])

    def is_inside(p):
        return 0 <= p.x < w and 0 <= p.y < h

    def move_rock(pos0):
        pos = pos0
        newpos = pos0 + dir
        while is_inside(newpos) and grid[newpos.y][newpos.x] == '.':
            pos = newpos
            newpos += dir

        grid[pos0.y][pos0.x] = '.'
        grid[pos.y][pos.x] = 'O'

    for rock in sort_rocks(get_rounded_rocks(grid), dir):
        move_rock(rock)

def load(grid):
    return sum(len(grid) - rock.y for rock in get_rounded_rocks(grid))

def to_string(grid):
    return ''.join([''.join(row) for row in grid])

def spin_cycle(grid):
    for d in [NORTH, WEST, SOUTH, EAST]:
        tilt(grid, d)


# Task 1
grid = parse_grid()

tilt(grid, NORTH)
task1 = load(grid)
print(task1)

# Task 2
grid = parse_grid()

states = {}
states[to_string(grid)] = 0

i = 1
while True:
    spin_cycle(grid)
    state = to_string(grid)
    if state in states:
        cycle_start = states[state]
        cycle_len = i - cycle_start
        break

    states[state] = i
    i += 1



n = 1000000000 - cycle_start
r = n % cycle_len

grid = parse_grid()

for i in range(cycle_start + r):
    spin_cycle(grid)

task2 = load(grid)
print(task2)

