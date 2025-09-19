# OOPS

# class Factory:
#     a = 14 # this is an attribute

#     def hello(self): # method and here self for is a perameter
#         print("How are you?")

#     print("Hello how are you I am getting initialized")

# print(Factory().a)
# Factory().hello()

# object in oops
# obj = Factory()
# print(obj.a)

# # constructor

# class Company:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
#     def show(self):
#         print(f"your materials are {self.material}, {self.pockets}, {self.pockets}")
        
# reebok = Company("Leather", 3, 2)
# campus = Company("Nylon", 3, 3)
# reebok.show()

class Animal:
    name = "Lion"

    def __init__(self, age):
        self.age = age # instance attribute

    def show(self): # instance method
        print(f"Your age is {self.age}")
    
    @classmethod
    def hello(cls):
        print("This is a class method")

    @staticmethod
    def static():
        print("Hello Brother")

obj = Animal(16)
obj.show()
obj.hello()
obj.static()