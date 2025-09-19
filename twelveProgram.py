# exception handling

# this is about errors
# a = 12
# if a == 12:
# print(a)

# keywords for handle exception :-

# try                wrap the block of code that might cause an exception
# except             handle the exception if it occurs
# else               run code only if no exception occur
# finally            run code no matter what, weather there's and exception or not
# raise              manually throw an exception

a = 565
try:
    print(a/7)
# except ZeroDivisionError:
#     print("Sorry you can not divide by 0")
except Exception as err:
    print(f"Sorry there is and error {err}")
else:
    print("Good there is no exception")
finally:
    print("Run your code if there is an error or other")