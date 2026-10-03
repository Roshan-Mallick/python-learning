# Parent class
class Employee:
    def work(self):
        print("Employee is working")


# Child class 1 - inherits from Employee(Parent)
class Dev(Employee):
    def code(self):
        print("Developer is working")


# Child class 2 - inherits from Employee(Parent)
class Ui(Employee):
    def design(self):
        print("Designer is designing")


developer = Dev()

developer.work()
developer.code()

designer = Ui()

designer.work()
designer.design()
