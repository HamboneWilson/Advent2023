import re

file = open('inputs/day3.txt')
lines = file.readlines()

#part1
partNumSum = 0
partNumSet = set()

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
    line = lines[lineNum]
    tempStr = ''
    coordList = []
    
    idx = 0
    while idx < len(line):
        char = line[idx]
        if(not re.match('[0-9]',char)):
            if(tempStr):
                partDict[lineNum][int(tempStr)] = coordList
            tempStr = ''
            coordList = []
            
        else:
            tempStr += char
            coordList.append(idx)
        idx += 1
    
    lineNum += 1

print('done populating partDict')


def mark_part_numbers(lidx, idx):

    for partNumber in partDict[lidx].keys():
        coords = partDict[lidx][partNumber]
        if idx - 1 in coords or idx in coords or idx +1 in coords:
            coords.append('isPart')
            
    return


#go through lines looking for special characters and use their indexes to find part numbers
lineNum = 0
prevSpecialIndexes = []
while lineNum < len(lines):
    line = lines[lineNum]
    idx = 0
    
    while idx < len(line):
        if(not re.match('[0-9\.]',line[idx])):
            if(lineNum > 0):
                #mark real part numbers on the line above current line
                mark_part_numbers(lineNum - 1, idx)
            #mark real part numbers on the current line
            mark_part_numbers(lineNum, idx)
            if(lineNum < len(lines) - 1):
                #mark real part numbers on the line below current line
                mark_part_numbers(lineNum + 1, idx)
        idx += 1
    
    lineNum += 1

for rowNum in partDict.keys():
    for partNumber in partDict[rowNum].keys():
        if 'isPart' in partDict[rowNum][partNumber]:
            partNumSum += partNumber

print("The sum of all part numbers is " + str(partNumSum))
                
            

