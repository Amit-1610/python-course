# functions

# def hello():
#     print("this is a hello function")

# hello()

# perameters and arguments in function
# positional arguments
# num1 = int(input("first number :- "))
# num2 = int(input("second number :- "))
# def sum(a, b):
#     add = a + b
#     print(f"Sum of your number is {add}")

# sum(num1, num2)

#  key word argument
# def hello(name , age):
#     print(f"your name is {name} and your age is {age}")


# hello(age=22, name="Amit Kinha")

# default arguments

# num1 = int(input("first number :- "))
# num2 = int(input("second number :- "))
# def sum(a, b=34):
#     add = a + b
#     print(f"Sum of your number is {add}")

# sum(num1, num2)
# st = str(input("Provide name :- "))
# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
#     if rev == st:
#         print(f"{st} String is pallindrome")
#     else:
#         print(f"{st} not pallindrome")

# pallindrome(st)

def hello():
    return "hello boss"

print(hello())