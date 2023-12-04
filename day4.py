from utils import *

input = read_input(4)

# Only information needed is number of matches per card
cards = []

# Parse input
for line in input.split('\n'):
    a, b = line.split('|')
    winning_numbers = [x for x in a.split(' ') if x.isdigit()]
    your_numbers = [x for x in b.split(' ') if x.isdigit()]
    
    matches = set(winning_numbers) & set(your_numbers)
    cards.append(len(matches))


# Task1: Card value is 2 ** (matches - 1) or 0
task1 = sum(int(2 ** (n - 1)) if n > 0 else 0 for n in cards)
print(task1)

# Task2: Winning cards copy [number of matches] subsequent cards which must be processed similarly, count all processed cards
L = len(cards)
card_amounts = [1] * L
for i in range(L):
    for k in range(card_amounts[i]):
        for j in range(i + 1, min(L, i + 1 + cards[i])):
            card_amounts[j] += 1
    

print(sum(card_amounts))




    
    

