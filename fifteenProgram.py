# inheritance

# class FactoryDelhi: # parent class / superclass
#     a = "I am an attribute mentioned inside factory"
#     def hello(self):
#         print("I am a method inside in factory")

# class FactoryHaryana(FactoryDelhi): # child class inherit parent class / subclass
#     pass

# obj = FactoryDelhi()
# obj2 = FactoryHaryana()
# print(obj.a)
# print(obj2.hello()) # if you see none after the function calling don't worry function calling always gave none type


# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def show(self):
#         print(f"My name is {self.name}")
    

# class Human(Animal): # now the child class have power of the constructor which is in parent class
#     def __init__(self, name, age):
#         super().__init__(name) # super function target parent class
#         self.age = age
        
#     def show(self):  # method overiding
#         print(f"My name is {self.name}, {self.age}")

# animal1 = Animal("Lion")
# animal1.show()
# person1 = Human("Amit Kinha", 24)
# person1.show()


# multilevel inheritance

# class Animal:
#     name1 = "Lion"

# class Human:
#     name2 = "Amit"

# class Robot(Animal, Human):
#     name3 = "Charlie123"

# obj = Robot()
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)


class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class DelhiFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class HaryanaFactory(DelhiFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = HaryanaFactory()
