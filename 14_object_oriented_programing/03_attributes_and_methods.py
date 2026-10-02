class Full_name :
    def __init__(self):
        self.first_name = "Roshan"
        self.last_name = "Mallick"

    def name(self):
        return f"{self.first_name} {self.last_name}"

n1 = Full_name()

print(n1.name())

full_name = n1.name()

print(full_name)
