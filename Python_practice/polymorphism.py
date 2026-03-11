class vehicle:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("Move!")
class Car(vehicle):
  pass
class Boat(vehicle):
  def move(self):
    print("sail!")
class plane(vehicle):
  def move(self):
    print("FLY!")

car1=Car("Ford","mustang")
boat1=Boat("Ibiza","Touring 20")
plane1=plane("airindia","747")

for x in (car1,boat1,plane1):
  print(x.brand)
  print(x.model)
  x.move()