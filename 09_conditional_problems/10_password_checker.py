password = str(input("Enter your password : "))

pass_check = len(password)

if (pass_check < 6) :
    print("Weak")
elif ( pass_check <= 10) :
    print("Medium")
else :
    print("Strong")
