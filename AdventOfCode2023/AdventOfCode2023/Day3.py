file = open('inputs/test.txt')
lines = file.readlines()

#part1
partNumSum = 0
partNumSet = {}

#build a dictionary of keys to dictionary. Number of keys should match the number of lines
coordDict = {
    0:{0:[]}
}

idx = 0

while idx < len(lines):
    coordDict[idx] = {0:{}}
    idx += 1
    
print('done building parent dict')

#for each key, populate it's dictionary with a key to empty set. Keys size should match the length of a line in lines
lineIdx = 0

for key in coordDict.keys():
    idx = 0
    
    while idx < len(lines[lineIdx]):
        coordDict[key][idx]={}
        idx += 1
        
    lineIdx += 1


print('done nesting child dicts')

#find part numbers in each line and map them into the coordDict
lineNum = 0
while lineNum < len(lines):
    line = lines[lineNum]
    tempStr = ''
    coordList = []
    
    idx = 0
    while idx < len(line):
        char = line[idx]
        coordList.append(idx)
        if (not char.isdigit):
            if(tempStr):
                for coord in coordList:
                    coordDict[lineNum][coord].append(int(tempStr))
                tempStr = ''
        else:
            tempStr += char
        idx += 1
    
    lineNum += 1

print('done mapping part numbers to coord map')
                
            

