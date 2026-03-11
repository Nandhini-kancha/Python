class person:
  def __init__(self,name):
    self.name=name
  def greet(self):
    print("Hello")
p1=person("nandhu")
p1.greet()
del person.greet
# p1.greet() #causes error