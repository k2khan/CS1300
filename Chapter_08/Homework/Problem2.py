words = ['racecar', 'anna', 'civic', 'madam', 'mom', 'noon', 'RaceCar']
palindromes = []

for i in (words):
    i = i.lower()
    if len(i) >= 5:
        if i[::-1] == i:
            palindromes.append(i)

print(palindromes)
