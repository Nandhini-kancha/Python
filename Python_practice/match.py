#match is similar to case stmt
day=4
match day:
  case 1:
    print("monday")
  case 2:
    print("tuesday")
  case 3:
    print("wednesday")
  case 4:
    print("thursday")
  case 5:
    print("friday")
  case 6:
    print("saturday")
  case 7:
    print("sunday")
  case _:
    print("please enter a day from 1 to 7")


 #use the | pipe symbol as an operator in the case to check for more than one value match in one case:

match day:
  case 1|2|3|4:
    print("today is holiday")
  case _:
    print("no holiday")