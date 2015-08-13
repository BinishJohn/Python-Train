class Car(object):
  def factory(type):
    if type == 'Racecar':
       return Racecar()
    if type == 'Van':
       return Van()
  factory = staticmethod(factory)

class Racecar(Car):
  def drive(self): print "Racecar Driving"

class Van(Car):
  def drive(self): print "Van Driving"
