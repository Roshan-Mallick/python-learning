text = "PYTHON IS AWESOME"

print(text)

for index, char in enumerate(text):
    print(f"{index} : {char}")

print()
print(text[0:6]) #get charecters at index 0,1,2,3,4,5 stops BEFORE index 6 --> "PYTHON"

print(text[::2]) #Every 2nd character starting from beginning

print(text[::-1]) #Entire string backwards
