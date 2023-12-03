file = open('inputs/day2.txt')
lines = file.readlines()

#part1
cubeConfig = {
    'red':12,
    'green':13,
    'blue':14
}
gameCount = 0

for line in lines:
    isValid = True
    gameName = line.split(':')[0]
    gameId = ''.join(filter(str.isdigit, gameName))
    line = line.replace(';','')
    line = line.replace(',','')
    line = line.replace('\n','')
    line = line.split(': ')[1]
    cubeDrawArray = line.split(' ')
    
    while(len(cubeDrawArray)>0):
        qty = cubeDrawArray.pop(0)
        color = cubeDrawArray.pop(0)
        if(cubeConfig[color] < int(qty)):
            isValid = False
    
    if(isValid):
        gameCount += int(gameId)
    
print('Part1: The number sum of valid games ids is ' + str(gameCount))

#part2

totalCubePower = 0

for line in lines:
    line = line.replace(';','')
    line = line.replace(',','')
    line = line.replace('\n','')
    line = line.split(': ')[1]
    cubeDrawArray = line.split(' ')
    
    cubePwrDict = {
        'red':0,
        'green':0,
        'blue':0
    }
    
    cubePower = 1
    
    while(len(cubeDrawArray)>0):
        qty = int(cubeDrawArray.pop(0))
        color = cubeDrawArray.pop(0)
        if(cubePwrDict[color] < qty):
            cubePwrDict[color] = qty
    
    for value in cubePwrDict.values():
        cubePower = cubePower * value
    
    totalCubePower += cubePower
        
    
print('Part2: The total cube power of all games combined is ' + str(totalCubePower))
    
    
