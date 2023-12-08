from utils import *
import re, math
import itertools

def hand_type(counts):
    def n_same(n):
        return sum(counts[x] == n for x in counts)

    if n_same(5): return 6
    elif n_same(4): return 5
    elif n_same(3) and n_same(2): return 4
    elif n_same(3): return 3
    elif n_same(2) == 2: return 2
    elif n_same(2): return 1
    else: return 0


def hand_strength(cards, task=1):
    card_order = '23456789TJQKA' if task == 1 else 'J23456789TQKA'
    card_strengths = sum((card_order.index(x) << (16 - i * 4)) for i, x in enumerate(cards))
    
    counts = {card: cards.count(card) for card in cards}
    
    if task == 1 or 'J' not in counts:
        return (hand_type(counts) << 20) + card_strengths
    
    fixed_part = [x for x in cards if x != 'J']
    c = [x for x in card_order if x != 'J']
    length = len(cards) - len(fixed_part)

    comb = itertools.combinations_with_replacement(c, length)

    best_hand = 0
    for x in comb:
        hand = fixed_part + list(x)
        best_hand = max(best_hand, hand_type({card: hand.count(card) for card in hand}))

    return (best_hand << 20) + card_strengths
   
    

hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in read_input(7).split('\n')]

hands = sorted(hands, key=lambda x: hand_strength(x[0]))

task1 = sum((i + 1) * x[1] for i, x in enumerate(hands))
print(task1)

hands = sorted(hands, key=lambda x: hand_strength(x[0], 2)) 
task2 = sum((i + 1) * x[1] for i, x in enumerate(hands))
print(task2)