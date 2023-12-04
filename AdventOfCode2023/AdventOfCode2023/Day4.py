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

print("Total value = " + str(totalValue))

#part2
#convert cards to a dictionary of car number key to list containing card and winners strings
cardDict = {}
for line in lines:
    line = line.strip()
    lineKey = line.split(':')[0]
    lineKey = int(lineKey.lstrip('Card '))
    
    line = line.replace('  ', ' 0')
    line = line.split(': ')[1]
    sides = line.split(' | ')
    card = sides[0].split(' ')
    winners = sides[1].split(' ')
    
    cardDict[lineKey] = [card,winners]
    
    
totalScratchCards = 0
currentCardKeys = list(cardDict.keys())
nextCardKeys = []

idx = 0
while idx < len(currentCardKeys):
    key = currentCardKeys[idx]
    card = cardDict[key][0]
    winners = cardDict[key][1]
    
    cardsToAdd = 0
    keyToAdd = key + 1
    
    for num in card:
        if num in winners:
            cardsToAdd += 1
            
    while cardsToAdd > 0:
        nextCardKeys.append(keyToAdd)
        cardsToAdd -= 1
        keyToAdd += 1
    
    idx += 1
    
    if idx == len(currentCardKeys):
        totalScratchCards += len(currentCardKeys)
        currentCardKeys = nextCardKeys
        nextCardKeys = []
        idx = 0
        

print('Total cards ' + str(totalScratchCards))

    