Id = 1177
print(Id)
print(type(Id))

Price = 99.99
print(Price)
print(type(Price))

number = 3 + 4j
print(number)
print(type(number))	

is_student = True
print(is_student)
print(type(is_student))
ls'
from decimal import Decimal

decimal_number = Decimal("10.50")
print(decimal_number)
print(type(decimal_number))

from fractions import Fraction

fraction_number = Fraction(1,3)
print(fraction_number)
print(type(fraction_number))

print()
#Checking bool as a subclass of int 
print(isinstance(True,int)) #isinstance() is a Python function used to check whether a value/object belongs to a particular data type (class).

print(True == 1)
print(False == 0)
