calTotal = 0

day1File = open('inputs/day1.txt')
lines = day1File.readlines()

#part1
for line in lines:
    numStr = ''.join(filter(str.isdigit, line))
    calStr = None
    
    if(len(numStr) > 1):
        calStr = numStr[0] + numStr[len(numStr) - 1]
    elif(len(numStr) == 1):
        calStr = numStr + numStr
    else:
        continue

    calTotal += int(calStr)
    
print('Part1: the total of the calibration values is ' + str(calTotal))

#part2
calTotal = 0

numDict = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

for line in lines:
    print('Starting new line ' + line)
    tempStr = ''
    numStr = ''
    calStr = ''
    index = 0
    
    
    while(index < len(line)):
        keyfound = False
        char = line[index]
        tempStr += line[index]
        
        for key in numDict.keys():
            if key in tempStr:
                numStr += numDict[key]
                keyfound = True
                break   
                
        if(keyfound):
            tempStr = ''
            continue
            #continue while loop without updating the index, so we can catch instances of twone
        elif(str.isdigit(char)):
            numStr += char
            tempStr = ''
            index += 1
        elif(len(tempStr) == 5):
            tempStr = ''
            #roll the index back to the next character after this tempstr began and start scanning again
            index -= 3
        else:
            index += 1
            
    if(len(numStr) > 1):
        calStr = numStr[0] + numStr[len(numStr) - 1]
    elif(len(numStr) == 1):
        calStr = numStr + numStr
    else:
        continue
    
    print('All numbers = ' + numStr)
    print('First and last =' + calStr)
    calTotal += int(calStr)
    print('Calibration total = ' + str(calTotal) + '\n')
    
print('Part2: the total of the calibration values is ' + str(calTotal))
