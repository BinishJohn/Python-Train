
class C:
  HEADER = '\033[95m'
  B = '\033[94m'
  G = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  E = '\033[0m'
  BOLD = '\033[1m'
  UL = '\033[4m'

#build in function float(x)
def func_print_with_condition():
  print C.BOLD + C.HEADER + C.UL +  "Print with condition." + C.E
  a = 10
  print "Value of a = " + str(a)
  print C.G + "print(\" A is Even\" , \" A is Odd \") [ a % 2 == 0] " + C.E
  print "[ a % 2 == 0] " + str( a % 2 == 0) 
  print ("A is Odd" , "A is Even") [ a % 2 == 0]    


def main():
  func_print_with_condition()

if __name__ == '__main__':
  print C.BOLD + C.UL + "This only executes when %s is executed rather than imported" % __file__ + "\n\n" + C.E
  main()
