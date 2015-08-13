def func_format():
  print '{0}, {1} , {2}'.format('Hello' ,'Hai', 'Hi')
  print '{1}, {1} , {0}'.format('Hello' ,'Hai', 'Hi')
  print '{2}{1},{0}'.format('Hello' ,'Hai', 'Hi')
  print 'Months : {jan},{feb}'.format( jan = 'January' , feb='February')
  print '{:<30}'.format('Left')
  print '{:#>30}'.format('Right')
  print '{:^30}'.format('Center')
  print '{:$^30}'.format('Filler')
  print '{:,}'.format(12312312)
  print '100/2 Percentage: {:.2%}'.format(.50)

  
  


def main():
  func_format()

if __name__ == '__main__':
  main()
