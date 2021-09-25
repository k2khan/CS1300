sentence = list(input('Enter word and a number: '))
lastIndex = int(sentence[-1])

temp = ''
for i in range(len(sentence)):
    temp = sentence[i:i+lastIndex]
    temp = ''.join(temp)
    print(temp)

