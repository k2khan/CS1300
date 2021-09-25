heightInImperial = input('What is your height? ')
heightInImperial = heightInImperial.split("'")
feet = int(heightInImperial[0]) * 12
inches = int(heightInImperial[1][:-1])

feetInMetric = feet * 2.54
inchesInMetric = inches * 2.54

print('That is', feetInMetric + inchesInMetric, 'centemeters.')
