file = open('inputs/day2.txt')
lines = file.readlines()

#part1
cubeConfig = {
    'red':'12',
    'green':'13',
    'blue':'14'
}
gameCount = 0

for line in lines:
    line = line.replace(';',',')
    line = line.split(':')[1]
    
    
