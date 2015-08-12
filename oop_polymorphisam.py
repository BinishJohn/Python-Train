#Different subclasses can be treated like the parent class, but execute their specialized behavior
#Polymorphisam exists when you define a number of subclassed which have commonly names methods
#Example :

class Animal:
  def __init__(self, name) :
     self.name = name

  def talk(self):
     pass


class Cat(Animal):
  def __init__(self,name) :
    self.name = name


  def talk(self) :
    print "Meow"


class Dog(Animal):
  def __init__(self,name) :
    self.name = name

  def talk(self):
    print "Woof"
   
