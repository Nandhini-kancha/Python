import math
# print("enter your name")
# name=input()
# print(f"Hello {name}")

# name=input("enter ur name:")
# print(f"Hello {name}")

#converting a input(string) into number
# 6
y=True
while y==True:
  x=input("Enter a number:")
  try:
    x=float(x)
    print(f"entered number is{x}")
    y=False
  except:
    print("wrong input please try again")
print("thankyou")