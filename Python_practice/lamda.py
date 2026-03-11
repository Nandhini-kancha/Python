#syntax   lamda arguments:expression
x=lambda a:a+10
print(x(5))


x=lambda a,b :a*b
print(x(5,6))

def myfunc(n):
 return lambda a:a*n  #n=2 amd n=3 a=11
mydouble=myfunc(2)
mytripler=myfunc(3)

print(mydouble(11))  #22
print(mytripler(11))  #33



#mydouble=myfunc(2)
#   returns lambda a:a*2
#   n=3 returns lambda a:a*3
#  that means mytripler(a)=a*3 and mydouble(a)=a*2
# when mydouble and mytripler func calls then the values willl be evaluated

#map(),filter(),sorted() are commonly used built in fun in lambda

num=[1,4,5,8,9]
double =list(map(lambda x:x*2,num))
print(double)


odd_num=list(filter(lambda s:s%2 !=0,num))
print(odd_num)

students=[("emil",25),("tom",22),("jerry",34)]
sorted_stu =sorted(students,key=lambda x:x[1])
print(sorted_stu)

words=["apple","pie","banana"]
sorted_words=sorted(words,key=lambda x:len(x))
print(sorted_words)