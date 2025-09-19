# loops

# two types of loop
# for loop and while loop

# for loop :-
# before for loop understand range
# range(start, stop, steps)

# for i in range(1, 20, 1):
#     print(i)

# for i in range(16, 0, -1):
#     print(i)


# for i in range(-5, -16, -1):
#     print(i)

# for i in range(5, 51, 5):
#     print(i)

# n = int(input("which table you want ? "))

# for i in range(n, (n*10)+1, n):
#     print(i)

# loops for string

# a = "Amit Kinha , I am a developer"
# for i in range(len(a)):
#     print(a[i])

# Break continue else
# else use with break , this else is not of if condition else this else is use in loop

# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1, 21):
#     if i == 15:
#         continue
#     print(i)

# for i in range(1, 21):
#     if i == 30:
#         print("Break statement is executed")
#         break
#     print(i)
# else:
#     print("Break statement is not executed")


# n = int(input("check your number is perfect or not :- "))
# sum = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i
# if sum == n:
#     print("Your number is perfect")
# else:
#     print("your number is not perfect")


# number is prime or not

# n = int(input("check your number is prime or not :- "))

# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

# other for count prime number

# n = int(input("check your number is prime or not :- "))
# count = 0

# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")

# reverse string
# a = "Amit Kinha"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     # print(a[i])
#     b = b + a[i]
#     # print(b)
# print(b)

# pallindrome or not

a = "nitin"
b = ""
for i in range(len(a)-1, -1, -1):
    b = b + a[i]
if b == a:
    print("your string is pallindrome")
else: 
    print("your string is not")