# Parent class
class Student:

    def full_name(self):  # Method to set the student's full name
        self.name = "Roshan Mallick"


# Marks inherits from Student
class Marks(Student):
    def __init__(self):

        super().full_name() # Call full_name() method from Student class

        self.marks = 74


# Roll_id inherits from Marks
class Roll_id(Marks):
    def __init__(self):
        # Call Marks constructor
        super().__init__()
        self.id = 251001001177


# Academic_year inherits from Roll_id
class Academic_year(Roll_id):
    # Class variable
    year = "2nd Year"


# Information inherits from Academic_year
class Information(Academic_year):
    def __init__(self):

        super().__init__() # Call the next available __init__() in the MRO, which is Roll_id.__init__()



s1 = Information() # Create an object of Information

# Display student information
print(f"Name  : {s1.name}")
print(f"Id    : {s1.id}")
print(f"Marks : {s1.marks}")
print(f"Years : {s1.year}")
