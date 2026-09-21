print("Pet food recommendation food for only dog and cat")
pet = str(input("Enter what is your pet : ")).strip().lower()
age = int(input("Enter your pet age : "))

match pet :
    case "dog" :
        if age < 2 :
            print("Recommend food : Puppy food")
        else :
            print("Recommend food : Adult dog food")
    case "cat" :
        if age > 5:
            print("Recommend food : Senior cat food")
        else :
            print("Recommend food : Adult cat food")
    case _:
        print("unkown pet species")
