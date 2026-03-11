import functools

def changecase(name):
  def inner():
    return name().upper()
  return inner

@changecase
def myfun():
  return "hello"
print(myfun.__name__)

def changecase(func):
  def myinner(*args,**kwargs):
    return func(*args,**kwargs).upper()
  return myinner
@changecase
def myfun(name):
  return "hello"+name
print(myfun("John"))

#using mutliple decorator for one funtiom
def changecase(name):
  def inner():
    return name().upper()
  return inner
def add(func):
  def myinner():
    return "hello"+func()+" have a nice day"
  return myinner

@add
@changecase #first executes this then the upper one executes
def myfun():
  return "tobias" 

print(myfun.__name__)


#accessing attributes or metadata of a func
def myone():
  return "have a nice day"
print(myone.__name__)  #myone