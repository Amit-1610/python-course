# decorator it can modify function without changing in code

# class Animal:
#     @property  # now i can call my function without brackets
#     def show(self):
#         print("Hello how are you")

# obj = Animal()
# obj.show

# create a decorator

# def decorate(func):
#     def wrapper():
#         print("I will print my self before the function hello")
#         func()
#         print("I will print after hello function")
    
#     return wrapper
# @decorate
# def hello():
#     print("Hello how are you")

# hello()
def decorate(func):
    def wrapper(*a, **k):
        print("The addition of your numbers are ")
        func(*a, **k)
        print("I hope you liked it")
    
    return wrapper
@decorate
def addition(a, b):
    print(f"Total is {a + b}")

addition(12, 50)
