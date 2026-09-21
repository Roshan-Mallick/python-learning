computer_lang = ["python", "java", "c++", "c", "javascript", "golang", "rust"]

# append()
computer_lang.append("kotlin")
print(computer_lang)

# pop()
computer_lang.pop()
print(computer_lang)

# remove()
computer_lang.remove("python")
print(computer_lang)

# insert()
computer_lang.insert(0, "python")
print(computer_lang)

# copy()
c_lang = computer_lang.copy()

print(c_lang)

c_lang.append("assembly")

print(c_lang)
print(computer_lang)  # original list is unchanged