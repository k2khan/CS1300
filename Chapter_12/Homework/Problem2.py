def minmax(values):
    smallest = values[0]
    largest = values[0]
    for i in values:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    return [smallest, largest]

print(minmax([15, 4, 23, 8, 35, 3, 18, 2, 31]))
