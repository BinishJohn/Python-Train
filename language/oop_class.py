#1 All classed are derived from object.
#2 Python objects have data and function attributes
#3 Define data attributes in __iniit__
#4 Class attributes are shared across all instances
class Account(object):
  counter = 0 #class varible shared by all the objects

#__init__ is a constructor method which is called when the object is getting created

  def __init__(self,holder,number,balance):
     self.Holder = holder # instance variable unique to every objects
     self.Number = number
     self.Balance = balance
     Account.counter += 1

# __del__ is destructor method which is called when the object is deleted

  def __del__(self):
     print "Deleting Account " + str(self.Number)
     Account.counter -= 1

# Object methods  : Object methods have one specific difference
# from ordinary functions. They mush have an extra first parameter (self) , but you do not
# do not give a value for this parameter when you call the method
# Example : sbi_account= Account("SBI",12123,100)
#           sbi.deposit(200)

  def get_counter(self):
     print self.counter
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

# Class functions
  def show_account_count():
     print "Number of Accounts" , counter



