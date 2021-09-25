class ChargeCard:
  def __init__(self, limit, balance=0):
    self._limit = limit
    self._balance = balance
    
  def getBalance(self):
    return self._balance
    
  def getLimit(self):
    return self._limit
    
  def deposit(self, amount):
    if amount > 0:
      self._balance -= amount
    
  def charge(self, amount):
    if amount + self._balance <= self._limit:
      self._balance += amount
      return True
    else:
      return False
