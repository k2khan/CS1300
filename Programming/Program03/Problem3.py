numbers = input('').split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    max1 = numbers[i]
    if numbers[i] > max1:
        max1 = numbers[i]

for i in range(len(numbers)):
    max2 = numbers[i]
    if (numbers[i] > max2) and (numbers[i] <= max1):
        max2 = numbers[i]

print(max1, max2)
