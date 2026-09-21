distance = int(input("Enter distance in km : "))

if distance <= 3 :
    transport = "Walk"
elif distance > 3 and distance <= 15 :
    transport = "Bike"
else :
    transport = "Car"

print("Ai recommends you the transport : ", transport)
