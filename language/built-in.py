
class C:
  HEADER = '\033[95m'
  B = '\033[94m'
  G = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  E = '\033[0m'
  BOLD = '\033[1m'
  UL = '\033[4m'
#built in function abs(c)
def func_abs():
  print C.BOLD + C.HEADER + C.UL + "abs(x) return the absolute value of a numnber.If the argument is complex numbers then ,its magnitude is returned" + C.E
  print C.G + "Absolute Value Of 10	abs(10)    : " + str(abs(10)) 
  print C.G + "Absolute Value of 10.7	abs(10.7)  : " + str(abs(10.7))
  print C.G + "Absolute Value of -10	abs(-10)   : " + str(abs(-10))
  print C.G + "Absolute Value of 2+3j	abs(2+3j)  : " + str(abs(2+3j)) + C.E
  print C.B + "Absolute value describes the distance of a number on a the number line from 0 without considering which direction from zero.\n*** abs of a number is never negative\n\n" + C.E


#build in function bin(c)
def func_bin():
  print C.BOLD + C.HEADER + C.UL + "bin(x) convert x into binary string." + C.E
  print C.G + "Binary Value Of 10	bin(10)    : " + (bin(10)) 
  print C.G + "Binary Value of -10	bin(-10)   : " + (bin(-10)) + C.E + "\n\n"


#build in function hex(c)
def func_hex():
  print C.BOLD + C.HEADER + C.UL + "hex(x) convert x into hex value." + C.E
  print C.G + "Hex Value Of 10 hex(10)		: " + (hex(10)) 
  print C.G + "Hex Value of -10 hex(-10)	: " + (hex(-10)) + C.E + "\n\n"

#build in function int(c)
def func_int():
  print C.BOLD + C.HEADER + C.UL + "int(x) convert x into hex value." + C.E
  print C.G + "Integer Value Of 10.5 int(10.5)		: " + str(int(10.5)) 
  print C.G + "Integer Value of \"20\" int(\"20\")	: " + str(int("20")) + C.E 
  print C.G + "Integer Value of 0xff int(0xff)		: " + str(int(0xff)) + C.E + "\n\n"
  
  


#build in function bool(c)
def func_bool():
  print C.BOLD + C.HEADER + C.UL +  "bool(x) returns the boolean." + C.E
  print C.G + "Boolean Value Of 10		bool(10)	: " + str(bool(10))
  print C.G + "Boolean Value Of -10		bool(-10)	: " + str(bool(-10))
  print C.G + "Boolean Value Of true		bool(true)	: " + str(bool(10))
  print C.G + "Boolean Value Of \"false\" 	bool(\"false\")	: " + str(bool("false"))
  print C.G + "Boolean Value Of 1		bool(1)		: " + str(bool(1))
  print C.G + "Boolean Value of 0		bool(0)		: " + str(bool(0)) + C.E + "\n\n"

#build in function chr(c)
def func_chr():
  print C.BOLD + C.HEADER + C.UL +  "chr(x) returns character representation of ASCII code." + C.E
  print C.G + "Character value of 65		chr(65)		: " + str(chr(65)) + C.E 
  print C.G + "Character value of 97		chr(97)		: " + str(chr(97)) + C.E + "\n\n"

#build in function cmp(c)
def func_cmp():
  print C.BOLD + C.HEADER + C.UL +  "cmp(x,y) compare two values and return an integer based on comparison." + C.E
  print C.G + "cmp(10,20)		: " + str(cmp(10,20))
  print C.G + "cmp(100,100)		: " + str(cmp(100,100))
  print C.G + "cmp(30,20)		: " + str(cmp(30,20))
  print C.G + "cmp(0,-10)		: " + str(cmp(0,-10))
  print C.G + "cmp('B',1) 		: " + str(cmp('B',1))
  print C.G + "cmp('A','B') 		: " + str(cmp('A','B'))
  print C.G + "cmp('A','A') 		: " + str(cmp('A','A'))
  print C.G + "cmp('A','a')		: " + str(cmp('A','a')) + C.E + "\n\n"

#build in function eval(expression)
def func_eval():
  print C.BOLD + C.HEADER + C.UL +  "eval(expression) parse and evaluvated as python expression." + C.E
  print C.G + "eval(\'2+2\')		: " + str(eval('2+2')) + C.E 
  print C.G + "eval(\'chr(97)\')		: " + str(eval('chr(97)')) + C.E + "\n\n"


def main():
  func_abs()
  func_bin()
  func_bool()
  func_hex()
  func_int()
  func_chr()
  func_cmp()
  func_eval()

if __name__ == '__main__':
  print C.BOLD + C.UL + "This only executes when %s is executed rather than imported" % __file__ + "\n\n" + C.E
  main()
