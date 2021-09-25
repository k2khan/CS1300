states = []

with open('states.csv') as inputFile:
    for line in inputFile:
        linelist = line.split(',')
        state = linelist.pop(0)
        for i in range(len(linelist)):
                linelist[i] = int(linelist[i])
        states.append((state, linelist))

print(states)
