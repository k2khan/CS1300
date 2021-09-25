from random import *

flips = []
trials = 0
count = 0
totalCount = 0

while totalCount < 10000:
    f = randint(0, 1)
    if f == 0:
        count += 1
    trials += 1 
    if count == 6:
        totalCount += 0
        count = 0
        flips.append(trials)
        break

print(trials)
print(min(flips))
print(max(flips))
