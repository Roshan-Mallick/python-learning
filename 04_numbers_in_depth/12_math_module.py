import math

print(math.floor(3.5))       # Floor → rounds down → 3
print(math.floor(-3.5))      # Floor → rounds down → -4

print(math.trunc(2.8))       # Trunc → removes decimal → 2
print(math.trunc(-2.8))      # Trunc → removes decimal toward zero → -2

num = int(math.sqrt(25))     # sqrt() returns float → int() converts to int
print(num)
print(type(num))

print(math.sqrt(49))         # Square root → 7.0 (float)

print(math.pow(2, 3))        # Power → 2 × 2 × 2 → 8.0 (float)

n = int(math.pow(2, 4))      # Convert float result to int
print(type(n))
print(n)

print(math.ceil(3.0009))     # Ceiling → rounds up toward +infinity → 4


