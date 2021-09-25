class ChargeCard:
    def __init__(self, spendingLimit, initialBalance=0):
        self._spendingLimit = spendingLimit
        self._balance = initialBalance 

    def getBalance(self):
        return self._balance

    def getLimit(self):
        return self._spendingLimit

    def charge(self, amount):
        if (self._balance + amount) > self._spendingLimit:
            return False
        self._balance += amount
        return True
        
    def deposit(self, payment):
        self._balance -= payment


