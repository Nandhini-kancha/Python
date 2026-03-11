a=33
b=30
if a>b:
  print("a is greater than b")
if(a>0):
 print("a is posistive")


 is_logged_in=True
 if is_logged_in:
   print("logged...")
 elif a==b:
   print("a and b are equal")


marks=50
if marks<20 :
  print("grade c")
elif marks<40 :
  print("grade B")
elif marks>=50 :
  print("grade A")

a=50
b=10
if a==b:
  print("1")
elif a>b:
  print("2")
else :
  print("3")

username="nandhu"
if len(username)>0:
  print(f"Welcome {username}")
else:
  print("Error :username cannot be empty")

#a=3 ; print("hii")

marks=20
print("1") if marks>10 else print("2")# conditional expression or ternary operator

a=10
b=20
big=a if a>b else b
print(big)

print(a) if a>b else print("=") if(a==b) else print(b)



#using logical operators
c=4
if a>b and a>c :
  print("a is bigger than b and c")

if a>b or a>c :
  print ("there is a chance of a is bigger than both b and c")

if not a>b:
  print("a is lessthan b")


#nested if
temp=250
if temp>36:
  if temp>50:
   print("temp is greaterthan room and it is sunny")

if temp >200:
   pass  #pass stmt is a null operation -nothing happenps when if executes it serves as a placeholder