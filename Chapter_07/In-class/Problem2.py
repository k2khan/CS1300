k = int(input('Enter k: '))
factorial = 1 
for i in range(1, k + 1):
   factorial *= i
print(str(k) + '! =', str(factorial))
