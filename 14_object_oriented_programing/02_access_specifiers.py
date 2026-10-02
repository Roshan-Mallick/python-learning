class Student:
    def __init__(self):

        # All the name variables are treated differently

        self.name = "Roshan 1177"         # Public
        self._name = "Roshan 1178"        # Protected
        self.__name = "Roshan 1179"       # Private

        # Private data can be accessed indirectly using a public attribute
        self.use_private = self.__name

       # Public method can access private data
    def access_private(self):
        print(self.__name)

    # Private method
    def __access_private(self):
        print(self.name)

    # Public method used to call the private method
    def call_private_method(self):
        self.__access_private()


# -------- OUTSIDE THE CLASS --------

s1 = Student()

print(s1.name)               # Public
print(s1._name)              # Protected → Technically possible but not recommended

# print(s1.__name)           # Private → ❌ Direct access

print(s1.use_private)        # Private data via public attribute
s1.access_private()          # Private data via public method

# s1.__access_private()      # Private method → ❌ Direct access

s1.call_private_method()     # Private method via public method
