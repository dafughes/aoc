from utils import *
import re, math

input = read_input(8).split('\n\n')

instructions = input[0]
network = {line.split('=')[0].strip(): re.findall('\w+', line.split('=')[1].strip()) for line in input[1].split('\n')}

def num_steps(instructions, network, current_node, task=1):
    def is_target(node):
        return node == 'ZZZ' if task == 1 else node[-1] == 'Z'

    i = 0
    while not is_target(current_node):
        instruction = instructions[i % len(instructions)]
        j = 0 if instruction == 'L' else 1
        current_node = network[current_node][j]

        i += 1
    
    return i

# Task 1
task1 = num_steps(instructions, network, 'AAA')
print(task1)

# Task 2
# Least common multiple of step count for all starting positions
nodes = [node for node in network if node[-1] == 'A']
steps = [num_steps(instructions, network, node, 2) for node in nodes]
task2 = 0
print(math.lcm(*steps))

