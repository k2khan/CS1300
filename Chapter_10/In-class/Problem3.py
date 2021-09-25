print('Start entering words: ')
test = input('')
newWord = ''

count = 0
while test != newWord:
    newWord = input('')
    count += 1

print('You already entered', test)
print('You listed', count, 'distinct words.')
