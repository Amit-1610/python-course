# input and outputs

# formated string, use 'f' in starting and declare variable in single string using '{}'

amit = "My name is Amit"
age = 24
print("about me", amit, "and my age is", age)
print(f"about me {amit} and my age is {age}")

# input function, we also use type conversion in input
name = str(input("what is your name? "))
name = input("what is your name? ")
print(type(name))
print(name)

# operators
# Arithmetic operators

# addition                             +
# substraction                         -
# multiplication                       *
# division                             /
# Floor Division                      //
# modules                              %
# Exponentation                       **

# --------------------------------------

# addition
add1 = 20
add2 = 4
add3 = 58
print(add1 + add2 + add3)
print(add1 - add2 - add3)
print(add1 * add2 * add3)
print(add1 / add2) # always provide answer in float in the end it show .0
print(add1 // add2) # it remove float value it provide output in integer
print(add1 % add3)  # it finds reminder
print(add2 ** add3) # this use for power(cube)


# BODMAS
# Brackets, Orders(powers or roots), Division, Multiplication, Addition, Substraction

print(12+4/2) # in this first divide 4 by 2 then add reminder to 12