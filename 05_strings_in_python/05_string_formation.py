name = input("Enter your full name : ")
age = input ("Enter your age : ")
course = input ("Enter your course : ")

print("My name is " + name)

print("My name is {} and I am {} years old.".format(name,age)) #using .format

print("I am {} years old and I study {} ".format(age,course))

print("Name : {name} , Age : {age} , course : {course} ".format(  #using named placeholders

    name = name ,
    age = age ,
    course = course

    ))

print(f"My Name is {name} and I am {age} years old.") #using f string

print(f"Next year i will be {age+1} years old")
