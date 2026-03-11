try:
  print(x)
except:
  print("an exception occured")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("something is happened")
else:
  print("nothing went wrong")  #else will execute if try is executed 


try:
  f=open("demofile.txt")
  try:
   f.write("hi hello")
  except:
   print("something went wrong")
  finally:
   f.close()
except:
  print("something went wrong when opening the file")



# x=-1
# if x<0:
#   raise Exception("sorry..!negative value")  #raise keyword is use to raise the exception
# x="hello"
# if not type(x) is int:
#   raise TypeError("only integers are allowed")