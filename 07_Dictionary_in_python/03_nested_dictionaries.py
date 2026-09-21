# Nested Dictionaries

user_data = {

    "user1": {
        "Name": "Roshan Mallick",
        "Age": 25,
        "is_student": True,
        "Country": "India",
        "Course": "Python"
    },

    "user2": {
        "Name": "John Doe",
        "Age": 30,
        "is_student": False,
        "Country": "USA",
        "Course": "JavaScript"
    }
}

# Print complete nested dictionary
print(user_data)

# Check type
print(type(user_data))

# Access nested dictionary
print(user_data["user1"])

# Access a specific nested value
print(user_data["user1"]["Name"])

print(user_data["user2"]["Course"])