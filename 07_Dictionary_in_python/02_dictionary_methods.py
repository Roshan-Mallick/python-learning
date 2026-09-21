# Dictionary Methods

user_info = {
    "Name": "Roshan Mallick",
    "Age": 25,
    "is_student": True,
    "Country": "India",
    "Course": "Python"
}

# Add a new key-value pair
user_info["ID"] = 1177

print(user_info)

# Remove a specific key
user_info.pop("is_student")

print(user_info)

# Remove the last inserted key-value pair
user_info.popitem()

print(user_info)

# Delete a specific key
del user_info["Course"]

print(user_info)

# Copy dictionary
user_info_1 = user_info.copy()

print(user_info_1)