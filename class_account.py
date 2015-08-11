class Account(object):
  counter = 0
  def __init__(self,holder,number,balance):
     self.Holder = holder
     self.Number = number
     self.Balance = balance
     Account.counter += 1

  def __del__(self):
     print "Deleting Account " + str(self.Number)
     Account.counter -= 1

  def deposit(self, amount):
     self.Balance = self.Balance + amount

  def withdraw(self, amount):
     if(self.Balance - amount < 0):
       print "You don't have enough balance on your account"
       self.show_balance()
     else:
       self.Balance = self.Balance -  amount
       print amount , " Withdrawn from your account " , self.Number
       self.show_balance()

  def show_balance(self):
     print "Current Balance Is " , self.Balance
