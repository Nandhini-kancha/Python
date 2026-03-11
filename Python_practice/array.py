cars=["ford","volvo","BMW"]
print(len(cars))


for x in cars:
  print(x)

cars.append("honda") #adding array elements
cars.pop(1) #poping array elements

cars.remove("BMW")  # only removes the first occurence of the value

for x in cars:
  print(x)
