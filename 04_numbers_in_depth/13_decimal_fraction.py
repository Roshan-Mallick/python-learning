from decimal import Decimal

num = 0.1 + 0.2  # Float precision problem
print(num)
print(type(num))

num1 = Decimal("0.1") + Decimal("0.2")

print(num1)

print(type(num1))

a = Decimal("10.5")
b = Decimal("2.0")

print( a + b )
print( a * b )
print( a / b )
print( a % b )
print( a - b )

print()
print("Fractions starts from here -----------------------------> ")
print()


from fractions import Fraction

x = Fraction(1,3)
y = Fraction(1,6)

print(x)
print(y)

print(type(y))

print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x % y )

f = Fraction(3,4)

print(f.numerator)
print(f.denominator)

test = float(Fraction(2,4))

print(test)
print(type(test))
