n = int(input('Enter n: '))

total = 0
for i in range(n):
    total = total + (i * (n - i))
print('The sum is', str(total) + '.')
