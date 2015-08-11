
class C:
  HEADER = '\033[95m'
  B = '\033[94m'
  G = '\033[92m'
  WARNING = '\033[93m'
  F = '\033[91m'
  E = '\033[0m'
  BOLD = '\033[1m'
  UL = '\033[4m'

#build in function str(x)
def func_string():
  print C.BOLD + C.HEADER + C.UL +  "Print with condition." + C.E
  var = "Hello How Are You"
  print "Variable :" + var
  print "Length Of String - len() "  + C.F + str(len(var)) + C.E
  print "Type Of String type() "  + C.F + str(type(var)) + C.E
  print "Casting str(value) " +  C.F + str(20) + C.E
  print "Convert to Upper Case " +  C.F + var.upper()  + C.E
  print "Convert to Lower Case " +  C.F + var.lower() + C.E
  print "Get Hello From var var[0:6] "  + C.F + var[0:6] + C.E
  print "var[0:] "  + C.F + var[0:] + C.E
  print "var[:5] "  + C.F + var[:5] + C.E
  print "var[:-5] "  + C.F + var[:-5] + C.E
  print "var[-9:-1] "  + C.F + var[-9:-1] + C.E
  print "Membership - in ( Hello in var )" 
  print "Hello" in var  + C.E
  print "Membership - in ( hello in var )" 
  print "hello" in var  + C.E
  print "Membership - in ( John in var )" 
  print "John" in var  + C.E
  print "Membership - Not in ( Hello not in var )" 
  print "Hello" not in var  + C.E
  print "Repeater * ( var * 3 ) " + var * 3  + C.E
  print "\n\n"


  


def main():
  func_string()

if __name__ == '__main__':
  print C.BOLD + C.UL + "This only executes when %s is executed rather than imported" % __file__ + "\n\n" + C.E
  main()
