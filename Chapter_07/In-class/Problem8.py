words = input('Enter some words: ').split()

newMax = 0
for i in words:
    oldMax = ['']
    newMax = max(oldMax, words[i])
newMax = list(newMax)

count = 0
for i in range(newMax):
    count += 1
print(count)
