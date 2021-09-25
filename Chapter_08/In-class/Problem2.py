words = [line.strip() for line in open('words.txt') if line.strip()]

count = 0
for i in words:
    if '-to-' in i:
        count += 1

print(count)

