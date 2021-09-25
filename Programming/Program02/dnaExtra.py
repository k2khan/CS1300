# ask for user input
dnaSequence = input('Enter a DNA sequence: ')
pattern = input('Enter a pattern: ')

# finds the middle slice using the split() method
reversal = dnaSequence.split(pattern)
reversal = ''.join(reversal)
reversal = reversal.split(pattern[::-1])
reversal = ''.join(reversal)

# get index of the string that will be reversed
reversalIndex = dnaSequence.index(reversal)

# reverse the string
reversal = reversal[::-1]

print('Mutated DNA sequence:', dnaSequence[:4] + reversal + dnaSequence[4 + len(reversal):])



