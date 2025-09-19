# encapsulation - I don't want to give access to variable or I want to hide internal functions and attributes of my class this is call encapsulation
# access modifiers in python :-
# 1 - Public attribute and methods
# 2 - protected attributes and methods
# 3 - private attributes and method

# 1 and 2 are work same by using _ underscore
# 3 we use __ 2 time underscore then it private no one can access

# class Factory:
#     # _a = "Haryana" # _ is now using for naming convention not for protected like other programming language
#     __a = "Haryana" # __ now it private no one can access

#     # def _show(self):
#     def __show(self):
#         print("I am factory in Haryana")


# obj = Factory()
# obj.__show()


# how to access after make private
class Factory:
    # _a = "Haryana" # _ is now using for naming convention not for protected like other programming language
    __a = "Haryana" # __ now it private no one can access

    # def _show(self):
    def show(self):
        print(Factory.__a)


obj = Factory()
obj.show()