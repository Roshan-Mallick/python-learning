import math

def circle(radius) :

 area = math.pi * ( radius ** 2)
 circumference = 2 * math.pi * radius

 return area , circumference

area , circumference = circle(int(input("Enter number : ")))

print("Area          : " , area)
print("Circumference : ",circumference )
