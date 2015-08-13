from os.path import exists
print exists('write.txt')
file_object = open ('write.txt','r')
print file_object.readline()
file_object = open ('write.txt','r')
print str(file_object.read())
file_object = open ('write.txt','r')
print file_object.readline(11)
