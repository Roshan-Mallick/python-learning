import sys

marks = int(input("Enter you marks : "))

if marks > 100 or marks < 0 :
   print("Enter marks between 0 to 100")
   sys.exit()

if marks >=90 :
   grade = 'A'
elif marks >= 80 :
   grade = 'B'
elif marks >= 70 :
   grade = 'C'
elif marks >= 60 :
   grade = 'D'
elif marks >= 50 :
   grade = 'E'
else :
   grade = 'Fail'

print("Grade : ",grade)
