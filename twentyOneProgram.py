# Args (*) and Kwargs (**)

# def addition(*a):
#     sum = 0
#     for i in a:
#         sum = sum + i
#     print(sum)
# addition(12, 50, 23, 20, 59, 584, 56, 34, 67)

# kwargs
def information(**a):
    print("Your information is \n")
    for i in a:
        print(f"{i} : {a[i]}")

information(first = "Amit", last = "Kinha", age = 24, designation = "Developer")