#Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

#Subclass car
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

#Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

#Demonstrating polymorphism
vehicle = [Car(), Bicycle()]

for v in vehicle:
    v.move()