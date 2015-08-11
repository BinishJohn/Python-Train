from sys import argv

script, first_var, second_var, third_var = argv
print "Script Name : " + script
print "First Variable : " + first_var
print "Second Variable : " + second_var
print "Third Variable : " + third_var
print "Sum of arguments " + (first_var + second_var + third_var)
print "Sum of arguments " + str(int(first_var) + int(second_var) + int(third_var))
print "Product of argument {0}".format(int(first_var) * int(second_var) * int(third_var))
