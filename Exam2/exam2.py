def readFile(filename):
    userList = []
    try:
        with open(filename) as data:
            data.readline()
            for line in data:
                eachLine = line.rstrip().split(',')
                user = SysUser(eachLine)
                userList.append(user)
    except FileNotFoundError or ValueError:
        print('Invalid file name')
    return userList


class SysUser:
    def __init__(self, userList):
        self._firstName = userList[0]
        self._middleName = userList[1]
        self._lastName = userList[2]
        self._password = userList[3]
        self._securityQuestion = userList[4]
        self._securityAnswer = userList[5]
        self._age = userList[6]
        

    def getName(self):
        return self._firstName + ' ' + self._middleName[0] + '.' + ' ' + self._lastName

    def getUsername(self):
        return self._firstName[0].lower() + self._middleName[0].lower() + self._lastName[0:6].lower()

    def getAge(self):
        return int(self._age)

    def checkPassword(self, entered):
        if entered != self._password:
            return False
        return True

    def getSecQuestion(self):
        return int(self._securityQuestion)

    def checkSecAnswer(self, entered):
        if entered != self._securityAnswer:
            return False
        return True

    def setSecQuestion(self, num):
        self._securityQuestion = int(num)

    def setSecAnswer(self, answer):
        self._securityAnwer = answer


header = f'    Name                    Username         Age \n-----------                 --------         ---'


# Function for testing user logins
def loginUser (users, username, inputPass='', inputSecAns=''):
    print ()
    print ('username:  ' + username)

    idx = -1
    for i in range(len(users)):
        if (username == users[i].getUsername()):
            idx = i

    loginValid = True

    if (idx < 0):
        print ('*** Username invalid')
        loginValid = False

    print ('password:  ' + inputPass)
    if not users[idx].checkPassword(inputPass):
        print ('*** Password invalid')
        loginValid = False

    print (sec_ques[users[idx].getSecQuestion()] + '  ' + inputSecAns)
    if not users[idx].checkSecAnswer(inputSecAns):
        print ('*** Security answer invalid')
        loginValid = False

    if loginValid:
        print ('*** Welcome, ' + users[idx].getName())
    else:
        print ('*** Login failed.  Please try again.')

    return loginValid


# Given list of security questions
sec_ques = [ 'What\'s your favorite color?',
                'In what city was your mother born?',
                'What\'s the name of your first pet?',
                'What\'s the name of your favorite sports team?',
                'What was the make of your first car?',
                'What\'s your school mascot?' ]


#### Test cases for testing user logins
if __name__ == '__main__':
    # This first test case will fail
    users = readFile ('sysUsers.csv')
    
    # This test case will work
    users = readFile ('sys_users.csv')
    
    # The first login is valid, while the other three fail (for different reasons)
    loginUser (users, 'jtrobins', 'mightyMouse', 'Honda')
    loginUser (users, 'tpbradshaw', 'endZone', 'Steelers')
    loginUser (users, 'jagarner', 'uglyPeople', 'Big Red')
    loginUser (users, 'dsbrown', 'bubbleGum', 'Atalnta')
    
    print ()
    
    # Here, put your code for printing out the names, usernames, and ages of
    #   the users of your system
    
print(header)    

for person in readFile('sys_users.csv'):
    display = f'{person.getName():<20}        {person.getUsername():<8}         {person.getAge():>3}'
    print(display)


