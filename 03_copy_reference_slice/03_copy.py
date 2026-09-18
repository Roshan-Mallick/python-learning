import copy

p1 = [1,2,3]

p2 = copy.copy(p1)  #→ creates a shallow copy (new outer object, nested objects are shared)

print(p2)

print(p1)

p1[1]= 99

print(p2)
print(p1)

p2 = copy.deepcopy(p1) #→ creates a deep copy (new object and new nested objects)

print(p2) 
print(p1)
