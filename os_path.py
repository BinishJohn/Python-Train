#OS.Path Module Contains functions to interact with Operating File System
from sys import argv
import os.path
script , directory = argv

def ls():
  print "Directory Listing for directory :" + directory
  filenames = os.listdir(directory)
  for filename in filenames:
     print "Filename :" + filename
     print "Relative File Path :" +  os.path.join(directory, filename)
     print "Absolute File Path :" + os.path.abspath(os.path.join(directory,filename))


if __name__ == '__main__':
  ls()
