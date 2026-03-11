fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)
  if x== "banana":
    break

#range function
for c in range(3,5):
  print(c)


# else in a for loop
for x in range(6):
  print(x)
else:
  print("finally finished1")

#else block is not executed if the loop is stopped by break

for x in range(6):
  print(x)
  if x==2:
   break
else:
  print("finally finished")