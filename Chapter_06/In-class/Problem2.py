word = input('Enter a word: ')
word = list(word)
first = word.pop(0).lower()
word.append(first)
word.append('a')
word.append('y')
word = ''.join(word)
word = word.title()
print(word)
