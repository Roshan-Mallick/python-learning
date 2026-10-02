class Car:

    wheels = 4

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


car_01 = Car("BMW","M5")
car_02 = Car("TATA","NANO")

print("Wheels :",Car.wheels)
print(car_01.brand,car_01.model)
print(car_02.brand,car_02.model)
