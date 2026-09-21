# Dictionary Comprehension

# Create dictionary containing numbers and their squares
squared_number = {
    x: x ** 2
    for x in range(1, 11)
}

print(squared_number)


# Create dictionary containing only even numbers
even_number = {
    x: x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_number)


# Clear all items from dictionary
even_number.clear()

print(even_number)