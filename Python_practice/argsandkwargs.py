#using *args
def my_fun(*kids):
  print("the youngest child is ",kids[2])
  print(type(kids)) #tuole

my_fun("ramu","raju","ravi")


#finding max valule
def max_num(*numbers):
  if len(numbers)==0:
    return None
  maxnum=numbers[0]
  for i in numbers:
    if maxnum<i:
      maxnum=i
  return maxnum

maxi=max_num(3,6,12,9,48)
print(maxi)


#kwargs==keyword arguments
def my_func(**kid):
  print("last name is",kid["lname"])

my_func(fname="ravi",lname="raju")

#using **kwargs with regular Arguments
def my_func(username,**details):
  print("username ",username)
  print("additonal details: ")
  for key,value in details.items():
    print("",key+":",value)

my_func("hari",age=78,loc="hyd",faname="ravi")


#unpacking arguments
def unpack(a,b,c):
  return a+b+c
num=[1,2,3]
res=unpack(*num)
print(res)

#unpacking with **
def unpacking(fname,lname):
  print("hello",fname,lname)
person ={"fname":"emanuel","lname":"kashis"}
unpacking(**person)


x=400
def varia():
  x=30
  print(x,"fun") #30
varia()
print(x) #400

#global keywod
def myglobal():
  global xx
  xx=90
  print(xx,"fun")
myglobal()
print(xx)



xx=5
def myglobal():
  global xx
  xx=90
  print(xx,"fun")
myglobal()
print(xx)


#nonlocal keyword
def non():
  x="hari"
  def insidefun():
    nonlocal x
    x="ramesh"
  insidefun()
  return x

print(non())

#LEGB rule
x="global"
def outer():
  x="enclosing"
  def inner():
    x="local"
    print("inner value",x)
  inner()
  print("outer",x)
outer()
print("global",x)