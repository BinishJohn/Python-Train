class Me:
  __age = 26
  __crush = "Racing"
  name = "Binish"

  def __init__(self):
    self.__age = 26
    self.__crush = "Racing"
    self.name = "Binish"

  def me(self):
    print self.__age
    print self.__crush

  def __hack_me(self):
    self.__age = 27
    self.__crush = "Computers"

  def hack(self):
    self.__hack_me()
