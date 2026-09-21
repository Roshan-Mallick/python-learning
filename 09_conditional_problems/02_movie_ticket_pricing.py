age = int(input("Enter your age : "))

price = 12 if age >= 18 else 8

day = input("Enter the day : ").strip().lower()

discount = price - 2 if day == "wednesday" else price

print("Final price of the ticket : ",discount)
