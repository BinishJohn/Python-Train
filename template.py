from string import Template
def func_template():
  templ = Template('Hello $who , how are you')
  name = raw_input("Enter your name :")
  templ.substitute(who = name)
  print templ




if __name__ == '__main__':
  func_template()
