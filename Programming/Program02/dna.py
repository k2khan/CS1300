# ask for user input
dnaSequence = input('Enter a DNA sequence: ')
pattern = input('Enter a pattern: ')

# last index of first inverted pair 
firstSubstring = dnaSequence.find(pattern) + len(pattern)

# first index of last inverted pair 
# only looks after the first occurence of the first inverted pair
lastSubstring = dnaSequence.find(pattern[::-1], firstSubstring)

# find middle slice and reverse it
middleSlice = dnaSequence[firstSubstring:lastSubstring]
middleSlice = middleSlice[::-1]

print('Mutated DNA sequence:', dnaSequence[:firstSubstring] + middleSlice + dnaSequence[lastSubstring:])
