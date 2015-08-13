try:
  x = float(raw_input("Number :"))
  inverse = 1.0 / x 
except ValueError:
  print "Wrong Data" , x
except ZeroDivisionError:
  print "Divide by zero"
finally:
  print "Called finally"
  print "Inverse :" , inverse
