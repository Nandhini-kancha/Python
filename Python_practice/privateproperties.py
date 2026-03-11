# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.__age=age
# p1=Person("nandhu",56)
# print(p1.name)
# print(p1.__age) causes error


#access private property
class Person:
  def __init__(self,name,age):
    self.name=name
    self.__age=age
  def get_age(self):
    return self.__age


P1=Person("nandhu",56)
print(P1.get_age())


#change the value of the private property ,use setter method

class A:
  def __init__(self,name,age):
    self.name=name
    self.__age=age
  def get_age(self):
    return self.__age
  def set_age(self,age):
    if age>0:
      self.__age=age
    else:
      print("age must be positive")


p1=A("nandhu",5)
print(p1.get_age())

p1.set_age(45)
print(p1.get_age())

#protected ---means singe _