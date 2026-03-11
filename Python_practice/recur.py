def count(n):
  if n<0:
    print ("Done")
  else:
    print(n)
    count(n-1)
  
count(3)


def fac(n):
  if n==0 or n==1 :
    return 1
  else :
    return n*fac(n-1)

print(fac(5))  #120
