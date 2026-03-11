import re

txt="The rain is spain"

x=re.findall("ai",txt)
x2=re.findall("portugese",txt)

print(x)
print(x2)

#search function
txt="the rain in spain"
x=re.search("\s",txt)
print("the first white space character is located in position ",x.start())

#split function
x=re.split("\s",txt)
print(x)

#max split parameters
x=re.split("\s",txt,1)
print(x)   #"the","rain in spain"


#subfunction
x=re.sub("\s","9",txt)  # replaces every cahracter with 9
print(x)



x=re.sub("\s","9",txt,2)  # replaces every cahracter with 9
print(x)

#match object
x=re.search("ai",txt)
print(x)  #this will print the object  <re.Match object; span=(5, 7), match='ai'>

# x=re.search(r"\bS\w+",txt)
# print(x.span())

txt="hello world"
x=re.findall("[^lo]",txt)
print(x)
if x:
  print("yes")
else:
  print("NO")

txt="hare krishna" 
x=re.search(r"\bk\w+",txt)
print(x.span())  #5,12

print(x.string)#hare krishna
print(x.group()) #krishna