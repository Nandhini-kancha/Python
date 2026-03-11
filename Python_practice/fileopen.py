with open("text.txt") as f:
  print(f.read())

f=open("text.txt")
print(f.readline())
f.close()


#reading only parts of file
with open("text.txt") as f:
  print(f.read(5))


#writing into file
with open("text.txt","a") as f:
  f.write("now the file is in append mode")

with open("text.txt") as f:
  print(f.read())

#overwriting the content
f=open("text.txt","w") 
f.write("overwriting the original content")
print(f.readline())