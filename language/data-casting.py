
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
def func_float():
  print C.BOLD + C.HEADER + C.UL +  "float(x) retruns the floating point value." + C.E
  print C.G + "float(10)		: " + str(float(10)) + C.E    
  print C.G + "float(10.0)		: " + str(float(10.0)) + C.E    
  print C.G + "float(10.00230)		: " + str(float(10.00230)) + C.E    
  print C.G + "float(\"10.231\")		: " + str(float("10.231")) + C.E + "\n\n"    

#build in function str(expression)
def func_str():
  print C.BOLD + C.HEADER + C.UL +  "str(x) retruns the string value." + C.E
  print C.G + "str(float(10))	: " + str(float(10)) + C.E    
  print C.G + "str(10)		: " + str(10) + C.E  + "\n\n"  



def main():
  func_float()
  func_str()

if __name__ == '__main__':
  print C.BOLD + C.UL + "This only executes when %s is executed rather than imported" % __file__ + "\n\n" + C.E
  main()
