p1 = [10,20,30]

p2 = p1 [1:2] 

print(p2)

p3 = p1 [:] # slice copy new object

print(p3) 

p3[1]=89

p2[0] = 101 

p1[2] = 67


print("Final list ------------------------->")

print(p1)
print(p2)
print(p3)
