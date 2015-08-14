global x
try:
  x = float(raw_input("Number :"))
  inverse = 1.0 / x 
except ValueError:
  print "Wrong Data" , x
except ZeroDivisionError:
  print "Divide by zero"
finally:
  try:
    print "Called finally"
    print "Inverse :" , inverse
  except:
    print "Error"
