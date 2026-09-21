# Dictionary Basics

user_info = {
    "Name": "Roshan Mallick",
    "Age": 25,
    "is_student": True,
    "Country": "India",
    "Course": "Python"
}

# Print complete dictionary
print(user_info)

# Check type
print(type(user_info))

# Access value using key
print(user_info["Name"])

# Access value using get()
print(user_info.get("Age"))

# Loop through dictionary keys
for key in user_info:
    print(key, user_info[key])

# Loop through keys and values
print("User information using items()")

for key, value in user_info.items():
    print(key, value)

# Number of key-value pairs
print(len(user_info))