global x
global inverse
inverse = 0
try:
  x = float(raw_input("Number :"))
  inverse = 1.0 / x 
except ValueError:
  print "Wrong Data" , x
except ZeroDivisionError:
  print "Divide by zero"
finally:
    print "Finally"
    print inverse
