# Parent class
class Vehicle:
    brand = "BMW"


# Child class 1 - inherits from Vehicle
class Car(Vehicle):
    model = "M5"


# Child class 2 - inherits from Vehicle
class Bike(Vehicle):
    engine = "1000cc"


# Child class - inherits from both Car and Bike (Multiple Inheritance)

class sports_vehicle(Car, Bike):
    speed = 300



v1 = sports_vehicle()


print(f"Brand  : {v1.brand}")   # Access data inherited from Vehicle

print(f"Model  : {v1.model}")   # Access data inherited from Car

print(f"Engine : {v1.engine}")  # Access data inherited from Bike

print(f"Speed  : {v1.speed}")  # Access data from sports_vehicle
