def threshold(values, goal):
    count = 0
    total = 0
    for i in values:
        count += 1
        total += i
        if total > goal:
            return count 
    return 0

print(threshold([5, 3, 8, 2, 9, 1], 17))
