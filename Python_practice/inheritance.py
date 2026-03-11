# class Person:
#   def __init__(self,fname,lname):
#     self.firstname=fname
#     self.lastname=lname
#   def printname(self):
#     print(self.firstname,self.lastname)
# class student(Person):
#   pass
# x=student("nandhu","raju")
# x.printname()
# x=Person("John","doe")
# # x.printname()


#overriding parent init()
class Person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
    self.fullname =fname+" "+lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(Person):
  def __init__(self,fname,lname):
    Person.__init__(self,fname,lname)
    self.firstname=fname
    self.lastname=lname
    

x=student("nandhu","raju")
y=Person("hello","world")
x.printname()
print(x.fullname)  # fullname attribute will not print value if we dont call parent constructor
y.printname()