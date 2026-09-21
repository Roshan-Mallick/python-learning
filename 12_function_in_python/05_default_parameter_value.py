def greet(name = "user"):
    return "Hello "+ name

name = str(input("Enter your name : "))

print(greet(name))
print(greet()) #use the parameter value
