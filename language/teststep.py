class TestStep:
  def __init__ (self , status , expected , actual ):
    self.Status = status
    self.Expected = expected
    self.Actual = actual

  def setStatus(self, status):
    self.Status = status
  
  def getStatus(self):
    print self.Status


    

  
