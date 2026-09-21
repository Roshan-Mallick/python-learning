
char = str(input("Enter your string : "))

for i in char :
    if char.count(i) == 1 :
        print("char is : ",i)
        break
