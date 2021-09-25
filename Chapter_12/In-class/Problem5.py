def average(data):
    average = 0
    total = 0
    for i in data:
        total += i
    average = total / len(data)
    return average
