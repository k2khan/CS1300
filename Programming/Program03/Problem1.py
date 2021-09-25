length = input('').split()
for i in range(len(length)):
    length[i] = int(length[i])

ordered = True
for i in range(len(length) - 1):
    if length[i] > length[i+1]:
        ordered = False

if ordered:
    print('Ordered')
if not ordered:
    print('Unordered')
