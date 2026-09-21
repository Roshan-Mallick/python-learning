computer_lang = ["python", "java", "c++", "c", "javascript", "golang", "rust"]

print(computer_lang[0:3])       # slicing
print(computer_lang[0:6:2])    # slicing with step

computer_lang[4] = "ruby"      # updating a value
print(computer_lang)

computer_lang[5:7] = ["c#", "typescript"]
print(computer_lang)

computer_lang[1:1] = ["php"]   # inserting at index 1
print(computer_lang)

computer_lang[2:3] = []        # removing value using slice
print(computer_lang)