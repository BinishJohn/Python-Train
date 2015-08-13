
class C:
  HEADER = '\033[95m'
  B = '\033[94m'
  G = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  E = '\033[0m'
  BOLD = '\033[1m'
  UL = '\033[4m'

#build in function input(x)
def func_input():
  print C.BOLD + C.HEADER + C.UL +  "Input Function." + C.E
  name="empty"
  print "Type(name)" + str(type(name))
  name = input("Enter Your Name : (Remember Your Name Is Not Number) ")
  print "Type(name)" + str(type(name))
  age = 0
  print "Type(age)" + str(type(age))
  age = input("Enter Your Age : ")
  print "Type(age)" + str(type(age))
  print "Hello " + C .BOLD + C.FAIL + name + " ("+ str(age)  +" )"+  C.E + "\n\n"

#build in function raw_input(x)
def func_raw_input():
  print C.BOLD + C.HEADER + C.UL +  "Raw Input Function." + C.E
  name="empty"
  print "Type(name)" + str(type(name))
  name = raw_input("Enter Your Name : (Remember Your Name Is Not Number , Python is Intelligent !!) ")
  print "Type(name)" + str(type(name))
  age = 0
  print "Type(age)" + str(type(age))
  age = raw_input("Enter Your Age : ")
  print "Type(age)" + str(type(age))
  print "Hello " + C .BOLD + C.FAIL + name + " ("+ str(age)  +" )"+  C.E + "\n\n"



def main():
  func_input()
  func_raw_input()

if __name__ == '__main__':
  print C.BOLD + C.UL + "This only executes when %s is executed rather than imported" % __file__ + "\n\n" + C.E
  main()
