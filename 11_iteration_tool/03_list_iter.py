list = [1,2,3,4,]

I = iter(list)

print(I)
print(type(I))

print(I.__next__())

print(I.__next__())

print(I.__next__())

print(I.__next__())

#print(I.__next__()) #error cause we had iterate fulllist before this
