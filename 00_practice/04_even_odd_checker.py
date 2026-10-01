user_input = int(input("Enter number : "))

if user_input % 2 == 0:
    print(f"{user_input} is EVEN checked via modulas operator")
else:
    print(f"{user_input} is ODD checked via modulas operator ")


number = user_input

if user_input & 1 == 0:
    print(f"{number} is EVEN checked via bitwise AND operator ")
else :
    print(f"{number} is ODD checked via bitwise AND operator ")
