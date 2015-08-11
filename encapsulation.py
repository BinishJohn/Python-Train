class Encapsulation:
   def __init__ (self, name , age , crush ):
     self.Name = name
     self._Age = age
     self.__Crush = crush
'''
name 	Public
	Can be accessed from inside and outside
_name 	Protected
	Like a public member, but they shouldn't be directly accessed from outside.
__name 	Private
	Can't be seen and accessed from outside

'''
