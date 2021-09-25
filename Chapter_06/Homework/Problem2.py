name = input('What is your name? ')
name = name.split()
name[1] = name[1][0] + '.'
name = ' '.join(name)
print(name)
