

def function_1():
   print "Function One"


def function_2(name):
   print "Hello " , name

def function_3(name,age):
   print "Hello " , name , age

def function_4(name):
   return name


def function_5(name, age=26):
   print "Hello " , name , age

def function_6(name,age):
   return name , age

def function_7():
   function_5("Calling Function 6 from 7", 12)
