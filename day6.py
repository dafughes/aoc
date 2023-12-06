from utils import *
import re, math

input = read_input(6).split('\n')
input = list(zip(list(map(int, re.findall('\d+', input[0]))), list(map(int, re.findall('\d+', input[1])))))

def quadratic_solutions(a, b, c):
    x0 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
    x1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
    return (x0, x1)
    
def num_ways_to_win(game):
    distance_to_beat = game[1]
    total_time = game[0]
    
    solutions = quadratic_solutions(-1, total_time, -distance_to_beat)
    n0 = math.ceil(min(solutions))
    if n0 == min(solutions):
        n0 += 1

    n1 = math.floor(max(solutions))
    if n1 == max(solutions):
        n1 -= 1
    
    return (n1 - n0) + 1
    
task1 = math.prod(map(num_ways_to_win, input))
print(task1)

input = read_input(6).split('\n')
time = int(''.join(re.findall('\d+', input[0])))
distance = int(''.join(re.findall('\d+', input[1])))

task2 = num_ways_to_win((time, distance))
print(task2)


