def count(n):
  count=1
  while count <=n:
    yield count
    count +=1

for num in count(5):
  print(num)

#slicing operatoe []
