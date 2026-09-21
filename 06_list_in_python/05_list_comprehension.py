# range()
print(range(100))


# Squared numbers
squared_numbers = [x**2 for x in range(10)]

print(squared_numbers)
print(type(squared_numbers))

# Slicing
print(squared_numbers[0:5])


# Even numbers
even_numbers = [x for x in range(20) if x % 2 == 0]

print(even_numbers)


# Odd numbers
odd_numbers = [x for x in range(20) if x % 2 != 0]

print(odd_numbers)