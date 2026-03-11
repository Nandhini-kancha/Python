import json
x='{"name":"nandhu","age":30,"city":"newdelhi"}'
y=json.loads(x)
print(y["age"])



x={"name":"nandhu","age":30,"city":"newdelhi"}
y=json.dumps(x)
print(y)


  # dumps==>converts python to json 
  # loads==>converts json to python