# Parent class
class Vehicle:

    wheels = 4 # Class variable


# Child class inheriting from Vehicle
class Car(Vehicle):

    # Constructor of Car
    def __init__(self):
        # Instance variables
        self.brand = "BMW"
        self.model = "M5"


c1 = Car() # Create an object of Car

# Access Car's instance variables
print(f"Brand: {c1.brand}")
print(f"Model: {c1.model}")

# Access the wheels variable inherited from Vehicle through Car (inheritance)
print(f"Wheels: {c1.wheels}")
