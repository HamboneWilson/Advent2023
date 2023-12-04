import re
from math import prod

file = open('inputs/day3.txt')
lines = file.readlines()

#part 1 & 2
partNumSum = 0
gearRatioTotal = 0

#build a dictionary of parts and their coordinate data by row number
partDict = {}

lineNum = 0

while lineNum < len(lines):
    partDict[lineNum] = {}
    lineNum += 1
    
print('done building parent dict')

#for each add a key for each part with a list value containing all it's index locations
lineNum = 0
while lineNum < len(lines):
    line = lines[lineNum].strip()
    tempStr = ''
    coordList = []
    
    idx = 0
    while idx < len(line):
        char = line[idx]
        if(not re.match('[0-9]',char)):
            if(tempStr):
                partDict[lineNum][tempStr + (' ' * idx)] = coordList
            tempStr = ''
            coordList = []
            
        else:
            tempStr += char
            coordList.append(idx)
            #if the loop will end after this cycle then add the part number to the list now
            if idx == len(line) - 1:
                if tempStr:
                    partDict[lineNum][tempStr + (' ' * idx)] = coordList
        idx += 1
    
    lineNum += 1

print('done populating partDict')


def mark_part_numbers(lidx, idx):
    partList = []
    for partNumber in partDict[lidx].keys():
        coords = partDict[lidx][partNumber]
        if idx - 1 in coords or idx in coords or idx +1 in coords:
            coords.append('isPart')
            partList.append(int(partNumber.strip()))
            
    return partList


#go through lines looking for special characters and use their indexes to find part numbers
lineNum = 0
while lineNum < len(lines):
    line = lines[lineNum].strip()
    idx = 0
    
    while idx < len(line):
        gearParts = []
        if(not re.match('[0-9\.]',line[idx])):
            if(lineNum > 0):
                #mark real part numbers on the line above current line
                partList = mark_part_numbers(lineNum - 1, idx)
                if line[idx] == '*':
                    gearParts.extend(partList)
                
            #mark real part numbers on the current line
                partList = mark_part_numbers(lineNum, idx)
                if line[idx] == '*':
                    gearParts.extend(partList)
            if(lineNum < len(lines) - 1):
                #mark real part numbers on the line below current line
                partList = mark_part_numbers(lineNum + 1, idx)
                if line[idx] == '*':
                    gearParts.extend(partList)
        if len(gearParts) == 2:
            gearRatioTotal += int(prod(gearParts))
                
        idx += 1
    
    lineNum += 1

for rowNum in partDict.keys():
    for partString in partDict[rowNum].keys():
        if 'isPart' in partDict[rowNum][partString]:
            partNumber = partString.strip()
            partNumSum += int(partNumber)

print("The sum of all part numbers is " + str(partNumSum))

print("The sum of all gear ratios is " + str(gearRatioTotal))              
            

