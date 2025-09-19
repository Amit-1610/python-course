# polymorphism

class Human:
    def show(self):
        print("Hello I am Amit")
        
class Animal(Human):
    def show(self):
        print("Hello How are you")

obj = Animal()
obj.show() # it gave my Animal show function output because it override Human show method this is polymorphism