import re

file = open('inputs/day4.txt')
lines = file.readlines()

#part1
totalValue = 0

for line in lines:
    cardValue = 0
    line = line.strip()
    line = line.replace('  ', ' 0')
    line = line.split(': ')[1]
    sides = line.split(' | ')
    card = sides[0].split(' ')
    winners = sides[1].split(' ')
    
    for num in card:
        if num in winners:
            if cardValue == 0:
                cardValue += 1
            else:
                cardValue = cardValue * 2
    
    totalValue += cardValue

print(totalValue)

#part2
totalScratchCards = 0

for line in lines:
    matches = 0
    line = line.strip()
    line = line.replace('  ', ' 0')
    line = line.split(': ')[1]
    sides = line.split(' | ')
    card = sides[0].split(' ')
    winners = sides[1].split(' ')
    
    for num in card:
        if num in winners:
            matches += 1
    
    totalValue += cardValue

print(totalValue)

    