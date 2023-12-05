from utils import *
import re, math

input = read_input(2)

task1 = 0
task2 = 0
for line in input.split('\n'):
    values = re.findall('\d+|red|green|blue', line)
    id = int(values[0])

    # Task 1: Find out which games are possible if bag contains 12/13/14 cubes
    # Calculate max cubes for each game
    max_cubes_revealed = {'red': 0, 'green': 0, 'blue': 0}
    for i in range(1, len(values), 2):
        amount = int(values[i])
        color = values[i + 1]
        max_cubes_revealed[color] = max(max_cubes_revealed[color], amount)
    
    # Check if game is possible
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    if all(max_cubes_revealed[c] <= max_cubes[c] for c in max_cubes):
        task1 += id

    # Task 2: Calculate minimum number of cubes needed for each game
    # Multiply max_cubes_revealed together
    task2 += math.prod(map(lambda x: max_cubes_revealed[x], max_cubes_revealed))


print(task1)
print(task2)
        
    
    



