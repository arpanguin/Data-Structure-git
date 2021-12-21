class MyClass:
    def __init__(self, name,address):
        self.Name = name
        self.Address = address

    def display(self):
        print(f"{self.Name} and {self.Address}")


s1 = MyClass("Arpan", "Mindapore")
s2 = MyClass("Raja", "Kolkata")

s1.display()
s2.display()