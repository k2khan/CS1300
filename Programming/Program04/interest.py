from random import * #This imports the random module

def greeting(): #This is a greeting
    return 'This interest calculator will ask you to select an interest rate, followed by a principal value. It will then calculate and display the principal, interest rate, and balance after one year. You will then be invited to execute the process again or terminate.'


def getPrincipal(limit=1000000):
    principal = 0
    while not 1 <= principal <= limit: #Loop through until correct input
        try:
            principal = input('Enter the principal: ')
            if principal[0] == '$': #Check if input starts with #
                principal = float(principal[1:])
            principal = float(principal) #Convert input to float
            if principal > 1000000: #Can not be more than 1 million
                print('The principal can be at most 1000000\n')
            if principal == 0: #Must be strictly greater than 0
                print('The principal must be greater than 0\n')
            if principal < 0: #Must be a positive number
                print('You must enter a positive amount\n')
        except ValueError: #Risen when the input can not be converted to float
            print('Please enter a valid number\n')
            principal = 0 #Reset the principal to 0 so it can be looped through again
    print(" ")
    return principal 

def computeBalance(principal, rate): #This function computes the balance
    balance = principal + (principal * rate) #Compute the balance
    return balance #Return the value of the balance

def getRate(): #Give the user some options of what interest rate to select
    h = sorted(sample(range(1,20), randint(2,6)))
    print("Please select an interest rate: ")
    a = ['A','B','C','D','E','F']
    b = []
    for i in range(len(h)):
        print(a[i]+') '+str(h[i])+'%')
        b.append(a[i])
    l = len(h) - 1
    rate = input("Enter A-"+str(a[l])+": ")
    while rate not in b:
        print("That is not a valid selection\n")
        print("Please select an interest rate: ")
        for i in range(len(h)):
            print(a[i]+') '+str(h[i])+'%')
        rate = input("Enter A-"+str(a[l])+": ")
    print(" ")
    num = a.index(rate)
    rate = h[num]
    return rate / 100

rate = getRate()
principal = getPrincipal()
balance = computeBalance(principal, rate)

def monthlyBalance(): #Calculates the monthly balance
    monthlyRate = pow(1+rate, 1.0/12) - 1
    monthlyBalance = principal 
    monthlyBalanceList = [principal]
    for i in range(12):
        monthlyBalance += monthlyBalance * monthlyRate
        monthlyBalanceList.append(monthlyBalance)
    return monthlyBalanceList 

monthlyBalance = monthlyBalance()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def displayResults(): #Functions as displaying all of the results that have been accumulated
    global rate
    global principal
    global balance
    global months
    global monthlyBalance
    p = 'Initial Principal'
    r = 'Interest Rate'
    b = 'End of Year Balance'
    print(f'{p:<17}    {r:<13}    {b:<20}') #Header
    print('=' * 57)
    print(f'${principal:<16.2f}    {rate:<13.2f}    ${balance:<20.2f}')
    print(" ")
    m = 'Month'
    s = 'Starting Balance'
    a = 'APR'
    e = 'Ending Balance'
    print(f'{m:<5}    {s:<16}    {a:<3}    {e:<14}')
    print('=' * 50)
    for i in range(12):
        print(f'{months[i]:<5}    ${monthlyBalance[i]:<15.2f}    {rate:<1.2f}   ${monthlyBalance[i+1]:<12.2f}')
    print()

def askYesNo(prompt): #Asks the user if they want to calculate again
    prompt = " ".join(prompt)
    prompt = prompt.split(" ")
    if prompt[0] in ["y","Y"]:
        return True
    if prompt[0] in ['n','N']:
        return False

displayResults() #Starts the program

prompt = input("Another computation? [y/n] ")

print(" ")

while askYesNo(prompt) == True: #Keeps the program running unless user says no
    displayResults()
    prompt = input("Another computation? [y/n] ")
    print(" ")

print("\nGoodbye.")
