integers = int(input(''))

def sumDigit(n):
    s = 0
    while n:
        s += n % 10
        n = n // 10
    return s
    

def repeatedSum(number):
    if len(str(number)) == 1:
        return number
    if number % 9 == 0:
        return 9 
    digitSum = sumDigit(number)
    return repeatedSum(digitSum)

print(repeatedSum(integers))
