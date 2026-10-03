# First parent class
class Name:
    def __init__(self):

        self.name = "Roshan Mallick"


# Second parent class
class Number:
    def __init__(self):

        self.number = 999999999


# Info inherits from both Name and Number
class info(Name, Number):

    def __init__(self):

        Name.__init__(self)  # Explicitly call Name's constructor

        Number.__init__(self)  # Explicitly call Number's constructor



i1 = info()

print(f"Name   : {i1.name}")
print(f"Number : {i1.number}")
