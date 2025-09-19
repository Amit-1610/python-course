#do not use number in the starting of veriable
# do not use spaces in veriables# 
#do not use special characters in variables

# use camelcase for better practice, pascal case(first and mid letter large), snake case (_) between words

amit = "Amit is a developer"
print(type(amit))

a = 12
print(type(a))

b = 3.5
print(type(b))

c = 22/7
print(type(c))

d = 43j
print(type(d))  # while use 'j' it make 'complex data types'

e = True
print(type(e))

f = False
print(type(f))

g = 'a'
print(ord(g))

h = 'A'
print(ord(h))

i = 67
print(chr(i))

indexing = "hello amit"
print(indexing[-4], indexing[5])

str_slice = "make string slicing"
print(str_slice[1:6:2])  # [start:end:steps] steps means how much you cover in (1) means it cover in serials line or jump (2) or multiple words

# type conversion
k = 12
k = str(k)
print(k)
print(type(k))
