p1 = [10,20,30] 
p2 = p1 #both point to the same object of list #obj1

print(p1)
print(p2) 

p2[0] = 100
print(p2)

print(p1)

p2 = [10,20,30]  #new object for p2  #obj2

print(p2)  #obj2

print(p1)   #obj1
