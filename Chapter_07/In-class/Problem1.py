numbers = input('Enter numbers: ')
numbers = numbers.split()
sum = 0
for i in numbers:
    sum += int(i)
print('The sum is', str(sum))
