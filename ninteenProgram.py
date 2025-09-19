# Dunder methods - it starts and ends with double underscores

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f"Your sum of ages are {self.age + sum}"

obj = Human("Sahil", 24)
obj2 = Human("Sonty", 23)
obj3 = Human("Suman", 34)
print(obj + (obj2,obj3))