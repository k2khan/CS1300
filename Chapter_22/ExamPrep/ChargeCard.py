import random

class ChargeCard:

  def randomNumber():
    randomNumber = ''
    firstNumber = str(random.randint(1,9))
    randomNumber += firstNumber
    for i in range(0, 8):
      number = str(random.randint(0,9))
      randomNumber += number
    return randomNumber

  def __init__(self, name, limit, accountNumber=randomNumber(), balance=0):
    if not isinstance(name, str):
        raise ValueError('Please enter a valid name')
    self._name = name
    self._accountNumber = accountNumber
    if not isinstance(limit, int):
      self._limit = 1000        # some default value
    elif limit < 0:
      self._limit = 1000        # some default value
    else:
      self._limit = limit

    if not isinstance(balance, int):
      self._balance = 0
    else:
      self._balance = balance

    self._log = f'New card created for {self._name:>8} with \n account number {self._accountNumber}, \n spending limit of ${self._limit:0.2f}, \n initial balance of ${self._balance:0.2f}.\n'


  def getName(self):
      return self._name

  def getAccountNum(self):
      return self._accountNumber

  def getBalance(self):
    return self._balance
    
  def getLimit(self):
    return self._limit
    
  def deposit(self, amount):
    if isinstance(amount, int) and amount > 0:
      self._balance -= amount
      self._log += f'${amount:0.2f} deposit, new balance = ${self._balance:0.2f}.\n'
    
  def charge(self, amount):
    if not isinstance(amount, int):
      return False
    if amount <= 0:
      return False
    if amount + self._balance <= self._limit:
      self._balance += amount
      self._log += f'${amount:0.2f} charge, new balance = ${self._balance:0.2f}.\n'
      return True
    else:
      self._log += f'${amount:0.2f} charge, denied.\n'
      return False
    
  def __str__(self):
    return self._log

if __name__ == '__main__':
    visa = ChargeCard('Bob Smith', 1000, 818624988)
    print (visa)

