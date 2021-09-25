import math as m

n = int(input('Enter n: '))
total = 0
for i in range(n):
    total += (1 / m.factorial(i))
print(total)

