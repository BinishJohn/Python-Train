
class C:
  HEADER = '\033[95m'
  B = '\033[94m'
  G = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  E = '\033[0m'
  BOLD = '\033[1m'
  UL = '\033[4m'

global var_global
var_global="Binish John" 

# Build in function globals(). Returns the dictionary of current global symbol table
def function_1():
  print C.BOLD + C.G + "Currnet globals dict : " + C.E
  print  globals()
  print C.UL + C.WARNING + "Value of var_global " + var_global + C.E
  #defining a global variable
  global var_global
  var_global = "John Terry"
  print C.BOLD + C.G + "globals after creating a global variable : " + C.E
  print  globals()
  print C.UL + C.WARNING + "Value of var_global in function_1 " + var_global + C.E


def function_2():
  print C.UL + C.FAIL + "Value of var_global in function_2 " + var_global + C.E
 
def main():
  function_1()
  function_2()

if __name__ == '__main__':
  main()
