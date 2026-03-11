# class myclass:
#   x=5
# p1=myclass()
# print(p1.x)
# p2=myclass()
# print(p2.x)
#__init__() method
# class person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
# p1=person("nandhu",56)
# print(p1.name)
# # print(p1.age)

# class person:
#   def __init__(self,name):
#     self.name=name
#   def printname(self):
#     print(self.name)
# p1=person("nandhu")
# p2=person("sitaram")
# p1.printname()
# p2.printname()

 #self can be not only self ,it can have any name
# class person:
#   def __init__(myobj,name,age):
#     myobj.name=name
#     myobj.age=age
#   def greet(myobj):  #use the slef obj name here
#     print(f"Hello "+myobj.name)
# p1=person("nandhu",56)
# p1.greet()


#modify parameters

# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
# p1=Person("nandhu",20)
# print(p1.age)
# p1.age=90
# print(p1.age)

# del p1.age
# # print(p1.age) causes error


#class Properties and object properties
class Person:
  species ="Human"
  def __init__(self,name):
    self.name=name
p1=Person("nandhu")
p2=Person("Ramayya")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


#modify class properties
Person.species="human beings"
print(p1.species)
print(p2.species)


#adding new properties to object
p1.age=15
p1.city="hyd"
print(p1.age)
print(p1.city)

#Methods Accessing Properties
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1=Person("Nandhu",7)
print(p1.get_info())