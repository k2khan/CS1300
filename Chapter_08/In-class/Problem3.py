words = [line.strip() for line in open('words.txt') if line.strip()]

totalCount = 0
vowel = 0
the_vowel = ['a', 'e', 'i', 'o', 'u']

for i in words:
    i.split()
    for c in i:
        if c.isalpha():
            totalCount += 1
        c = c.lower()
        if c in the_vowel:
            vowel += 1

print(vowel)
print(totalCount)
print('The percentrage is', str((vowel / totalCount) * 100))
