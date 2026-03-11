class Calculator:
  def __init__(self):
    self.result=0
  def __validate(self,num):
    if not isinstance(num ,(int,float)):
      return False
    return True
  def add(self,num):
    if self.__validate(num):
      self.result+=num
    else:
      print("INVALID NUM")


c=Calculator()
c.add(5)
c.add(9)
print(c.result)  #14

# c.__validate() it will throw the error


#name Mangling


class Per:
  def __init__(self,name,age):
    self.name=name
    self.__age=age


p1=Per("nandhu",40)
print(p1._Per__age)  #name Mangling --no error occurs while accessing private properties
  