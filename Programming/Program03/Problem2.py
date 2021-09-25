log = []
values = input('')
log.append(values)

while values != 'Done':
    values = input('')
    if values == 'Done':
        break
    log.append(values)

for i in range(len(log)):
    log[i] = log[i].split()

def totalDistance(L):
    totalDistance = 0
    subtract = 0
    totalTime = 0
    for i in range(0, len(L)):
        time = int(L[i][1]) - subtract 
        totalDistance += int(L[i][0]) * time 
        subtract = int(L[i][1])
    return totalDistance

print(totalDistance(log))
        
