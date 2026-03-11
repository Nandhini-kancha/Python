def my_func():
  print("hello from a function")

my_func()


def hello(name):
  print("hello "+name)

hello("nandhu")


#default values to parameter
def my_fun(name="friend"):
  print("hello WOrld ",name)

my_fun("emil")
my_fun("rani")
my_fun(9)
my_func()


#function that returns list
def my_func():
  return ["apple","banana","cherry"]
fruits=my_func()
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[2])


#/ means positional arguments only
def myfun(name,/):
  print("hello")
myfun("nandhu")

#keyword only argument
def myfun(*,name):
  print("hello",name)
myfun(name="nandhu")

#combing positional only and keyword only
def myfunc(a,b,/,*,c,d):
  return a+b+c+d
result=myfunc(5,10,c=12,d=89)
print(result)