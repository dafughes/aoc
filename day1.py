from utils import *
import re

input = read_input(1)

#Task 1: For each line, concatenate first and last digit. Sum together
task1 = 0    
for line in input.split('\n'):
    digits = [x for x in line if x.isdigit()]
    task1 += int(digits[0] + digits[-1])

print(task1)
    
# Task 2: Digits could be spelled out in english
numbers = 'one|two|three|four|five|six|seven|eight|nine'

# Converts spelled digit to normal digit
def to_digit(s):
    return {x: str(n + 1) for n, x in enumerate(numbers.split('|'))}[s] if not s.isdigit() else s
        

task2 = 0    
for line in input.split('\n'):
    first = re.search('\d|' + numbers, line).group()
    # Reverse line and numbers to find the last digit, then reverse again. Without reversing doesn't work correctly
    # For example line ending in "...eightwo" returns "eight" instead of "two"
    second = re.search('\d|' + numbers[::-1], line[::-1]).group()[::-1]
    
    task2 += int(to_digit(first) + to_digit(second))

print(task2)
    
