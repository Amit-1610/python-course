# assignment operators (=)
# +=                           Add and assign
# -=                           Substract and assign
# *=                           Multiply and assign
# /=                           Divide and assign
# //=                          Floor divide and assign
# %=                           Modules and assign
# **=                          Exponentiation and assign

# compound assignment operator

a = 20
# a = 40 # reassign value
# a = a + 60
a += 30
print(a)

# ------------------------------------------------------------------- 

# comparison operator

# ==                              Equal to
# !=                              Not Equal to
# >                               Greater than
# <                               Less than
# >=                              Greate than or equal to
# <=                              Less than or equal to

b = 12.6
c = 15
print(b == c)
print(b != c)
print(b > c)
print(b < c)
print(b >= c)
print(b <= c)
print(ord("A"), ord("B"))
print("A" > "B")

# -------------------------------------------------------------------

# Logical Operators

# and              Return True if both conditions are true, if first condition is false then it not check next condition
# or               Return True if at least one condition is true
# not              Reverse the boolean value

print("Logical Operators Output")
print(123 > 100 and 34 > 23 and 65 < 66)
print(123 > 123 or 34 > 34 or 123 >= 123)
print(not 12 == 12)